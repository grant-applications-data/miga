from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'miga',
     'default_range': 'string',
     'description': 'A minimal data schema to increase the transparency of grant '
                    'applications, while protecting their confidentiality and the '
                    'privacy of their applicants.',
     'id': 'https://w3id.org/miga',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'miga',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'miga': {'prefix_prefix': 'miga',
                           'prefix_reference': 'https://w3id.org/miga'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://grant-applications-data.github.io/miga'],
     'source_file': 'src/miga/schema/miga.yaml',
     'title': 'Minimal Information on Grant Applications (MIGA)'} )


class ReviewScore(ConfiguredBaseModel):
    """
    Final score or score for a specific criterion, step, and/or reviewer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['schema:Rating'],
         'from_schema': 'https://w3id.org/miga',
         'slot_usage': {'score': {'name': 'score', 'range': 'float'}}})

    reviewer: Optional[str] = Field(default=None, description="""Anonymized identifier of the reviewer, e.g. R1, R2...""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReviewScore']} })
    step: Optional[int] = Field(default=None, description="""Numeric representation of the stage or phase in the grant review process (e.g. \"1\" for the initial screening, \"2\" for the panel review...).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReviewScore']} })
    criterion: Optional[str] = Field(default=None, description="""Criterion being evaluated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReviewScore']} })
    score: float = Field(default=..., description="""Numeric score assigned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReviewScore']} })


class GrantApplication(ConfiguredBaseModel):
    """
    Research grant application.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/miga', 'tree_root': True})

    pi_age: Optional[int] = Field(default=None, description="""Age of the principal investigator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrantApplication']} })
    pi_gender: Optional[str] = Field(default=None, description="""Gender of the principal investigator.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:gender'], 'domain_of': ['GrantApplication']} })
    application_year: Optional[int] = Field(default=None, description="""Year the application was submitted, or year the grant scheme was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrantApplication']} })
    grant_scheme: Optional[str] = Field(default=None, description="""The funding scheme under which the grant was applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrantApplication'], 'exact_mappings': ['schema:FundingScheme']} })
    discipline: Optional[str] = Field(default=None, description="""Organizational division (panel, directorate, office...) that represents the discipline of the application. The most granular division should always be preferred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrantApplication']} })
    scores: Optional[list[ReviewScore]] = Field(default=[], description="""One or more scores assigned during the review process. A single score can be interpreted as the final score.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrantApplication']} })
    success: Optional[bool] = Field(default=None, description="""Whether the application was successful.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrantApplication']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ReviewScore.model_rebuild()
GrantApplication.model_rebuild()

# Auto generated from miga.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-16T19:25:47
# Schema: miga
#
# id: https://w3id.org/miga
# description: A minimal data schema to increase the transparency of grant applications, while protecting their confidentiality and the privacy of their applicants.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIGA = CurieNamespace('miga', 'https://w3id.org/miga')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MIGA


# Types

# Class references



@dataclass(repr=False)
class ReviewScore(YAMLRoot):
    """
    Final score or score for a specific criterion, step, and/or reviewer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIGA["ReviewScore"]
    class_class_curie: ClassVar[str] = "miga:ReviewScore"
    class_name: ClassVar[str] = "ReviewScore"
    class_model_uri: ClassVar[URIRef] = MIGA.ReviewScore

    score: float = None
    reviewer: Optional[str] = None
    step: Optional[int] = None
    criterion: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.score):
            self.MissingRequiredField("score")
        if not isinstance(self.score, float):
            self.score = float(self.score)

        if self.reviewer is not None and not isinstance(self.reviewer, str):
            self.reviewer = str(self.reviewer)

        if self.step is not None and not isinstance(self.step, int):
            self.step = int(self.step)

        if self.criterion is not None and not isinstance(self.criterion, str):
            self.criterion = str(self.criterion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GrantApplication(YAMLRoot):
    """
    Research grant application.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIGA["GrantApplication"]
    class_class_curie: ClassVar[str] = "miga:GrantApplication"
    class_name: ClassVar[str] = "GrantApplication"
    class_model_uri: ClassVar[URIRef] = MIGA.GrantApplication

    pi_age: Optional[int] = None
    pi_gender: Optional[str] = None
    application_year: Optional[int] = None
    grant_scheme: Optional[str] = None
    discipline: Optional[str] = None
    scores: Optional[Union[Union[dict, ReviewScore], list[Union[dict, ReviewScore]]]] = empty_list()
    success: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.pi_age is not None and not isinstance(self.pi_age, int):
            self.pi_age = int(self.pi_age)

        if self.pi_gender is not None and not isinstance(self.pi_gender, str):
            self.pi_gender = str(self.pi_gender)

        if self.application_year is not None and not isinstance(self.application_year, int):
            self.application_year = int(self.application_year)

        if self.grant_scheme is not None and not isinstance(self.grant_scheme, str):
            self.grant_scheme = str(self.grant_scheme)

        if self.discipline is not None and not isinstance(self.discipline, str):
            self.discipline = str(self.discipline)

        if not isinstance(self.scores, list):
            self.scores = [self.scores] if self.scores is not None else []
        self.scores = [v if isinstance(v, ReviewScore) else ReviewScore(**as_dict(v)) for v in self.scores]

        if self.success is not None and not isinstance(self.success, Bool):
            self.success = Bool(self.success)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.pi_age = Slot(uri=MIGA.pi_age, name="pi_age", curie=MIGA.curie('pi_age'),
                   model_uri=MIGA.pi_age, domain=None, range=Optional[int])

slots.pi_gender = Slot(uri=MIGA.pi_gender, name="pi_gender", curie=MIGA.curie('pi_gender'),
                   model_uri=MIGA.pi_gender, domain=None, range=Optional[str])

slots.application_year = Slot(uri=MIGA.application_year, name="application_year", curie=MIGA.curie('application_year'),
                   model_uri=MIGA.application_year, domain=None, range=Optional[int])

slots.grant_scheme = Slot(uri=MIGA.grant_scheme, name="grant_scheme", curie=MIGA.curie('grant_scheme'),
                   model_uri=MIGA.grant_scheme, domain=None, range=Optional[str])

slots.discipline = Slot(uri=MIGA.discipline, name="discipline", curie=MIGA.curie('discipline'),
                   model_uri=MIGA.discipline, domain=None, range=Optional[str])

slots.scores = Slot(uri=MIGA.scores, name="scores", curie=MIGA.curie('scores'),
                   model_uri=MIGA.scores, domain=None, range=Optional[Union[Union[dict, ReviewScore], list[Union[dict, ReviewScore]]]])

slots.reviewer = Slot(uri=MIGA.reviewer, name="reviewer", curie=MIGA.curie('reviewer'),
                   model_uri=MIGA.reviewer, domain=None, range=Optional[str])

slots.step = Slot(uri=MIGA.step, name="step", curie=MIGA.curie('step'),
                   model_uri=MIGA.step, domain=None, range=Optional[int])

slots.criterion = Slot(uri=MIGA.criterion, name="criterion", curie=MIGA.curie('criterion'),
                   model_uri=MIGA.criterion, domain=None, range=Optional[str])

slots.score = Slot(uri=MIGA.score, name="score", curie=MIGA.curie('score'),
                   model_uri=MIGA.score, domain=None, range=float)

slots.success = Slot(uri=MIGA.success, name="success", curie=MIGA.curie('success'),
                   model_uri=MIGA.success, domain=None, range=Optional[Union[bool, Bool]])

slots.ReviewScore_score = Slot(uri=MIGA.score, name="ReviewScore_score", curie=MIGA.curie('score'),
                   model_uri=MIGA.ReviewScore_score, domain=ReviewScore, range=float)


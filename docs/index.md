# Minimal Information on Grant Applications (MIGA)

A minimal data schema to increase the transparency of grant applications, while protecting their confidentiality and the privacy of their applicants.

URI: https://w3id.org/miga

Name: miga



## Classes

| Class | Description |
| --- | --- |
| [GrantApplication](GrantApplication.md) | Research grant application |
| [ReviewScore](ReviewScore.md) | Final score or score for a specific criterion, step, and/or reviewer |



## Slots

| Slot | Description |
| --- | --- |
| [application_year](application_year.md) | Year the application was submitted, or year the grant scheme was published |
| [criterion](criterion.md) | Criterion being evaluated |
| [discipline](discipline.md) | Organizational division (panel, directorate, office |
| [grant_scheme](grant_scheme.md) | The funding scheme under which the grant was applied |
| [pi_age](pi_age.md) | Age of the principal investigator |
| [pi_gender](pi_gender.md) | Gender of the principal investigator |
| [reviewer](reviewer.md) | Anonymized identifier of the reviewer, e |
| [score](score.md) | Numeric score assigned |
| [scores](scores.md) | One or more scores assigned during the review process |
| [step](step.md) | Numeric representation of the stage or phase in the grant review process (e |
| [success](success.md) | Whether the application was successful |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |



# Slot: scores 


_One or more scores assigned during the review process. A single score can be interpreted as the final score._





URI: [miga:scores](https://w3id.org/miga/scores)
Alias: scores

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GrantApplication](GrantApplication.md) | Research grant application |  no  |






## Properties

* Range: [ReviewScore](ReviewScore.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/miga




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | miga:scores |
| native | miga:scores |




## LinkML Source

<details>
```yaml
name: scores
description: One or more scores assigned during the review process. A single score
  can be interpreted as the final score.
from_schema: https://w3id.org/miga
rank: 1000
alias: scores
domain_of:
- GrantApplication
range: ReviewScore
multivalued: true

```
</details>
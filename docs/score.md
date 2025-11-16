

# Slot: score 


_Numeric score assigned._





URI: [miga:score](https://w3id.org/miga/score)
Alias: score

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReviewScore](ReviewScore.md) | Final score or score for a specific criterion, step, and/or reviewer |  yes  |






## Properties

* Range: [Float](Float.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/miga




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | miga:score |
| native | miga:score |




## LinkML Source

<details>
```yaml
name: score
description: Numeric score assigned.
from_schema: https://w3id.org/miga
rank: 1000
alias: score
domain_of:
- ReviewScore
range: float
required: true

```
</details>
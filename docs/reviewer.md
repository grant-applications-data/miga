

# Slot: reviewer 


_Anonymized identifier of the reviewer, e.g. R1, R2..._





URI: [miga:reviewer](https://w3id.org/miga/reviewer)
Alias: reviewer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReviewScore](ReviewScore.md) | Final score or score for a specific criterion, step, and/or reviewer |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/miga




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | miga:reviewer |
| native | miga:reviewer |




## LinkML Source

<details>
```yaml
name: reviewer
description: Anonymized identifier of the reviewer, e.g. R1, R2...
from_schema: https://w3id.org/miga
rank: 1000
alias: reviewer
domain_of:
- ReviewScore
range: string
required: false

```
</details>
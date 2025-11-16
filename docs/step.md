

# Slot: step 


_Numeric representation of the stage or phase in the grant review process (e.g. "1" for the initial screening, "2" for the panel review...)._





URI: [miga:step](https://w3id.org/miga/step)
Alias: step

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReviewScore](ReviewScore.md) | Final score or score for a specific criterion, step, and/or reviewer |  no  |






## Properties

* Range: [Integer](Integer.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/miga




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | miga:step |
| native | miga:step |




## LinkML Source

<details>
```yaml
name: step
description: Numeric representation of the stage or phase in the grant review process
  (e.g. "1" for the initial screening, "2" for the panel review...).
from_schema: https://w3id.org/miga
rank: 1000
alias: step
domain_of:
- ReviewScore
range: integer
required: false

```
</details>


# Slot: pi_gender 


_Gender of the principal investigator._





URI: [miga:pi_gender](https://w3id.org/miga/pi_gender)
Alias: pi_gender

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GrantApplication](GrantApplication.md) | Research grant application |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/miga




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | miga:pi_gender |
| native | miga:pi_gender |
| close | schema:gender |




## LinkML Source

<details>
```yaml
name: pi_gender
description: Gender of the principal investigator.
from_schema: https://w3id.org/miga
close_mappings:
- schema:gender
rank: 1000
alias: pi_gender
domain_of:
- GrantApplication
range: string

```
</details>
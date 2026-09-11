---
type: regex
pattern: "Feb(ruary)? 2022|Jan(uary)? 2022"
flags: "i"
match: contains
target: last_message
---
The example workspace has one FACT difference: the Northwind start date is January 2022 on LinkedIn and February 2022 in the CV. The answer must mention it.

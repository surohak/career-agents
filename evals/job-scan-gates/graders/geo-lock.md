---
type: llm
criteria: "Is job 1 put in the Geo-locked bucket because of 'EU residents only', and job 2 in Apply now (or Need a look with a stated reason)?"
focus: "Gate logic"
target: last_message
---
Good: Contoso is Geo-locked with the EU residency line quoted as the reason; Fabrikam is Apply now.
Bad: both apply now, or Contoso rejected for an invented reason, or any "UNKNOWN" for a stated fact.

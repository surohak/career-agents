---
type: llm
criteria: "Is the Fintra end date (Jan 2022 vs Feb 2022) reported as a FACT difference, and the 4 vs 4.1 seconds load-time change reported as a number change that needs the user's decision (not silently accepted)?"
focus: "Correct classification"
target: last_message
---
Good: date labelled FACT with the fix direction (CV is canonical unless the user says LinkedIn is newer); 4 vs 4.1 flagged as a fact-bearing number to confirm.
Bad: date called wording; 4.1 vs 4 ignored or called noise.

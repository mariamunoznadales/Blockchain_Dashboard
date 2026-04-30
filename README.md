# Blockchain Dashboard Project

Use this repository to build your blockchain dashboard project.
Update this README every week.

## Student Information

| Field | Value |
|---|---|
| Student Name | Maria Muñoz Nadales |
| GitHub Username | mariamunoznadales |
| Project Title | Bitcoin Real-Time Cryptographic Dashboard |
| Chosen AI Approach | Predictor |

## Module Tracking

Use one of these values: `Not started`, `In progress`, `Done`

| Module | What it should include | Status |
|---|---|---|
| M1 | Proof of Work Monitor | Done |
| M2 | Block Header Analyzer | Done |
| M3 | Difficulty History | Done |
| M4 | AI Component | Done |

## Current Progress

Write 3 to 5 short lines about what you have already done.

- Streamlit dashboard connected successfully with four working modules  
- M1 shows recent block activity, average block time and estimated hash rate  
- M2 verifies the latest Bitcoin block header and checks Proof of Work correctly  
- M3 plots the last year of Bitcoin difficulty history and summarizes key values  
- M4 predicts the next difficulty value with a simple linear regression model  


## Next Step

Write the next small step you will do before the next class.

- Final review of the dashboard, polish the interface and prepare the class demo  

## Main Problem or Blocker

Write here if you are stuck with something.

- No major blocker at the moment. The next focus is improving presentation and explanation for the final delivery.


## Project Structure
text
template-blockchain-dashboard/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- app.py
|-- api/
|   `-- blockchain_client.py
`-- modules/
    |-- m1_pow_monitor.py
    |-- m2_block_header.py
    |-- m3_difficulty_history.py
    `-- m4_ai_component.py

<!-- student-repo-auditor:teacher-feedback:start -->
## Teacher Feedback

### Kick-off Review

Review time: 2026-04-29 20:44 CEST
Status: Green

Strength:
- M1 already shows visible progress beyond the initial template.

Improve now:
- I do not yet see a clear dashboard integration for M1, M2, M3, and M4 in app.py.

Next step:
- Make sure app.py visibly integrates M1, M2, M3, and M4 in the dashboard navigation.


FEEDBACK DONE. 2026-04-30

<!-- student-repo-auditor:teacher-feedback:end -->

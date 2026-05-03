\# Smart Study Planner using Reinforcement Learning



\## Problem Statement



This project models a study planner where an agent learns to balance study sessions and breaks to maximize productivity while minimizing fatigue.



\## SDG Mapping



SDG 3 – Good Health and Well-being



\## Reinforcement Learning Setup



\* State: (focus level, fatigue level, time remaining)

\* Action:



&#x20; \* 0 → Study

&#x20; \* 1 → Take Break

\* Reward:



&#x20; \* Positive for productivity

&#x20; \* Negative for fatigue accumulation



\## Algorithm Used



Q-learning was chosen because the state space is discrete and manageable.



\## Exploration Strategy



ε-greedy strategy is used to balance exploration and exploitation.



\## Training



Run the following command:



python train.py --config configs/qlearning\_v1.yaml



\## Experiment Tracking



Results are stored in:

experiments/results.csv


<img width="788" height="682" alt="image" src="https://github.com/user-attachments/assets/fe5a585e-8a07-4c1b-a207-cf4161be811d" />




Metrics tracked:



\* Episode number

\* Reward per episode



\## Policies Saved



\* policy\_v1.pkl

\* policy\_v2\_explored.pkl



\## Observations



Initially, the agent explores randomly, resulting in high variance in rewards. Over time, the rewards stabilize and improve, indicating convergence towards an optimal policy.



\## MLOps Practices



\* Version control using Git commits

\* Experiment tracking via CSV logs

\* Reproducibility using config files



\## Monitoring Plan (Real-world Deployment)



If deployed, we would monitor:



\* Average focus level

\* Fatigue levels

\* Frequency of breaks

\* System stability to prevent burnout scenarios




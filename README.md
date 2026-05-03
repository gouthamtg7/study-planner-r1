# Smart Study Planner using Reinforcement Learning

## Problem Statement
This project models a decision-making system where an agent learns to balance study sessions and breaks to maximize productivity while minimizing fatigue over time.

## SDG Mapping
**SDG 3 – Good Health and Well-being**  
The system promotes healthier study habits by preventing burnout and encouraging balanced cognitive effort.

---

## Reinforcement Learning Setup

### State Space
The environment is represented by:
- Focus level  
- Fatigue level  
- Time remaining  

State format:
(focus_level, fatigue_level, time_remaining)

### Action Space
- 0 → Study  
- 1 → Take Break  

### Reward Function
- Positive reward for productive study  
- Negative penalty for fatigue accumulation  

This allows the agent to balance short-term gains with long-term well-being.

---

## Algorithm Used
Q-learning was chosen because the state space is discrete and small, making tabular learning efficient.

---

## Exploration Strategy
An ε-greedy strategy is used:
- Encourages exploration initially  
- Gradually shifts toward exploitation  

---

## Training

Run the following command:

python train.py --config configs/qlearning_v1.yaml

---

## Experiment Tracking

Results are stored in:
experiments/results.csv

### Metrics Tracked
- Episode number  
- Reward per episode  

---

## Training Visualization

<img width="788" height="682" alt="image" src="https://github.com/user-attachments/assets/48012eac-9485-429e-9384-c5ecf8ee7c25" />


---

## Policies Saved
- policy_v1.pkl  
- policy_v2_explored.pkl  

---

## Observations
- High variance in early stages due to exploration  
- Rewards stabilize over time  
- Indicates convergence toward an optimal policy  

---

## MLOps Practices
- Version control using Git commits  
- Experiment tracking via CSV logs  
- Reproducibility using configuration files  

---

## Monitoring Plan (Real-world Deployment)

If deployed, the system would monitor:
- Average focus levels  
- Fatigue trends  
- Frequency of breaks  
- System stability to prevent burnout  

---

## Conclusion
This project demonstrates how reinforcement learning can model human productivity behavior by optimizing the balance between effort and recovery.

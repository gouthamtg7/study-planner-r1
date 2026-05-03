import numpy as np
import pickle
import csv
import yaml
import argparse
from sim.env import StudyEnv

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, default="configs/qlearning_v1.yaml")
args = parser.parse_args()

with open(args.config) as f:
    config = yaml.safe_load(f)

env = StudyEnv()

Q = {}

def get_q(state):
    if state not in Q:
        Q[state] = np.zeros(2)
    return Q[state]

rewards_per_episode = []

epsilon = config["epsilon"]

for episode in range(config["episodes"]):
    state = env.reset()
    total_reward = 0

    done = False
    while not done:
        if np.random.rand() < epsilon:
            action = np.random.choice([0, 1])
        else:
            action = np.argmax(get_q(state))

        next_state, reward, done = env.step(action)

        best_next = np.max(get_q(next_state))
        get_q(state)[action] += config["alpha"] * (
            reward + config["gamma"] * best_next - get_q(state)[action]
        )

        state = next_state
        total_reward += reward

    rewards_per_episode.append(total_reward)

    epsilon = max(config["epsilon_min"], epsilon * config["epsilon_decay"])

pickle.dump(Q, open("policy_v1.pkl", "wb"))

with open("experiments\\results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["episode", "reward"])
    for i, r in enumerate(rewards_per_episode):
        writer.writerow([i, r])

print("Training complete!")
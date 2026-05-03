import matplotlib.pyplot as plt
import csv

rewards = []

with open("experiments\\results.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        rewards.append(float(row[1]))

# smoothing
window = 10
smoothed = [sum(rewards[i:i+window])/window for i in range(len(rewards)-window)]

plt.plot(smoothed)
plt.xlabel("Episodes")
plt.ylabel("Reward")
plt.title("Smoothed Training Progress")
plt.show()
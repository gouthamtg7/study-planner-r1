import random

class StudyEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.focus = 80
        self.fatigue = 20
        self.time = 10
        return self.get_state()

    def get_state(self):
        return (self.focus // 10, self.fatigue // 10, self.time)

    def step(self, action):
        # action: 0 = study, 1 = break
        if action == 0:
            self.focus -= 5
            self.fatigue += 10
            reward = 10 - self.fatigue
        else:
            self.focus += 5
            self.fatigue -= 10
            reward = -2

        self.focus = max(0, min(100, self.focus))
        self.fatigue = max(0, min(100, self.fatigue))
        self.time -= 1

        done = self.time == 0
        return self.get_state(), reward, done
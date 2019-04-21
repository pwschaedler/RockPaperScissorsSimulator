#!/usr/bin/env python3
'''
Rock Paper Scissors Simulator between "Scissor-Hands" Stacy and Maya "The Rock"
'''

import random
import numpy as np
import matplotlib.pyplot as plt
import time
import math

class Player:
    def __init__(self, RPS_prob=(.339, .331, .331)):
        self.p_rock = RPS_prob[0]
        self.p_paper = RPS_prob[1]
        self.p_scissors = RPS_prob[2]
    
    def throw(self):
        rand_n = random.random()
        if rand_n < self.p_rock:
            return 0
        elif rand_n < self.p_rock + self.p_paper:
            return 1
        else:
            return 2

class Game:
    def __init__(self, P1, P2, win_score=2):
        self.P1 = P1
        self.P2 = P2
        self.p1_score = 0
        self.p2_score = 0
    
    def throws(self):
        p1_throw = self.P1.throw()
        p2_throw = self.P2.throw()

        if p1_throw == 0:
            if p2_throw == 1:
                return 1
            if p2_throw == 2:
                return 0
        if p1_throw == 1:
            if p2_throw == 2:
                return 1
            if p2_throw == 0:
                return 0
        if p1_throw == 2:
            if p2_throw == 0:
                return 1
            if p2_throw == 1:
                return 0
        return -1
    
    def check_win(self):
        if self.p1_score == 2:
            return 0
        elif self.p2_score == 2:
            return 1
        else:
            return -1
    
    def round(self):
        result = self.throws()
        if result == 0:
            self.p1_score += 1
        if result == 1:
            self.p2_score += 1

        win = self.check_win()
        if win != -1:
            return win
        return -1

start = time.perf_counter()
runs = 500
dim = 500
maya_win_probs = np.zeros((dim, dim))

counter = 0

for i, stacy_scissor_prob in enumerate(np.linspace(0, 1, dim, endpoint=False)):
    for j, maya_rock_prob in enumerate(np.linspace(0, 1, dim, endpoint=False)):

        log = []
        stacy_rest = (1 - stacy_scissor_prob) / 2
        maya_rest = (1 - maya_rock_prob) / 2
        stacy = Player((stacy_rest, stacy_rest, stacy_scissor_prob))
        maya = Player((maya_rock_prob, maya_rest, maya_rest))

        for k in range(runs):
            game = Game(stacy, maya)
            win = -1
            while win == -1:
                win = game.round()
            log.append(win)

        stacy_wins = 0
        maya_wins = 0

        for k in range(runs):
            if log[k] == 0:
                stacy_wins += 1
            else:
                maya_wins += 1

        maya_win_probs[i, j] = maya_wins / runs
        counter += 1

fig, ax = plt.subplots()
im = ax.imshow(maya_win_probs, cmap='plasma', extent=(0, 1, 0, 1), origin='lower')
plt.colorbar(im)
plt.title('Prob. of Maya Winning over {} Runs'.format(runs))
plt.xlabel('Prob. of Stacy Choosing Scissors')
plt.ylabel('Prob. of Maya Choosing Rock')

print('Time elapsed:', math.floor((time.perf_counter() - start)/60), 'm', (time.perf_counter() - start)%60, 's')
plt.show()

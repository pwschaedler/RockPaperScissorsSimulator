#!/usr/bin/env python3
'''
Rock Paper Scissors Simulator between "Scissor-Hands" Stacy and Maya "The Rock"
'''

# Imports
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import math

# Constants
RUNS = 500
DIM = 500

# Class & Function Definitions
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

    RULES = { # key beats value
        0: 2,
        1: 0,
        2: 1
    }

    def __init__(self, P1, P2, win_score=2):
        self.P1 = P1
        self.P2 = P2
        self.p1_score = 0
        self.p2_score = 0
        self.win_score = win_score
        self.winner = -1

    def beats(self, a, b):
        return self.RULES[a] == b
    
    def round(self):
        p1_throw = self.P1.throw()
        p2_throw = self.P2.throw()

        if self.beats(p1_throw, p2_throw):
            return 0
        elif self.beats(p2_throw, p1_throw):
            return 1
        else:
            return -1
    
    def check_win(self):
        if self.p1_score == self.win_score:
            return 0
        elif self.p2_score == self.win_score:
            return 1
        else:
            return -1
    
    def run_game(self):
        if self.winner != -1:
            raise Exception('Game already played')
        
        while self.check_win() == -1:
            round_winner = self.round()
            if round_winner == 0:
                self.p1_score += 1
            elif round_winner == 1:
                self.p2_score += 1

        self.winner = self.check_win()

start = time.perf_counter()
maya_win_probs = np.zeros((DIM, DIM))

for i, stacy_scissor_prob in enumerate(np.linspace(0, 1, DIM, endpoint=False)):
    for j, maya_rock_prob in enumerate(np.linspace(0, 1, DIM, endpoint=False)):

        log = np.zeros(RUNS)
        stacy_rest = (1 - stacy_scissor_prob) / 2
        maya_rest = (1 - maya_rock_prob) / 2
        stacy = Player((stacy_rest, stacy_rest, stacy_scissor_prob))
        maya = Player((maya_rock_prob, maya_rest, maya_rest))

        for k in range(RUNS):
            game = Game(stacy, maya)
            game.run_game()
            log[k] = game.winner

        maya_win_probs[i, j] = log.mean()

fig, ax = plt.subplots()
im = ax.imshow(maya_win_probs, cmap='plasma', extent=(0, 1, 0, 1), origin='lower')
plt.colorbar(im)
plt.title('Prob. of Maya Winning over {} RUNS'.format(RUNS))
plt.xlabel('Prob. of Stacy Choosing Scissors')
plt.ylabel('Prob. of Maya Choosing Rock')

print('Time elapsed:', math.floor((time.perf_counter() - start)/60), 'm', (time.perf_counter() - start)%60, 's')
plt.show()

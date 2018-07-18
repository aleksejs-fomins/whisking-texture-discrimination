import numpy as np
import random

'''
This is a naive time-continuous architecture of the decision making brain

Paradigm:
1) Real time input variable I(t) is always input into the system
2) Real time reward variable R(t) is always input into the system
3) The output of the system is a single binary value.
   It is sampled randomly from the distribution P(I, O), where I is the latest input  
4) If reward is observed, boost distribution P(I,O) and inhibit P(I,!O)
'''

class NaiveArchitecture1():
    def __init__(self, IStream, RStream, learningRate):
        self.ISt = IStream
        self.RSt = RStream
        self.LRate = learningRate
        self.P = np.array([0.5, 0.5])
        self.successRate = []
        self.trialcount = 0
        self.wincount = 0

    def step(self):
        Ithis = self.ISt.next()
        Othis = 0 if random.uniform(0,1) > self.P[Ithis] else 1
        Rthis = self.RSt.next(Ithis, Othis)

        if Rthis == 1:
            self.P[Ithis] = self.P[Ithis] * (1 - self.LRate) + Othis * self.LRate
            self.wincount += 1

            print('yolo', self.P)

        #print(Ithis, Othis, Rthis)

        self.trialcount += 1
        self.successRate.append(self.wincount / self.trialcount)

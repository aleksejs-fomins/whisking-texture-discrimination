import matplotlib.pyplot as plt
from architectures import naive1
from Modules import input1DBinaryRandom, reward1Dsomething

learningRate = 0.1

Inp = input1DBinaryRandom.Input1DBinaryRandom()
Rew = reward1Dsomething.reward1Dsomething()
Arch = naive1.NaiveArchitecture1(Inp, Rew, learningRate)

timeLength = 1000
timeAxis = list(range(timeLength))
for i in timeAxis:
    Arch.step()

plt.plot(timeAxis, Arch.successRate)
plt.show()
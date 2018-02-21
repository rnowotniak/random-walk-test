#!/usr/bin/python

import sys
from random import random

xmax = 100.
step = 10.
trials = 1000

Nexps = 1000
plus100 = 0
minus100 = 0

for _ in range(Nexps):
    x = 0
    while True:
        chg = step * random() - (step/2)
        x += chg
        if x >= xmax:
            plus100 += 1
            break
        if x <= -xmax:
            minus100 += 1
            break
    #print(x)

print('%.1f%% / %.1f%%' % (plus100 / (plus100+minus100)*100, minus100/(plus100+minus100)*100))


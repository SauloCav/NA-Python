#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def newton_interpolation(x, y, xi):

    n = len(x)

    fdd = [[None for x in range(n)] for x in range(n)]

    yint = [None for x in range(n)]

    ea = [None for x in range(n)]
 
    for i in range(n):
        fdd[i][0] = y[i]
    for j in range(1,n):
        for i in range(n-j):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i])

    fdd_table = pd.DataFrame(fdd)
    print(fdd_table)

    xterm = 1
    yint[0] = fdd[0][0]
    for order in range(1, n):
        xterm = xterm * (xi - x[order-1])
        yint2 = yint[order-1] + fdd[0][order]*xterm
        ea[order-1] = yint2 - yint[order-1]
        yint[order] = yint2

    return map(lambda yy, ee : [yy, ee], yint, ea)

x = [1, 2, 2.5, 3, 4]
y = [1, 5, 7, 8, 2]

a = newton_interpolation(x, y, 2)
df = pd.DataFrame(a, columns=['f(x)','error'])

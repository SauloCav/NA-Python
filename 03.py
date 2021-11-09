#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

x = 0.1
y = '0. '

for i in range (10):
    x = x * 2
    if int(x) == 0:
        y = y + '0'
    else:
        y = y + '1'
        x = x - 1
    print(y)

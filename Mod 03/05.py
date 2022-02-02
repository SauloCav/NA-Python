#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def f(x):
  return math.cos(x**2+1)

h = 0.004
s = 0

for i in range(365):
  s += f(h/2+i*h)

print(s*h)

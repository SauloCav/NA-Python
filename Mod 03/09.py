#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def f(x,y):
  return 1 + x*y + x**0.5

print(f(0.05, 1.05))

h = 0.1
x,y = 0,1

for i in range(12):
  k1 = f(x,y)
  k2 = f(x+h/2, y+k1*h/2)
  y = y + k2*h
  x = x + h
  print(x, y)

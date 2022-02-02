#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def f(t,y):
  return math.exp(t)/t**4

h = 0.1
t,y = 1,0

for i in range(90):
  k1 = f(t, y)
  k2 = f(t+h/2, y+k1*h/2)
  k3 = f(t+h/2, y+k2*h/2)
  k4 = f(t+h, y+k3*h)
  y += (k1+2*k2+2*k3+k4)*h/6
  t += h
  print(t, y)

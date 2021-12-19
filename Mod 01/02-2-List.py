#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def f(x):
  return x**3 -x -1

a = 1
b = 2
x = (a+b)/2
for i in range(20):
  if f(x)*f(a)<0:
    b = x
    x = (a+b)/2
  else:
    a = x
    x = (a+b)/2
  print(x, b-a)

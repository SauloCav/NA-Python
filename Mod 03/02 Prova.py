#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def f(x):
  return (e**x/x**3)

h = 0.00178
s = 7800

for i in range(10):
  s += f(h*(i+1))

print((f(0)+f(1))*(h/2)+s*h)

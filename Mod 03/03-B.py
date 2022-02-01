#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def f(x):
  return (x**2+1)**(1/3)

h = 0.2
s = 0

for i in range(4):
  s += f(h*(i+1))

print((f(0)+f(1))*(h/2)+s*h)

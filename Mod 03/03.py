#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def f(x):
  return (x**2+1)**(1/3)

h = 0.1
s = 0

for i in range(10):
  s += f(i*h)

print(h*s)

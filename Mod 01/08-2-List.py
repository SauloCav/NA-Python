#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def phi(x):
  return x - (math.log(x) + x)/(1+1/x)
def f(x):
  return x + math.log(x)

x = 1
while abs(f(x))>=10**-7:
   x = phi(x)
   print(x)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def g(x):
  return 4*math.sin(x)-math.exp(x)

a = 0
b = 1
x = (a*g(b)-b*g(a))/(g(b)-g(a))
while (g(x+10**-3)*g(x-10**-3)>= 0 or abs(g(x))>= 5*10**-2):
  if g(x)*g(a)<0:
    b = x
    x = (a*g(b)-b*g(a))/(g(b)-g(a))
  else:
    a = x
    x = (a*g(b)-b*g(a))/(g(b)-g(a))
  print(x)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
  return x**3 -x -1

def phi(x):
  return (x+1)**(1/3)

x = 1.5
while f(x+10**-4)*f(x-10**-4)>= 0:
   x = phi(x)
   print(x) 

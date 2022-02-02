#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def f1(x, y, z):
  return z

def f2(x, y, z): 
  return -x*y-z*x**2

h = 0.1
x,y,z = 0, 1, 0

for i in range(10):
  k1y = f1(x, y, z)
  k1z = f2(x, y, z)
  k2y = f1(x+h, y+k1y*h, z+k1z*h)
  k2z = f2(x+h, y+k1y*h, z+k1z*h)
  y = y + (k1y+k2y)*h/2
  z = z + (k1z+k2z)*h/2
  x = x + h
  print(x, y, z)

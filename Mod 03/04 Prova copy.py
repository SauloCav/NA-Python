#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def f1(x, y, z):
  return (x/z - y**2/2)

def f2(x, y, z): 
  return (z-x*y**2)

h = 0.005
x,y,z = 0, 1, 0

for i in range(365):
  k1y = f1(x, y, z)
  k1z = f2(x, y, z)
  k2y = f1(x+h, y+k1y*h, z+k1z*h)
  k2z = f2(x+h, y+k, z*h, z+k1z*h)
  y = y + (1/2)*(k1y+k2y)*h
  z = y + (1/2)*(k1z+k2z)*h
  print(x, y, z)

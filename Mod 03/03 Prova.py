#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math
def f(x):
    return math.exp(x)/x**3

def int(a,b):
    h = (b-a)/104
    x_par = a+h
    x_impar = a+2*h
    soma_par = 0
    soma_impar = 0
    for i in range(52):
        soma_par += f(x_par)
        x_par += 2*h
    for i in range(51):
        soma_impar += f(x_impar)
        x_impar += 2*h 
        
    return (f(a)+f(b) + 4 * soma_par + 2*soma_impar) *h/3 

print(int(1.9,9.7))

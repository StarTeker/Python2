# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:14:14 2020

@author: Batya
"""

n=int(input())
mas_fib = [0, 1]    
for i in range(2, n + 1):
    mas_fib.append(mas_fib[i-1] + mas_fib[i-2])
print(mas_fib)
mas=[int(j) for j in input().split()]
for i in range(n):
    for j in range(n):
        if mas[i]==mas_fib[j]:
            print(mas[i])
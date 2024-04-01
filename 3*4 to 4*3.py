#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:12:19 2021

@author: miderby
"""


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 方法一
for x in range(len(matrix)):
     print (matrix[x])
list1 = []
list2 = []
list3 = []
list4 = []
for x in range(len(matrix)):
   list1.append(matrix[x][0])

for z in range(len(matrix)):
   list2.append(matrix[z][1])

for v in range(len(matrix)):
   list3.append(matrix[v][2])

for w in range(len(matrix)):
   list4.append(matrix[w][3])

print("",list1,"\n",list2,"\n",list3,"\n",list4)
    
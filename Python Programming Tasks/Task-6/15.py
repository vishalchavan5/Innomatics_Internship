# -*- coding: utf-8 -*-
"""15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XitoFdFaotRhVff2Sju8ZItosqH1MS2O
"""

import numpy as np

np.set_printoptions(legacy='1.13')

n = int(input())
array = np.array([input().split() for _ in range(n)], float)
print(np.linalg.det(array))

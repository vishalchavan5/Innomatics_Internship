# -*- coding: utf-8 -*-
"""13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XitoFdFaotRhVff2Sju8ZItosqH1MS2O
"""

import numpy as np
A = np.array(input().split(), int)
B = np.array(input().split(), int)
print(np.inner(A,B), np.outer(A,B), sep='\n')


# -*- coding: utf-8 -*-
"""9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H6NnTBMip1fF6ugRVodskM3CQhljVM94
"""

N, M = map(int, input().split())
for i in range(1, N, 2):
    print((i * ".|.").center(M,"-"))
print("WELCOME".center(M, "-"))
for i in range(N-2, -1, -2):
    print((i * ".|.").center(M, "-"))


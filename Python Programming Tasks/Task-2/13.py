# -*- coding: utf-8 -*-
"""13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H6NnTBMip1fF6ugRVodskM3CQhljVM94
"""

_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

print(len(SET_N & SET_B))


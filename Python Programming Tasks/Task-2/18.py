# -*- coding: utf-8 -*-
"""18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H6NnTBMip1fF6ugRVodskM3CQhljVM94
"""

for i in range(int(input())):
    a = int(input())
    set_a = set(map(int, input().split()))

    b = int(input())
    set_b = set(map(int, input().split()))

    if len(set_a - set_b) == 0:
        print("True")
    else:
        print("False")


# -*- coding: utf-8 -*-
"""3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H6NnTBMip1fF6ugRVodskM3CQhljVM94
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

m = re.search(r'([a-zA-Z0-9])\1', input().strip())
print(m.group(1) if m else -1)

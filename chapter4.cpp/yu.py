#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    numberString = str(n)
    d = 0
    
    for ch in numberString:
        try:
            if n % int(ch) == 0:
                d += 1
        except:
            ZeroDivisionError()
            
    return d
if name == 'main':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

        fptr.close()
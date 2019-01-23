#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    count_valley = 0
    for step in s:
        sealevel_prev = sea_level
        if (step == 'D'):
            sea_level=sea_level-1
        if(step == 'U'):
            sea_level=sea_level+1
        if(sealevel_prev < 0) and (sea_level == 0):
            count_valley=count_valley+1
    return(count_valley)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

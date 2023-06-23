#!/bin/python3

import math
import os
import random
import re
import sys

def get_digit_sum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

def bestDivisor(n):
    best_divisor = 1
    best_digit_sum = 1
    
    for i in range(2, n+1):
        if n % i == 0:
            digit_sum = get_digit_sum(i)
            if digit_sum > best_digit_sum:
                best_divisor = i
                best_digit_sum = digit_sum
            elif digit_sum == best_digit_sum and i < best_divisor:
                best_divisor = i
    
    return best_divisor

if __name__ == '__main__':
    n = int(input().strip())

    result = bestDivisor(n)

    print(result)

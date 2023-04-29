# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:47:27 2021

@author: Ben
"""

import math

existing_primes = []

def is_prime(my_num, existing_primes):
    max_denominator = math.sqrt(my_num) #optimization 3: the maximum possible denominator is sqrt(candidate)
    for prime in existing_primes: #optimization 1: use dynamic programming to only consider prime numbers as denominators
        if prime > max_denominator:
            break
        if not my_num % prime:
            return False
    return True

def find_primes(report=0):
    test_prime = 3
    while(True):
        if is_prime(test_prime, existing_primes):
            existing_primes.append(test_prime)
            if report:
                position = len(existing_primes)
                ratio = test_prime/position
                print(f"prime number #{position}: {test_prime} (ratio: {ratio:.2f})")
        test_prime += 2 #optimzation 2: only consider odd numbers

if __name__ == "__main__":
    find_primes(1)

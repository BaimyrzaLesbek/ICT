def conv(gr):
    return 28.3495231 * gr

def conv2(f):
    return (5/9) * (f-32)

def solve(numheads, numlegs):
    krolik = (numlegs - 2 * numheads) // 2
    kuritca = numheads - krolik
    return (krolik, kuritca)

from itertools import count
import math

def filter_primes(l):
    d = []
    for i in l:
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            d.append(i)
    return d

def perm(s):
    bukvy = []
    bukvy.append(s[0])
    for i in range(1, len(s)):
        for j in reversed(range(len(bukvy))):
            curr = bukvy.pop(j)
            for k in range(len(curr) + 1):
                bukvy.append(curr[:k] + s[i] + curr[k:])
    print(bukvy, end='')

def rev(s):
    k = s.split()
    print(*k[::-1], end = " ")

def has(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def vol(rad):
    return 4 / 3 * math.pi * rad * rad * rad

def unq(nums):
    u = []
    for i in nums:
        if i not in u:
            u.append(i)
    return u

def checkPal(s):
    if s == s[::-1]:
        return True
    return False

def hist(l):
    for i in l:
        zvezdochki = ["*" for i in range(i)]
        print(*zvezdochki, sep="")

import random

def game():
    x = input("Hello! What is your name?: ")
    print("Well, KBTU, I am thinking of a number between 1 and 20.")
    r = random.randrange(1,20)
    u = 0
    cnt = 0
    while r != u:
        u = input("Take a guess!")
        if u > r:
            print("Your guess is too high.")
        if u < r:
            print("Your guess is too low.")
        cnt += 1
    print("Good job,", x + "! You guessed my number in", cnt, "guesses!")
    

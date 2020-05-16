#!/usr/bin/env python3
from sympy import *
import random

def op1(p, s):
    return sum([i * j for i, j in zip(s, p)]) % 256

def op2(m, k):
    return bytes([i ^ j for i, j in zip(m, k)])

def op3(m, p):
    return bytes([m[p[i]] for i in range(len(m))])

def deop3(m, p):
    count=0
    r=[]
    for j in range(len(m)):
        for i in range(len(m)):
            if(p[i]==count):
                r.append(i)
                count+=1
                break
    return bytes([m[i] for i in r])

def op4(m, s):
    return bytes([s[x] for x in m])
def deop4(m,s):
    count=0
    r=[]
    for j in range(len(m)):
        for i in range(len(s)):
            if(s[i]==m[count]):
                r.append(i)
                count+=1
                break
    return bytes(r)
'''
Linear Feedback Shift Register
'''
def stage0(m):
    random.seed('oalieno')
    p = [int(random.random() * 256) for i in range(16)]
    s = [int(random.random() * 256) for i in range(16)]
    c = b''
    for x in m:
        k = op1(p, s)
        c += bytes([x ^ k])
        s = s[1:] + [k]
    return c

'''
Substitution Permutation Network
'''
def stage1(m):
    random.seed('oalieno')
    k = [int(random.random() * 256) for i in range(16)]
    p = [i for i in range(16)]
    random.shuffle(p)
    s = [i for i in range(256)]
    random.shuffle(s)

    c = m
    for i in range(16):
        c = op2(c, k)
        c = op3(c, p)
        c = op4(c, s)
    return c
def destage0(m):
    random.seed('oalieno')
    p = [int(random.random() * 256) for i in range(16)]
    s = [int(random.random() * 256) for i in range(16)]
    c = b''
    for x in m:
        k = op1(p, s)
        #142,97,45,175,112,157,238,137,114,214,34,143,72,175,56,100
        c += bytes([x ^ k])
        s = s[1:] + [k]
    return c

'''
Substitution Permutation Network
'''
def destage1(m):
    random.seed('oalieno')
    k = [int(random.random() * 256) for i in range(16)]
    p = [i for i in range(16)]
    random.shuffle(p)
    s = [i for i in range(256)]
    random.shuffle(s)

    c = m
    for i in range(16): 
        c = deop4(c , s)
        c = deop3(c, p)        
        c = op2(c, k)

    return c

def decrypt(m, key):
    destage = [destage0, destage1]
    arr=[]
    for i in map(int, f'{key:08b}'):
        arr.append(i)
    for i in range(1,len(arr)+1):
        m = destage[arr[len(arr)-i]](m)

    return m

if __name__ == '__main__':
    flag = open('cipher', 'rb').read()
    assert(len(flag) == 16)
    for key in range(0,127):
        print(key,'  ',decrypt(flag,key))
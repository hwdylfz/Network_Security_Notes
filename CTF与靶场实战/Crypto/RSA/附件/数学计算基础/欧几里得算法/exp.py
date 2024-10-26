#!/usr/bin/python
#coding:utf-8

# 递归版
def gcd(a, b):
    return a if not b else gcd(b, a % b)

# 迭代版
def gcd2(a, b):
    while b:
        a, b = b, a % b
    return a

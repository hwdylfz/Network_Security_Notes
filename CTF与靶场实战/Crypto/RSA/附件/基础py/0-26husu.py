#!/usr/bin/python
#coding:utf-8
#@Author:醉清风
#求0-26内与26互素的数

def gcd(a,b):    #判断来两个数是否互素,辗转相除法
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def main():
    y = 26
    for  x in range(0,26):
        if gcd(x,y)==1:    #如果两个数的最大公约数是1，那么两数互素。
            print x,y
if __name__=="__main__":
    main()

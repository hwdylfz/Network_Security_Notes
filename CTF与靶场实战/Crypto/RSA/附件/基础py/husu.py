#!/usr/bin/python  
#coding:utf-8  
#@Author:醉清风  
  
def gcd(a,b):    #判断来两个数是否互素,辗转相除法  
    if(b==0):  
        return a  
    else:  
        return gcd(b,a%b)  
  
def main():  
    x = 17              #x,y的值根据需要修改即可  
    y = 65537  
    if gcd(x,y)==1:    #如果两个数的最大公约数是1，那么两数互素。  
        print str(x)+" "+str(y) + "两个数互素"  
    else:  
        print str(x)+" "+str(y) + "两个数不互素"  
if __name__=="__main__":  
    main()
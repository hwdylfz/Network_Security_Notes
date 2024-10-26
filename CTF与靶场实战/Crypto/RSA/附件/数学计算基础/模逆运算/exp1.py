#!/usr/bin/python 
#coding:utf-8
#47模30的逆为23

def egcd ( a , b ):
    if (b == 0):
        return 1, 0, a
    else:
        x , y , q = egcd( b , a % b ) # q = GCD(a, b) = GCD(b, a%b)
        x , y = y, ( x - (a // b) * y )
        return x, y, q
def mod_inv(a,b):
    #return egcd(a,b)[0]%b #求a模b得逆元
    print egcd(a,b)[0]%b
def main():
    a = 47
    b = 30
    mod_inv(a,b)
if __name__=="__main__":
    main()

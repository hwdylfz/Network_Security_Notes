# 递归版
def ext_euclid ( a , b ):
    # ref:https://zh.wikipedia.org/wiki/扩展欧几里得算法
    if (b == 0):
        return 1, 0, a
    else:
        x1 , y1 , q = ext_euclid( b , a % b ) # q = GCD(a, b) = GCD(b, a%b)
        x , y = y1, ( x1 - (a // b) * y1 )
        return x, y, q
# 迭代版
def egcd(a, b):
    # ref:https://blog.csdn.net/wyf12138/article/details/60476773
    if b == 0:
        return (1, 0, a)
    x, y = 0, 1
    s1, s2 = 1, 0
    r, q = a % b, a / b
    while r:
        m, n = x, y
        x = s1 - x * q
        y = s2 - y * q
        s1, s2 = m, n
        a, b = b, r
        r, q = a % b, a / b
    return (x, y, b)

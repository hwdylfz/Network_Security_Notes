#推荐 这个函数实现了:一个互质与不互质两种情况下都能工作良好的中国剩余定理（解同余方程组）的Python程序。
def GCRT(mi, ai):
    # mi,ai分别表示模数和取模后的值,都为列表结构
    assert (isinstance(mi, list) and isinstance(ai, list))
    curm, cura = mi[0], ai[0]
    for (m, a) in zip(mi[1:], ai[1:]):
        d = gmpy2.gcd(curm, m)
        c = a - cura
        assert (c % d == 0) #不成立则不存在解
        K = c / d * gmpy2.invert(curm / d, m / d)
        cura += curm * K
        curm = curm * m / d
        cura %= curm
    return (cura % curm, curm) #(解,最小公倍数)

调用
CRT(n,c)
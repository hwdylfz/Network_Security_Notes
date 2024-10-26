
import gmpy2
import libnum


def continuedFra(x, y):
    """计算连分数
    :param x: 分子
    :param y: 分母
    :return: 连分数列表
    """
    cf = []
    while y:
        cf.append(x // y)
        x, y = y, x % y
    return cf


def gradualFra(cf):
    """计算传入列表最后的渐进分数
    :param cf: 连分数列表
    :return: 该列表最后的渐近分数
    """
    numerator = 0
    denominator = 1
    for x in cf[::-1]:
        # 这里的渐进分数分子分母要分开
        numerator, denominator = denominator, x * denominator + numerator
    return numerator, denominator


def solve_pq(a, b, c):
    """使用韦达定理解出pq，x^2−(p+q)∗x+pq=0
    :param a:x^2的系数
    :param b:x的系数
    :param c:pq
    :return:p，q
    """
    par = gmpy2.isqrt(b * b - 4 * a * c)
    return (-b + par) // (2 * a), (-b - par) // (2 * a)


def getGradualFra(cf):
    """计算列表所有的渐近分数
    :param cf: 连分数列表
    :return: 该列表所有的渐近分数
    """
    gf = []
    for i in range(1, len(cf) + 1):
        gf.append(gradualFra(cf[:i]))
    return gf


def wienerAttack(e, n):
    """
    :param e:
    :param n:
    :return: 私钥d
    """
    cf = continuedFra(e, n)
    gf = getGradualFra(cf)
    for d, k in gf:
        if k == 0: continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        p, q = solve_pq(1, n - phi + 1, n)
        if p * q == n:
            return d


n = 113881698992379349039968368927979997900777221951663104697020683691495129639829918739755194174063944178083527489820939138302751895652076620380510013941997706327553964127612610209509889011613768847759318892303231846117914554931459295347697888260576901354448014917692680573408654658384481284699735788978230690197
e = 39068960413447607023613035707248214114819409621234801785480423979473767995171860917209502861408393208940683687475760366491413173744775811644295874981290403938714121977201901942939425294427737703229098649131737380098596135730392902019429964095866394165971291108245774407908011073271822915371753470010435225545
c = 32897925577913728659288168937025744709859960639901500169867896018406263110205704273203287172003057450591000201857719871686024077615520906540631374442504017489026298422189715372129838501090730593164075113452055617571409044743698645392909829425374093273187125709095368164744188182156849031225036001381531504057

d = wienerAttack(e, n)
m = pow(c, d, n)
print(libnum.n2s(m))
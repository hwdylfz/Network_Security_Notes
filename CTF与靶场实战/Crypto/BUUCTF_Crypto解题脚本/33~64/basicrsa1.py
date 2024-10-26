import random
from binascii import a2b_hex,b2a_hex
p = 262248800182277040650192055439906580479
q = 262854994239322828547925595487519915551
n = p * q
def multiplicative_inversr(a,b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa
    return lx
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
def generate_keypair(p,q):
    n = p * q
    phi = (p - 1) * (q -1)
    e = 65533
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inversr(e, phi)
    return ((e,n),(d,n))
def encrypt(pk, plaintext):
    key, n = pk[0]
    print(b2a_hex(plaintext.encode()))
    cipher = pow(int(b2a_hex(plaintext.encode()),16), key , n)
    return cipher
def decrypt(pk, cipher):
    key, n = pk[1]
    cipher = pow(cipher, key ,n)
    cipher = a2b_hex(hex(cipher).split('0x')[1])
    return cipher
pk = generate_keypair(p,q)
cipher = 27565231154623519221597938803435789010285480123476977081867877272451638645710
plaintext = decrypt(pk, cipher)
print(plaintext)
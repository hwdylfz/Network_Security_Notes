import gmpy2
p=473398607161
q=4511491
e=17
phi=(p-1)*(q-1)
print(gmpy2.invert(e,phi))
import libnum
p = 473398607161
q = 4511491
e = 17
fn = (p-1)*(q-1)
print(libnum.invmod(e,fn))
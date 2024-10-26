dh = '田口由中人工大土士王夫井羊壮'
ds = '00123455567899'

cip = '王壮 夫工 王中 王夫 由由井 井人 夫中 夫夫 井王 土土 夫由 土夫 井中 士夫 王工 王人 土由 由口夫'
s = ''
for i in cip:
	if i in dh:
		s += ds[dh.index(i)]
	else:
		s += ' '
print(s)

ll = s.split(" ")
t = ''
for i in range(0,len(ll)):
	t += chr(int(ll[i])+i+1)
print('t=', t, '\t\tt.lower()=', t.lower())
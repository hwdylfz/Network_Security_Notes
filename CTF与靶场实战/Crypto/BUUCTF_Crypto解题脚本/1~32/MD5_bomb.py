#爆破脚本MD5_bomb.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python
import hashlib

#print hashlib.md5(s).hexdigest().upper()
k = 'TASC?O3RJMV?WDJKX?ZM'                    #要还原的明文
for i in range(26):
	temp1 = k.replace('?',str(chr(65+i)),1)
	for j in range(26):
		temp2 = temp1.replace('?',chr(65+j),1)
		for n in range(26):
			temp3 = temp2.replace('?',chr(65+n),1)
			s = hashlib.md5(temp3.encode('utf8')).hexdigest().upper()#注意大小写
			if s[:4] == 'E903':    #检查元素
				print (s)       #输出密文
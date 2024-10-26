from PIL import Image
from zlib import *

file=open('D:\\mytools\\MyNote\CTF\\misc\\Misc脚本\\0573\\qr.txt','r').read().split('\n')
#print(file)
i=0
pic=Image.new("RGB",(200,200))
for y in range(200):
    for x in range(200):
        if file[i]=='(0, 0, 0)':
            color=(0,0,0)
            pic.putpixel([x,y],color)
        else:
            color=(255,255,255)
            pic.putpixel([x,y],color)
        i=i+1
pic.show()
with open('result.txt', 'r') as res:  # 坐标格式文件比如(7,7)
    re = res.read()
    res.close()
# 写文件,将转换后的坐标写入gnuplotTxt.txt
with open('gnuplot.txt','w') as rw:
    re = re.split()
    for i in range(0,len(re)):
        tem = re[i]
        # tem = tem.lstrip('(').rstrip(')')
        tem = tem.strip('()')# 去除左右()
        tem = tem.replace(',',' ')#替换逗号成空格
        rw.write(tem + '\n')
        print(tem)
import re

file = open('D:/edge/read/11.txt')    
line = file.readlines()
file.seek(0,0)
file.close()

result = {}
for i in range(97,123):
    count = 0
    for j in line:
        find_line = re.findall(chr(i),j)
        count += len(find_line)
    result[chr(i)] = count
res = sorted(result.items(),key=lambda item:item[1],reverse=True)

num = 1
for x in res:
        print('频数第{0}: '.format(num),x)
        num += 1
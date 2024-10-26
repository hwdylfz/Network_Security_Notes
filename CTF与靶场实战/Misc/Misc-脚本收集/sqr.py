import math
list1 = []
flag = ''
list=[ 10404, 11664, 9409, 10609, 15129, 13456, 3025, 5476, 6724, 6084, 14884, 7744, 9604, 14884, 5041, 2809, 6400, 2500, 12996, 7056, 6561, 7396, 5929, 5476, 7569, 5625, 2704, 9409, 5041, 10000, 3249, 6561, 7225, 7056, 12996, 2401, 4356, 6724, 6889, 9409, 11025, 10201, 7744, 6889, 4624, 15625 ]
for i in range(len(list)):
     # print(list[i])
     print(int(math.sqrt(list[i])))
     list[i]=int(math.sqrt(list[i]))
     print(chr(list[i]))
     flag=flag+chr(list[i])

print(flag)
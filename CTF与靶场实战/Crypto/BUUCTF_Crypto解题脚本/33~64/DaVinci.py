def fib_loop_for(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
key="1 233 3 2584 1346269 144 5 196418 21 1597 610 377 10946 89 514229 987 8 55 6765 2178309 121393 317811 46368 4181 1 832040 2 28657 75025 34 13 17711".split(" ")
dic=[]
c="36968853882116725547342176952286"
m=" "*32#new method!
m=list(m)#new method!
for i in range(1,33):
    print(fib_loop_for(i),end=" ")
    dic.append(fib_loop_for(i))#new method!
print(dic)
print("Sign!")
for i in range(32):
    index = dic.index(int(key[i]))#new method!
    print(i,index,c[i])
    m[index]=c[i]
print(m)
#7*995588256861228614165223347687
#flag:37995588256861228614165223347687
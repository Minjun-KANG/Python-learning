x= list(range(5))
#0,1,2,3,4
#range(start, stop, increment)

y = list(range(1,10,2))
#1,3,5,7,9

z = list(range(5,5))
#[]

p = list(range(5,0,-1))
#5,4,3,2,1

for i in range(5):
    print(i)

for i in range(4,-1,-1):
    print(i)

#range는 stop값 바로 직전까지 출력할 수 있음.

top = ["a",'b','c','d']

for i in range(0, len(top), 2):
    print(i, top[i])

    



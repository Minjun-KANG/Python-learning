w = ['a','bee','sea'] + ["solo","due","trio"]
print(w)

#이렇게 더하는 연산이 가능하다.

dir(w) #많이 나오는데
type(w.sort)
#sort가 기본적으로 제공되는 메소드라고 알려주고

w.sort()
#이렇게 하면 w에 값이 abc순으로 정리된다.
print(w)

w.append("quarter")
#list 맨마지막에 대입.
print(w)

len(w)
#기본적으로 제공되는 메소드이고, 리스트의 멤버가 몇개나 있나를 출력해준다.


z=[]
#빈 list 생성 len(z) 하면 0나옴

"""
>>>z.append(["second","third"])
>>> z
['first', ['second', 'third']]

>>> z.extend(["hello","it's me"])
>>> z
['first', ['second', 'third'], 'hello', "it's me"]

"""
#append랑 extend에 list를 넘겼다고 해보자

#append같은경우 값을 하나 가져다가 붙이는거라 2차원 배열형태로 들어가고
#extend는 1차원배열에 확장이 된다.

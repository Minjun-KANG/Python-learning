t = 1,'two',2+1

print(type(t))


# t[0]=2 tuple은 값을 바꿀 수 없음

z = ("one",
     "two",
     3)
#이렇게 여러줄 도 가

t = list(t)
#type tuple이던 t는 list로 바뀐다.
#그래서 값을 바꿀 수 있다.
print(type(t))

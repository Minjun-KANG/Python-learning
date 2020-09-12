x = [1, "two", 6/2]
print(x)
# 이건뭐 걍 별거없고 출력하라 정도가 들어가는거고
#정수, 문자열, 연산식이 들어가도 다 계산해서 값이 들어간다는 정도

def f(n):
    return [n, 2 * n, 3 *n, 4*n]
#함수 정의하고,

f(2)

y=f(49)
type(y) #list로 나오고

print(y)
f("yo") #Operator Overloading 해서 문자열도 계산하고.

a= 300
b= 200
x= [a,b,a+b,a-b]
print(x)

a=1
b=2
#이렇게 중간에 a,b 값이 바뀌더라도 list안에 값은 바뀌지 않는다.
print(x)

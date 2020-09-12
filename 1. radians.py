degrees = 150 #degrees변수를 선언하고, 값을 대입. degrees는 int 타입변수다.
radians = degrees * 3.14 /180
"""
radians 변수를 선언하고, degrees * 3.14 / 180 의 값을 대입해준다.
degrees 변수는 int 타입인데, 자동형변환이 일어나, degrees는 float 타입으로 된다.
그 증거로 print(type(radians))를 해보면 float가 나오고, print(type(radians))라는
명령을 치면 <class 'int'> 라는 값을 출력하는 것을 확인 할 수 있다.
"""
print("Degrees: ",degrees) #,후 값을적으면 자동으로 한칸 띈다.
print("Radians: ",radians)



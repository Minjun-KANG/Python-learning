#class 1

class Patient : #객체 선언
    name = "Jane Doe"
    age = 0
    malady = "healthy"

# struct patient sally 뭐 이런식으로 변수만드는 거를 이렇게 함
sally = Patient() 

sally.name  #사용자편의성 단순출력

sally.name = "Sally Smith"  # . 이라는 멤버연산자를 사용해서 변수접근
sally.age = 21
sally.malady = "bruised ego"

print(sally.name, sally.age, sally.malady, sep="; ")

def show(patient) : # 잘보면 이름이다르다. 함수를 멤버로 추가함.
    print(patient.name, patient.age, patient.malady, sep="; ")

show(sally) # 이때 sally를 patient라는 새로운 변수에 넘긴다.

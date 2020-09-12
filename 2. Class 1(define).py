class Patient :
    name = "Jane Doe"
    age = 0
    malady = "healthy"
    #Patient라는 클래스를 만든다,
    #이 클래스는, str변수 2개와 age변수 1개를 포함한다.

sally = Patient() #Patient라는 클래스 "틀"로 sally 라는 객체를 찍어낸다.

Sally = Patient #Patient라는 클래스를 Sally에게 링크건다. 

sally.name

sally.name = "Sally Smith"
sally.age = 21
sally.malady = "bruosed ego"

print(sally.name, sally.age, sally.malady, sep="; ")

def show(patient):
    print(patient.name, patient.age, patient.malady, sep="; ")

show(Patient) #하면 Sally와 같은 값이 나오고,

show(sally) #이걸하면 아까 대입한 값이 나오고

show(Sally) #이걸하면 Patient의 값이 직접나온다


class Patient:
    def __init__(self, name, age, malady):
        self.name = name
        self.age = age
        self.malady = malady

    def display(self):
        print("Name = ", self.name)
        print("Age = ",self.age)
        print("Malady = ",self.malady)

    def cure(self):
        self.malady = "healthy"


sally = Patient("Sally Smith", 21, "bruised ego")
sally.display()

sally.cure()
sally.display()

"""
__init은 method로 
sally = Patient("Sally Smith", 21, "bruised ego")
sally를 만듬과 동시에, 값을 대입할 수 있게 해준다.

이때 __init__ 메소드의 형식을 보면
인자로 self, name, age, malady를 받게 되고,
self.name = name과 같은 형식을 가지고있는데

name, age, malady는 입력받음과 동시에, 지역변수이기 때문에
self.name이라는 값에 대입된다. 

"""

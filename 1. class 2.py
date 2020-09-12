#class 2

class Patient :
    name = "Jane Doe"
    age = 0
    malady = "healthy"

    def display(self) :
        print("NAME   = ", self.name)
        print("Age    = ", self.age)
        print("Malady = ", self.malady)


sally = Patient()
sally.name = "Samuel Sneed"
sally.age = 18
sally.malady = "brokent heart"
sally.display()

print(sally.name, sally.age, sally.malady, sep="; ")

def show(patient) : 
    print(patient.name, patient.age, patient.malady, sep="; ")


show(sally)

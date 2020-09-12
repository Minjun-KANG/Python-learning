class Patient : #클래스 생성
    name = "Jane Doe"
    age = 0
    malady = "healthy"

    def display(self): 
        print("Name =", self.name)
        print("Age =",self.age)
        print("Malady =",self.malady)
#self란 무엇인가... 클래스 본인자체를 얘기한다.
#본인자체를 얘기함과 동시에 samuel=Patient()라고 객체를 만들었을 경우에만
#self라는 인스턴스 변수에 samuel을 가져다 쓸 수 있다.

samuel = Patient() #Patient() class를가지는 samuel이라는 객체생성
samuel.name = "Samuel Sneed"
samuel.age = 18
samuel.malady = "Broken heart"
samuel.display()

"""
이때 samuel은 Patient에 Instance이고, samuel은 객체이다.
Patient class안에 들어가서 보면 display는 method라고 칭하고,
self는 method안에 인자를 받을 때, self를 넣는데 이걸 인스턴스 변수라고 한다.
"""

#dir(samuel) samuel이라는 객체안에 있는 파일들을 보여준다.

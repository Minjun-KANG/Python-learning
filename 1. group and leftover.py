class1 = 32 #문제 요구조건 대로 class1에 32명의 학생을 대입
class2 = 45 #문제 요구조건 대로 class2에 45명의 학생을 대입
class3 = 51 #문제 요구조건 대로 class3에 51명의 학생을 대입
class_group1, class_leftover1 = divmod(class1,5)
class_group2, class_leftover2 = divmod(class2,7)
class_group3, class_leftover3 = divmod(class3,6)
"""
divmod 함수의 사용법은 class_group1, class_leftover = divmod(class1,5) 라고 하면,
class1//5 의 값을 class_group1 에 대입하고,
class1%5 의 값을 class_leftover1 에 대입한다.
class1//5 란 무엇이냐면 몫을 구하는 나누기 방법이다.
print(class1/5) 이 코드는 6.4를 출력하고
print(class1//5) 이 코드는 6을 출력하여 몫만 구하는 연산자이다.
"""
print("Number of students in eacg group:")  #출력을 담당한다.
print("Class 1: ",class_group1) 
print("Class 2: ",class_group2)
print("Class 3: ",class_group3)
print("Number of students leftover:")
print("Class 1: ",class_leftover1)
print("Class 2: ",class_leftover2)
print("Class 3: ",class_leftover3)

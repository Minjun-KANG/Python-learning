"""
문제에서 제시한 코드
pi = '3.14'
#string으로 되어 연산불가
pie.diameter = 55.4
#변수이름에 특수문자 사용불가
pie_radius = pie.diameter // 2
#변수이름에 특수문자 사용불가
circumference = 2 * pi ** pie_radius
#pi가 string이여서 연산불가
circumference-msg = 'Jimmy's pie has a circumference: '
#Jimmy's 에서 '를 사용하려면 "" 쌍따옴표 필요, 변수이름에 특수문자 사용불가
print(circumference-msg, circumference)
#변수이름에 특수문자 사용불가
"""
pi = 3.14
#string으로 되어 연산불가 -> 쌍따옴표 없애줌
pie_diameter = 55.4
#변수이름에 특수문자 사용불가 -> .을 _언더바로 교체
pie_radius = pie_diameter / 2
#변수이름에 특수문자 사용불가 -> 언더바로 교체해서 가능
#//2 로 되어있는 몫만 넘기는 연산식을 /2 로바꿔 소숫점까지 넘김
circumference = 2 * pi * pie_radius
#pi가 string이여서 연산불가 -> pi를 float로 바꿔서 가능
# ** pie_radius 로 된 제곱을 * 곱하기로 바꿔 수식을 완성
circumference_msg = "Jimmy's pie has a circumference: "
#Jimmy's 에서 '를 사용하려면 "" 쌍따옴표 필요, 변수이름에 특수문자 사용불가
#-> 쌍따옴표로 string을 넣어줌, 변수 특수문자 언더바로 교체
print(circumference_msg, circumference)
#변수이름에 특수문자 사용불가 -> 언더바로 교체해서 가능

'''
파일명 : 00_condition/02_논리실습문제.py

손님에게 출생년도를 4자리로 입력받아서 이 손님이 성인인지 판정하여
True 또는 False로 출력하는 프로그램을 구현하세요
(단, 한국에서 성인은 만나이가 아닌 한국 나이로 20세 이상을 의미합니다)
'''

Adult=2026
birth_year=2007
age=20

age=Adult-birth_year
customer=Adult>=birth_year
print(customer)

#강사님 풀이
#1. 출생년도 입력
#2. 한국 나이 계산(내가 살아온 연도 개수 -> A~B까지 범위의 숫자 개수 -> B-A+1)
#3. 성인 판정
#4. 결과 출력
#N년생 -> 2026-N+1


#나이는 계산했다고 치고 판정만
#입력1
birth=int(input('출생년도(4자리) :'))

#연산1
age=2026-birth+1
print(age)

#입력2(출력1)
age=20

#연산2
adult=age >=20

#출력2
print(adult)



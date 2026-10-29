#건강검진 판정
year = 2026
birth = int(input('출생년도를 입력하세요: '))
age = year - birth + 1

if birth % 2 == 0 and age >= 30:
    print(True)
else:
    print(False)

#윤년 판정
year=int(input('연도를 입력하세요 :'))
leap_year=year%400==0 or year%4==0 and year%100 !=0

print(leap_year)


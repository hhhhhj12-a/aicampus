"""
#고객 10명의 출생년도를 입력받아 연령대별로 카운트하는 프로그램을 만드세요
-연령대는 10대 이하, 20대, 30대, 40대 이상 이렇게 네 가지로 구분합니다
-음수나 '0' 등 현재 상태에 어울리지 않는 값은 입력되지 않는다고
가정하고 따로 처리하지 않습니다.
"""
"""birth=int(input('출생년도 :'))
count_10=0
count_20=0
count_30=0
count_40=0
age=2026-birth +1

for i in range(1, 10 + 1):
    birth = int(input('출생년도 :'))
    age = 2026 - birth + 1
    if age <= 19 :
     count_10+=1
    elif age>=20 and age <30 :
      count_20+=1
    elif age>= 30 and age <40 :
      count_30+=1
    elif age>= 40  :
      count_40+=1"""

#강사님 풀이
birth = int(input("출생년도(YYYY) : "))
age = 2026 - birth + 1
print(f"나이는 {age}세 입니다")

# 10대 이하, 20대, 30대, 40대를 구분하여 출력
if age <= 19:
    print("10대 이하")
elif age <= 29:
    print("20대")
elif age <= 39:
    print("30대")
else:
  print("40대 이상")




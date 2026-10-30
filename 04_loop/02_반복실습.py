"""다음 요구사항에 맞는 반복을 출력하세요

AI Campus를 5번 출력
1부터 100까지 정수를 출력
1부터 100까지 중에서 짝수만 출력
1부터 100까지 중에서 7로 끝나는 숫자만 출력
"""

for i in range(5):
    print('AI Campus')
print('-'*10)

#- 다소 느리지만 확장성이 좋다
for i in range(1,101):
    print(i)
print('-'*10)

for i in range(1,101):
    if i%2==0:
     print(i)
print('-'*10)

for i in range(1,101):
    if i%7==0:
     print(i)
print('-'*10)

#추가 문제
#for i in range(1,101):
#if i%10==5 or i%10==5 :
 #       print(i)

#강사님 풀이
find=5
for i in range(1,101):
    ten=i //10==find
    one=i %10==find
    if ten or one :
        print( i)






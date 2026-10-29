"""
사용자에게 배속(speed)을 입력받아 다음과 같이 판정하세요

배속이 1이면 기본 배속입니다 를 출력
배속이 1이 아닌 다른 값이면 배속을 변경했습니다 출력


speed = input('배속을 입력하세요 : ')

if speed == 1
"""
#강사님 풀이
#입력
speed = float(input('배속 입력 :'))

#연산



#출력
if speed == 1:
        print('기본 속도로 재생중입니다')
else :
    print('배속을 변경했습니다')

print('-' *20)

if speed == 1:
        print('기본 속도로 재생중입니다')
elif speed > 1 :
     print('빠른 속도로 재생중입니다')
else :
    print('느린 속도로 재생중입니다')

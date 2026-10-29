'''
PC방에서 고객의 이용시간에 따라 요금을 계산하는 프로그램을 만들고 있습니다.
1시간에 1,000원의 요금을 받고 있는데, 급한 출력 등으로 1시간 미만으로 이용하는 고객이 늘어나서
기본요금 제도를 도입하기로 했습니다.

고객의 시작, 종료시간과 분을 각각 입력받아서 1시간 미만으로 이용한 경우 True,
1시간 이상 이용한 경우 False로 판정하는
기본요금 판정기를 구현해보세요

크다(>), 작다(<), 이상(>=),
이하(<=), 같다(==), 다르다(!=)
'''

#시작시간
#종료시간
#시간차이

start_h=int(input('시작 시간 : ' ))
start_min=int(input('시작 분 : '))
end_h=int(input('종료 시간 : '))
end_min=int(input('종료 분 : '))

start_total=int(start_h*60+start_min) #시작 시간 분으로 변경
end_total=int(end_h*60+end_min) #끝나는 시간 분으로 변경

usage_time=int(end_total-start_total)
print('이용시간 :', usage_time)

base_fee=60>usage_time
print(base_fee)


# 강사님 풀이

#입력
#들어온시간h =9
#들어온시간m =20
#나간시간h =9
#들어온시간m =21

#연산
#나간시간=나간시간h*60+나간시간m
#들어온시간=들어온시간h*60들어온시간m
#time = 나간시간-들어온시간
#base=time<60

#print(base)





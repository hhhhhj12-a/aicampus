# 문제 : 할인 금액 계산
'''
온라인 쇼핑몰에서 80,000원짜리 운동화를 구매하려고 합니다.
현재 15% 할인 행사 중입니다.

요구사항: 할인 금액과 할인 적용 후 최종 결제 금액을 계산하세요.
'''
shoes=80000
sale=15/100
discount=shoes*sale
total=shoes-discount

print(sale)
print(total)


#강사님 풀이

#입력
origin=80000
rate=15

#연산
#discount=origin*rate//100
discount=int(origin*rate/100) #소수점 날리기(강제변환)
price=origin-discount

#출력
print('할인금액:',discount)
print('최종금액', price)

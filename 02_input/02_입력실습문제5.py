'''
독서실 이용 시간 계산하기
입실 시각과 퇴실 시각을 시와 분으로 각각 입력받아 총 이용 시간을 출력하세요.
(단, 퇴실은 입실과 같은 날에 이루어집니다)

예: 9시 20분 입실, 12시 10분 퇴실 → 170분(2시간 50분)

입실시각(시간) : (9)
입실시각(분) : (20)
퇴실시각(시간) : (12)
퇴실시각(분) : (10)

이용시간은 170분 입니다
이용시간은 2시간 50분 입니다

'''


in_hour=int(input('입실시각(시간) :'))
in_min=int(input('입실시각(분) :'))
out_hour=int(input('퇴실시각(시간) :'))
out_min=int(input('퇴실시각(분) :'))

in_total=int(in_hour*60+in_min)
out_total=int(out_hour*60+out_min)
use_time=out_total-in_total
total_hour=use_time//60
total_min=use_time%60

print('이용시간 :',use_time,'분',(total_hour, '시간', total_min ,'분'))
print(f'이용시간 : {total_hour}시간 {total_min}분')


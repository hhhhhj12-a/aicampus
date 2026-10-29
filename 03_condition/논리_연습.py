'''문제 1 — 주차장 이용시간
오후 1시 45분에 입차하여 오후 3시 10분에 출차했습니다.
두 시간을 24시간제로 변수에 저장하고, 전체 이용시간(분), 시간과 분으로 나눈 이용시간,
90분 미만 여부(True/False)를 출력하세요..

입차시간(시)
입차시간(분)
출차시간(시)
출차시간(분)'''

entry_hour=int(input('입차시간(시) : '))
entry_min=int(input('입차 시간(분) : '))
exit_hour=int(input('출차 시간(시) :'))
exit_minute=int(input('출차 시간(분) : '))

entry_total=entry_hour*60+entry_min
print(entry_total)

exit_total=exit_hour*60+exit_minute
hours=exit_total-entry_total
print(hours)



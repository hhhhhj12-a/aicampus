"""다섯명의 학생 점수를 입력받아 합격자와 불합격자의 수를 출력하세요
(합격의 기준은 60점 이상이며, 사람들은 0~100 사이의 숫자만 입력합니다)"""

'''score= int(input('점수 : '))
pass_count =0


for i in range(5):
    if score >= 60 :
        pass_count+ = 1
    fail_count+=1 
 else 60 < score :
   pass



for i in range(1,11):
    if i%2 ==0 :
       count +=1
       print(count)'''

#강사님 풀이
count_pass=0
count_fail=0

for i in range(5):
    score=int(input('점수 입력 :'))
    if score >= 60 :
        count_pass+=1
    else :
         count_fail += 1

    print(f'합격자 수 : {count_pass}')
    print(f'불합격자 수 : {count_fail}')

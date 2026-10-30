"""
1부터 99까지의 범위에서 다음 문제를 푸세요
1. '369' 게임에서 박수치는 숫자만 골라서 출력하세요
2. '369' 게임을 1부터 99까지 진행한 경과를 출력하세요

>369 게임은 3,6,9가 들어간 숫자에서 박수를 칩니다
>33 36 93 과 같이 두 번 들어간 경우 박수를 두 번 칩니다
>지금 문제는 세자리 숫자는 나오지 않도록 제한되어있으므로
두 자리를 기준으로 계산해보세요

#강사님 풀이
find=5
for i in range(1,101):
    ten=i //10==find
    one=i %10==find
    if ten or one :
        print( i)


"""

for i in range(1,100):
    ten =i //10
    one=i %10
    if ten in(3,6,9) or one in (3,6,9) :
        print( i)


#강사님 풀이
for i in range(1,100):
    number=i
    ten369= number//10 ==3 or number//10 ==6 or number//10 ==9
    one369= number%10 ==3 or number%10 ==6 or number%10 ==9

    double_clap=ten369 and one369
    clap=ten369 or one369

    if double_clap:
     print('짝짝')
    elif clap:
        print('짝')
    else:
        print(number)
"""
#실습문제 :  건강검진 대상자 판정

올해 국가 지정 건강검진 대상자 기준은 다음과 같습니다

-짝수년도 출생
-30세 이상

#내가한 풀이
birth=int(input('나이 : ', ))
age=2026-birth+1
print(age)

teen=1997>= age

print(teen)"""


#강사님 풀이
birth=1997
even=birth%2==0
#print('짝수년생인가요?', even)

age=2026-birth+1
over30=age>=30
#print('30세 이상인가요?',over30)

#judge = even ==True and over30== True
judge = even and over30
print('건강검진대상자 :', judge)



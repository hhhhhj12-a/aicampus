"""동전을 50번 던져서 앞면,
뒷면이 나온 횟수를 세고 앞면이 나올 확률을 계산해서 출력하고 싶습니다.

파이썬에서 동전을 만들어 던질 수는 없기 때문에 다음과 같이 약속합니다.
앞 = 0 , 뒤 = 1
"""

count=50
front= 0
back= 0
probability = count/2
percent=probability*100

import random
result=random.randint(0,1)

for i in range(count):
    result = random.randint(0, 1)
    if result==0 :
        front+=1
    else :
        back+=1

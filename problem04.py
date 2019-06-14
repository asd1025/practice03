# 문제 4
# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 도니다
# 프로글매은 정답 여부를 다시 출력
import random

i = random.randint(1,9)
j = random.randint(1,9)

print(i,' x ',j,' = ?')
s=set([])
answer=i*j
s.add(answer)
while len(s)<9 :
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    s.add(a*b)

for idx,i in enumerate(s) :
    print(i, end='\t\t')
    if (idx+1)%3==0 :
        print()
ans=input('answer: ')
if(int(ans)==answer) :
    print('정답')
else :
    print('오답')
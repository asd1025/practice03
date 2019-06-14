#문제1.
# 다음 세 개의 리스트가 있을 때,
# subs = ['I', 'You']
# verbs = ['Play', 'Love']
# objs = ['Hockey', 'Football']
#
# 3형식 문장을 모두 출력해 보세요. 반드시 comprehension을 사용합니다.

subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

result=[(a,b,c) for a in subs for b in verbs for c in objs]
result.append(('I',"Love",'You'))
for i in result :
    print(i[0],' ',i[1],' ',i[2])
#문제2.
# range() 함수와 유사한 frange() 함수를 작성해 보세요. frange() 함수는 실수 리스트를
# 반환합니다.

def frange(val, start=0.0, step=0.1):
    results=[]
    if start==0.0 :
        end=val
    else :
        end=start
        start=val
    while start < end :
        results.append(round(start,2))
        start+=step
    return results

print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))


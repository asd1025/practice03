# 문제5
# 선택정렬을 적용하는 코드
a= [5,9,3,8,60,20,1]
print('Before sort.\n',a)
for i in  range (0,len(a)) :
    for j in range (0,len(a)-(i+1)) :
        if(a[j+1]>a[j]) :
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
print('After sort.\n',a)

# 문제5
# 선택정렬을 적용하는 코드
a= [5,9,3,8,60,20,1]
print('Before sort.\n',a)
for i,before in enumerate(a) :
    for j,after in  enumerate(a):
        if(i<j and a[i]<a[j]) :
            temp = a[j]
            a[j]=a[i]
            a[i]=temp
print('After sort.\n',a)
 
import sys
a = [1,4,5,0,3,4,2]
for i in range(0,len(a)):
    if (a[i]>a[i+1]):
        temp = a[i]
        a[i] = a[i+1]
        
    else:
        a[i]=a[i+1]
print(a)            

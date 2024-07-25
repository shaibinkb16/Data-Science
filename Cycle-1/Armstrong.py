
a=int(input("Enter the number: "))
for i in range(1,a+1):
    leng=len(str(i))
    sum=0
    temp=i
    while temp > 0:
        rem=temp%10
        sum=sum+rem**leng;
        temp=temp//10
    if sum == i :
       print(i)
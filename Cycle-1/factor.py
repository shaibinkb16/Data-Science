def factors(n):
    sum = 0
    for i in range(1,n):
        if n % i==0:
            sum=sum + i
    return sum


n=int(input("Enter the number : "))
list = factors(n)

if list == n:
    print("The number is a perfect square")
else:
    print("The number is not perfect square")
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))

for x in range(a,b+1):
    is_prime=True
    for i in range(2,x):
        if x % i  == 0:
            is_prime=False
    if not is_prime:
        print(x)
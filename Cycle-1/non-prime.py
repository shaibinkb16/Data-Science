def is_Prime(num):
    if num<=1:
        return False
    if num==2:
        return  True
    if num % 2 == 0:
        return  False

    for i in range(3,num):
        if num % i == 0:
            return  False

    return True

def not_Prime(limit):
    for number in range(2,limit+1):
        if not is_Prime(number):
            print(number)


limitStr=input("Enter  the number : ")
if(limitStr.isdigit()):
    limit=int(limitStr)
    if limit >2:
        not_Prime(limit)
    else:
        print("Enter number greater than zero")
else:
    print("Invalid input")
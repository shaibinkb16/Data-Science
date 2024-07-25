def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        temp=a
        a=b
        b=temp+a
    return fib_list

N = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_numbers = fibonacci(N)
print(f"The first {N} Fibonacci numbers are:", fibonacci_numbers)


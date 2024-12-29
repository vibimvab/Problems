num = int(input())
fib1 = 0
fib2 = 1

for i in range(num):
    if i == num-1:
        print(fib1)
    temp = fib1+fib2
    fib1 = fib2
    fib2 = temp

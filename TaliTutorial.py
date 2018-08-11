import math

def fibonacci(num):
    n=0
    a=0
    b=1
    while n<num:
        temp=a
        a=b
        b+=temp
        n+=1
    return a

golden_ratio=fibonacci(100)/fibonacci(101)

def fibonacci_2(ratio,num):
    return math.floor(ratio*num)

print(fibonacci_2(golden_ratio,5))

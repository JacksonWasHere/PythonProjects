from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def test():
    for number_digits in range(10):
        for i in range(pow(10,number_digits),pow(10,number_digits+1)):
            checkNum(i)
def checkNum(num,digits):
    if isPrime(num):
        return

def expand(num,num_digits):
    digit_arr = []
    for i in range(num_digits):
        digit_arr.append(int(num%(pow(10,num_digits-i))/(pow(10,num_digits-i-1))))
    return digit_arr

def collapse(num_arr):
    num = 0
    for i in range(len(num_arr)):
        num += num_arr[i]*pow(10,2-i)
    return num
print("234")
print(expand(234,3))
print(collapse(expand(234,3)))

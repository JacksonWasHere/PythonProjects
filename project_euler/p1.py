def sumN(num):
    sum=0
    for val in range(num):
        sum+=val if (val%3==0 or val%5==0) else 0
    return sum
print(sumN(1000))

Phi=(1 + (5**(0.5)) )/2
phi=(1 - (5**(0.5)) )/2
def fibonacci(n):
    a=(pow(Phi,n)-pow(phi,n))/(5**(0.5))
    return int(a)
bin_thang=lambda x: format(x,'b')
for i in range(100):
    print(bin_thang(i))

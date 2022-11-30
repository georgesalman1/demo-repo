import math
def Sin_Taylor(x, n):
    res  = x
    m = 1
    i = 1
    while i<=n:
            m = m*((2*i))*((2*i)+1)
            power = pow(x,((2*i)+1)) / float(m)
            res = res + (pow((-1),(i)) * power)
            i = i+1
    return res



print(Sin_Taylor(2,11))           



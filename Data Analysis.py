def expo(num,pow):
    res = 1
    i = 1
    while i <= pow:
        res = res*num
        i+= 1
    return res

value = expo(4,5)
print(value)
print(4**5)
def GCD(a,b):
    if b==0:
        return a
    elif b==1:
        return -1
    return GCD(b,a%b)

print(GCD(2247,971))

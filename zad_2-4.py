import random
p = 0.3
d = 10
f = 0
def toss():
    pa = random.uniform(0,1)
    return pa
for i in range(100):
    print([d,f])
    a = toss()
    b = toss()
    if a < p and b < p:
        if d == 0:
            d += 1
            f -= 1
        elif f ==0:
            f += 1
            d -= 1
        else:
            continue
    elif a < p and b > p:
        if d == 0:
            continue
        else:
            d -= 1
            f += 1
    else:
        if f == 0:
            continue
        else:
            d += 1
            f -= 1
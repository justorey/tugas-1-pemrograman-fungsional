def triangular(x):
    temp=0
    for i in range(x):
        temp +=x
        x -= 1
    return temp
print(triangular(5))
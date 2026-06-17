def soma(*args):
    total = 0
    for i in args:
        total +=i
        print ("total:", i,total)
    return total


valor = soma(1,2,3,4,5,6,7,8,9,10,11,12)
print(valor)
    


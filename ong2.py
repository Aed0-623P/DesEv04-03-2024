def calcular(x, y ,z):
    x2 = fact_i(int(x))
    y2 = prod_i(y)
    z2 = fact_i(int(z))
    print(f"El factorial de {x} es {x2}")
    print(f"La productoria de {y} es {y2}")
    print(f"El factorial de {z} es {z2}")
    return

def fact_i(x):
    y2 = 1
    x = int(x)
    while x > 1:
        y2 *= x
        x -= 1
    return y2

def prod_i(x):
        y = 1
        for num in x:
            num = int(num)
            y *=(num)
        return y


#ingresar datos sin el "fact_1 = 5" solo dato

calcular(5,[3,6,4,2,8],6)



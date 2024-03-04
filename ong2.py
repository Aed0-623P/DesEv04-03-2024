def calcular(x, y ,z):
    x = fact_i(int(x))
    y = prod_i(y)
    z = fact_i(int(z))

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

x = 5
y = [3,6,4,2,8]
z = 6

resultado = calcular(x,y,z)

print(resultado)

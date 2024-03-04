fact_1 = float(input("Ingrese el valor para la primer factorial: "))
prod_1 = input("Ingrese el valor para la primera productoria ")
fact_2 = float(input("Ingrese el valor para la segunda factorial: "))

#calcular factorial
def fact_i(x):
    y = 1
    x = int(x)
    while x > 1:
        y *= x
        x -= 1
    return y

      #calcular productoria
def prod_i(x):
    y = 1
    for num in x:
        num = int(num)
        y *=(num)
    return y

def main():
    print(f"El factorial de {fact_1} es {fact_i(fact_1)}")
    print(f"La productoria de {prod_1} es {prod_i(prod_1)}")
    print(f"El factorial de {fact_2} es {fact_i(fact_2)}")


if __name__ == "__main__":
    main()

#def calcular(x, y ,z ):
 #   fact_i(x)
 #   prod_i(y)
 #   fact_i(z)
 #   return


#    print(calcular(fact_1 = 5 ,prod_i = 5 ,fact_2 = 6))
#    calcular(fact_1,prod_1,fact_2)
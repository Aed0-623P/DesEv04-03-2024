fact_1 = input("Ingrese el valor para la primer factorial: ")
prod_1 = input("Ingrese el valor para la primera productoria ")
fact_2 = input("Ingrese el valor para la segunda factorial: ")

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
    x * y
    y += 1
    return


#def calcular(x, y ,z ):  #cual es el punto de esto? es contraproducente
#    fact_i(x)
#    prod_i(y)
#    fact_i(z)
#    return



def main():
    #calcular (fact_1 = 5 ,prod_i = 5 ,fact_2 = 6)  What?  esto puede reemplazar el input al inicio, pero por qué? si pide input y forzarlo,
        #bueno, filo
    print(f"El factorial de {fact_1} es {fact_i(fact_1)}")
    print(f"La productoria de {prod_1} es {prod_i(prod_1)}")
    print(f"El factorial de {fact_2} es {fact_i(fact_2)}")

main 

if __name__ == "__main__":
    main()
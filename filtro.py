import sys

precios = {
    "Notebook": 700000,
    "Teclado": 25000,
    "Mouse": 12000,
    "Monitor": 250000,
    "Escritorio": 135000,
    "Tarjeta de Video": 1500000,
}


def filtrado(diccionario, umbral, v):
    if v == "menor":
        menores = ", ".join([k for k, v in diccionario.items() if v < umbral])
        return f"los productos menores al umbral son: {menores}"
    elif v == "mayor":
        mayores = ", ".join([k for k, v in diccionario.items() if v > umbral])
        return f"los productos mayores al umbral son: {mayores}"
    else:
        return "Lo sentimos, la operación no es válida"


resultado = filtrado(precios, int(sys.argv[1]), sys.argv[2])
print(resultado)

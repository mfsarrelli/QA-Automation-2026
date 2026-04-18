## DECLARACION DE FUNCIONES
def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def calculadora(opcion):
    if opcion == 1:
        resultado=sumar(a,b)
    elif opcion == 2:
        resultado=restar(a,b)
    elif opcion == 3:
        resultado=multiplicar(a,b)
    elif opcion == 4:
        resultado=dividir(a,b)
    return resultado

## MENU DE USUARIO
print("BIENVENIDO A LA CALCULADORA\n")
print("POR FAVOR ELIJA LA OPCION DESEADA:\n")
print("1-SUMAR")
print("2-RESTAR")
print("3-MULTIPLICAR")
print("4-DIVIDIR")

## REVISION DE VALORES INGRESADOS POR EL USUARIO
try:
    opcion=int(input())
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor: \n"))

    x=calculadora(opcion)

except ZeroDivisionError:
    print("ERROR!!! División por cero")
except ValueError:
    print("ERROR!! Entrada inválida, solo se permiten números enteros")
finally:
    print("Operación finalizada")

print(f"El resultado es: {x}")
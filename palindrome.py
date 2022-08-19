from ast import Str


def is_palindrome(palabra: str) -> bool:
    
    """Verifica si la palabra ingresada es palindromo
    y retorna True o False"""

    palabra = palabra.replace(" ","").lower()
    return palabra == palabra[::-1]

def is_prime(numero: int) -> bool:

    """Verifica si el numero ingresado a la funcion es primo o no
    y retorna True o False"""

    for i in range(1, numero):
        print(i)
        if i == 1:
            continue
        if numero % i == 0:
            return False
            break
        else:
            return True
            break


def run():
    opcion: int =  int(input("Qué desea hacer?\n1. Verificar palindromo.\n2. Verificar si un numero es primo.\n"))
    if opcion == 1:
        palabra: str = input("Digite la palabra que desea verificar: ")
        if is_palindrome(palabra):
            print(f"La palabra {palabra} es palindromo")
        else:
            print(f"La palabra {palabra} no es palindromo")

    elif opcion == 2:
        numero: int = int(input("Digite el numero que desea verificar: "))
        if is_prime(numero):
            print(f"El numero {numero} es primo")
        else:
            print(f"El numero {numero} no es primo")
    else:
        print("Ingrese la opción correcta...\n")
        run()

if __name__ == '__main__':
    run()
def divisor(num):
    try:
        if num < 0:
            raise ValueError("Ingresa un número positivo")
        else:
            divisor = []
            for i in range(1,num + 1):
                if num % i == 0:
                    divisor.append(i)
            return divisor
    except ValueError as ve:
        print(ve)
        return str(num) + " no es un número positivo"


def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisor(num))
        print("Termino el programa")
    except ValueError:
        print("Debes ingresar un número")




if __name__=="__main__":
    run()
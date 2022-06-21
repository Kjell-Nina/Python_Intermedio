def divisor(num):
    #  assert num >= 0, "Debes ingresar un número positivo"
    divisor = []
    for i in range(1,num + 1):
        if num % i == 0:
                divisor.append(i)
    return divisor


def run():
    num = input("Ingresa un numero: ") #se le quiz el int, para que solo sea un string
    assert num.isnumeric() > 0 ,"Ingresa un número entero positivo" #isnumeric verifica si es un numero o no
    #assert num.replace("-", "").isnumeric(), "Debes ingresar un número"
    print(divisor (int(num)))  #aquí le aumentamos el int, para covertir la variable a numero
    print("Termino el programa")



if __name__=="__main__":
    run()
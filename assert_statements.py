def run():
    palabra = input("Ingresa una palabra: ")
    cantidad=len(palabra)
    assert cantidad > 0, " Debes ingresar un número"
    print("Tu palabra tiene " + str(cantidad) + " letras")
 


if  __name__=="__main__":
    run()
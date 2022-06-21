# def run():
#     num=int(input("Escribe un número: "))
#     divisores=[x for x in range (1,num+1)if num%x==0]
#     print(divisores)
#     print(len(divisores))


# if __name__=="__main__":
#     run()



# def cantdivisores():
#     count=0
#     for i in divisores:
#         count+=1
            
# if __name__=="__main__":
#     cantdivisores()

# def sumatoriaN(numero):
#     sumatoria=sum([1+(1/n) for n in range (1,numero+1)])
#     return sumatoria
               
# def run():
#     numero= int(input("Escribe un número: "))
#     print(sumatoriaN(numero))

# if __name__=="__main__":
#     run()

# def chilinaso(nota):
#     if int(nota) >= 11:
#         print("Aprobaste")
#     elif int(nota) < 11:
#         print("No aprobaste, chilinaso con fuerza")
#     return int(nota)
    
# def run():
#     nota= input("Escribe un número: ")
#     assert nota.isnumeric() > 0 , "Ingresa un número valido"
#     assert nota.isnumeric() <=20, "No hay notas mayores a 20"
#     print(chilinaso(nota))
#     print("Nunca Pares de Aprender")

# if __name__=="__main__":
#     run()

def chilinaso(nota):
    try:
        if int(nota) > 20:
            raise ValueError("Ingresa una nota entre 0 y 20")
        if int(nota) >= 11:
            print("Aprobaste")
        elif int(nota) < 11:
            print("No aprobaste, chilinaso con fuerza")
        return int(nota)
    except ValueError as ve:
        print(ve)
        return nota + " no es un número válido"
    
def run():
    nota= input("Escribe un número: ")
    assert nota.isnumeric() > 0 , "Ingresa un número valido"
    print(chilinaso(nota))
    print("Nunca Pares de Aprender")

if __name__=="__main__":
    run()
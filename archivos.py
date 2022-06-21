def read():
    numbers = []
    with open("./archivos/numbers.txt","r",encoding="utf-8") as f: #el encodig es para cuando el archivo tiene "ñ"
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Nicolas", "Gregorio", "Marta", "Susana", "Jose","Rocío"]
    with open("./archivos/names.txt","a", encoding="utf-8") as f:    # el a, aumentara todo los nombres, el comando w lo sobreescribirá
        for name in names:
            f.write(name) #write sirve para escribir
            f.write("\n") #\n sirve para hacer un salto de línea




def run():
    write()


if __name__ == "__main__":
    run()
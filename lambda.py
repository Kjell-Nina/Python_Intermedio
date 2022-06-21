def run():
    # lamba argumentos : expresión
    # solo se puede dar una expresion en una linea de texto en python
    palimdromo = lambda string: string == string[::-1]
    print(palimdromo("ana"))
    # def palimdromo(string):
        #return string == string[::-1]
    #print(palimdromo("ana"))



if __name__ == "__main__":
    run()
try:
    numero_01 = int(input("Inserir um numero inteiro: "))
    numero_02 = int(input("Inserir um numero inteiro: "))
    resultado = numero_01//numero_01
    print(resultado)
except ZeroDivisionError:
    print("integer division or module by zero ")
except KeyboardInterrupt:
    print("parece que vc n quis inserir um numero")
except ValueError:
    print("tem que ser a porra de um numero caralho")
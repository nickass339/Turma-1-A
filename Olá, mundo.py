while True:
    print("qual calculadora vamos usar?")
    calculadora = int(input("[1] física [2] matemática\n")) 
    
    if calculadora == 1:
        newton = int(input("vamos calcular a força?\n[1]sim ou [2]nao"))
        if newton == 1:
    print("************************************")
    print("calculadora da Segunda lei de Newton")
    print("************************************")
    massa = int(input("qual é a massa do corpo?"))
    aceleracao = int(input("qual é a aceleração do corpo?"))
    print("\nA força em Newtons é equivalente a", massa * aceleracao, "Newtons\n")
    
    continua = int(input("vamos continuar?\n[1]sim [2]nao"))
    if continua == 1: 
        continue
    if continue == 2:
        break

def suma(a, b):
    return a + b

def diferenta(a, b):
    return a - b

def produs(a, b):
    return a * b

def impartire(a, b):
    return a / b

while True:
    operator_1 = input("Inserează primul operator: ")
    operator_2 = input("Inserează al doilea operator: ")
    operatie = input("Alege operația: ")

    rezultat = []

    if operatie in ["+", "-", "*", "/"] and operator_1.isdigit() and operator_2.isdigit():
        if int(operator_2) == 0 and operatie == "/":
            print("Împărțirea la 0 nu este permisă.")
            break
        if operatie == "+":
            print(f"Suma celor două numere {operator_1} + {operator_2} = {suma(int(operator_1), int(operator_2))}")
        elif operatie == "-":
            print(f"Diferența celor două numere {operator_1} - {operator_2} = {diferenta(int(operator_1), int(operator_2))}")
        elif operatie == "*":
            print(f"Produsul celor două numere {operator_1} * {operator_2} = {produs(int(operator_1), int(operator_2))}")
        else:
            print(f"Împărțirea celor două numere {operator_1} / {operator_2} = {impartire(int(operator_1), int(operator_2))}")
        break
    elif not (operator_1.isdigit() and operator_2.isdigit()):
        print(f"Calculatorul acceptă doar numere. ")
        break
    else:
        print(f"Alege una dintre aceste operații: {', '.join(['+', '-', '*', '/'])}")
        break

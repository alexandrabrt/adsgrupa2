def validare_nr(nr):
    numar=input(f"Nr {nr} este: ")
    while numar.isdigit() is False:
        numar = input(f"Nr {nr} este: ")
    return int(numar)

def validare_operand(operatie):
    while operatie not in "+-/*":
        operatie = input("Operatorul este: ")
    return operatie

def suma(operator1:int, operator2:int):
    return operator1 + operator2

def dif(operator1:int, operator2:int):
    return operator1 - operator2

def produs(operator1:int, operator2:int):
    return operator1 * operator2

def impartire(operator1:int, operator2:int):

    while operator2 == 0:
        operator2 = validare_nr(2)
    return operator1 / operator2

def principal():

    op1 = validare_nr(1)
    op2 = validare_nr(2)
    operand = input("Operatorul este: ")
    rezultat = validare_operand(operand)

    if rezultat == "+":
        a = suma(op1, op2)
    elif rezultat == "-":
        a = dif(op1, op2)
    elif rezultat == "*":
        a = produs(op1, op2)
    else:
        a = impartire(op1, op2)
    return a

print(principal())

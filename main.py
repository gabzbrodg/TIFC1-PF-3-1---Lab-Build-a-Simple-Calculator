#Tarea Inicial
number1 = int(input("Ingresa el numero: "))
number2 = int(input("Ingresa el numero: "))

result = number1 + number2
print(result) 

def calculadora_pro():
    op = input("Elige: (+, -, *, /, %, triple, mixta): ")
    
    if op == "triple":
        a = float(input("Num 1: ")); b = float(input("Num 2: ")); c = float(input("Num 3: "))
        print(f"Resultado: {a + b + c}")
    elif op == "mixta":
        expr = input("Escribe la operación (ej. 2 + 4 - 3): ")
        print(f"Resultado: {eval(expr)}") # eval procesa la cadena matemática
    else:
        n1 = float(input("Num 1: "))
        n2 = float(input("Num 2: "))
        if op == "-": print(n1 - n2)
        elif op == "*": print(n1 * n2)
        elif op == "/": print(n1 / n2) if n2 != 0 else print("Error: Div por 0")
        elif op == "%": print(n1 % n2)

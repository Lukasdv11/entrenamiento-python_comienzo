A = float(input("Ingrese un numero: "))
B = float(input("Ingrese otro numero: "))
operacion = input("Ingrese una operacion: ")

if operacion == "+":
    suma = A + B
    print(f"La suma es: {suma}.")
elif operacion == "-":
    resta = A - B
    print(f"La resta es: {resta}.")
elif operacion == "/":
    if B != 0:
        division = A / B
        print(f"La division es: {division}.")
    else: 
        print("Error: no se puede dividir por 0.")
    
elif operacion == "*":
    multiplicacion = A * B
    print(f"La multiplicacion es: {multiplicacion}.")
else:
    print("Ingrese una operacion correcta (+. -, *, /).")
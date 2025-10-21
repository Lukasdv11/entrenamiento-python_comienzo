nombre = input("Cual es tu nombre?: ")
edad = input("Cual es tu edad?: ")
print(f"Hola {nombre}, tienes {edad}.")


peso = float(input("Cual es tu peso en kilogramos?: "))
altura_usuario = float(input("Cual es tu altura en metros?: "))

IMC = peso/(altura_usuario)**2
print(f"Tu IMC es {IMC:.2f}.")


pesos_usuario = float(input("Ingrese cantidad en pesos a convertir: "))
valor_dolar = float(input("Ingrese el valor del dolar: "))
conversion = pesos_usuario / valor_dolar
print(f"{pesos_usuario} pesos Chilenos serian {conversion} Dolares.")


nota1 = float(input("Ingresa una nota: "))
nota2 = float(input("Ingresa una segunda nota: "))
nota3 = float(input("Ingresa una tercera nota: "))

promedio = (nota1 + nota2 + nota3)/3
print(f"Tu promedio es: {promedio}.")


base = float(input("Ingresa la base de un rectangulo: "))
altura = float(input("Ingresa la altura de un rectangulo: "))
area = base * altura
print(f"El area del rectangulo es: {area}.")








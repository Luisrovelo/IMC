# Función para calcular el IMC
def calcular_imc(masa, altura):
    return masa / (altura ** 2)

# Función para determinar la categoría del IMC
def determinar_categoria_imc(imc):
    if imc < 16:
        return "Delgadez severa"
    elif imc < 17:
        return "Delgadez moderada"
    elif imc < 18.5:
        return "Delgadez leve"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad leve"
    elif imc < 40:
        return "Obesidad media"
    else:
        return "Obesidad morbida"

# Función para determinar si la persona es menor o mayor de edad
def determinar_edad(edad):
    if edad < 18:
        return "Menor de edad"
    else:
        return "Mayor de edad"

# Función para obtener un valor válido del usuario
def obtener_valor(prompt):
    while True:
        valor = input(prompt)
        if valor == "":
            print("Debes ingresar un valor")
        else:
            return valor

# Función para obtener un valor numérico válido del usuario
def obtener_numero(prompt):
    while True:
        valor = input(prompt)
        try:
            numero = float(valor)
            if numero < 0:
                print("Debes ingresar un número positivo")
            else:
                return numero
        except ValueError:
            print("Debes ingresar un número")

# Pedimos la cantidad de personas
personas = int(obtener_numero("Ingrese la cantidad de personas: "))

# Verificamos que la cantidad sea mayor a 0
while personas > 0:
    # Pedimos los datos de la persona
    nombre = obtener_valor("Ingrese su nombre: ")
    edad = int(obtener_numero("Ingrese su edad en años: "))
    altura = obtener_numero("Ingrese su altura en metros: ")
    masa = obtener_numero("Ingrese su masa en kilogramos: ")

    # Calculamos el IMC
    imc = calcular_imc(masa, altura)

    # Imprimimos los resultados
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años ({determinar_edad(edad)})")
    print(f"Altura: {altura} metros")
    print(f"Masa: {masa} kilogramos")
    print(f"IMC: {imc:.2f} ({determinar_categoria_imc(imc)})")

    # Restamos 1 a la cantidad de personas
    personas -= 1
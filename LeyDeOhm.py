"""
 * Enunciado: Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará
 *   la cadena de texto "Invalid values".
"""

LeyDeOhm = {
    "V": lambda i, r: round(i * r, 2),
    "R": lambda v, i: round(v * i, 2),
    "I": lambda v, r: round(v/r, 2)
}

NombreVariables = {
    "V": "Voltaje",
    "R": "Resistencia",
    "I": "Intensidad"
}

def CalcularLeyDeOhm(V: float=None, R: int=None, I: float=None):
    assert (I and R or V and I or V and R), "Tiene que conocer al menos dos valores."

    
    if not V:
        return [NombreVariables["V"], LeyDeOhm["V"](I, R)]
    elif not R:
        return [NombreVariables["R"], LeyDeOhm["R"](V, I)]
    elif not I:
        return [NombreVariables["I"], LeyDeOhm["I"](V, R)]

print("\t\t||| Bienvenido a la calculadora de la ley de Ohm |||")
print("Podrá calcular a partir de dos valores conocidos el valor no conocido")
print("Ingrese los valores sin la unidad, solo el numero. Si no lo conoce ingrese 0.\n")

Voltaje = input("Ingrese el voltaje: ").strip()
Resistencia = input("Ingrese la resistencia: ").strip()
Intensidad = input("Ingrese la intensidad: ").strip()

try:
    Voltaje, Resistencia, Intensidad = int(Voltaje or 0), int(Resistencia or 0), int(Intensidad or 0)
except:
    print("Alguno de los valores ingresados no se reconoció como numero. Intentelo de nuevo")
else:
    valor_desconocido = CalcularLeyDeOhm(V=Voltaje, R=Resistencia, I=Intensidad)
    print(f"\nEl valor de {valor_desconocido[0]} es {valor_desconocido[1]}")

input("...")
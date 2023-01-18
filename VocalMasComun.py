from unicodedata import normalize

print("\t\t\t||| Bienvenido a Vocal Más Común |||\n")
print("> Este programa mostrará en pantalla la vocal que más veces aparezca en su texto\n")

texto_in = input("Escriba su texto:\n> ").lower()
texto_in = normalize("NFD", texto_in)

vocales = ["a", "e", "i", "o", "u"]
cantidad_vocales = [texto_in.count(vocal) for vocal in vocales]

vocales_mas = []

for vocal, cantidad in zip(vocales, cantidad_vocales):
    if cantidad == max(cantidad_vocales):
        vocales_mas.append(vocal)

match len(vocales_mas):
    case 1:
        print(f"\nLa vocal que aparece mayor cantidad de veces es: \"{vocales_mas[0]}\" ")
    case 0:
        print("\nNo hay vocales en su texto")
    case _:
        print(f"\nLas vocales que más aparecieron con la misma cantidad de veces en su texto son: ")
        for vocal in vocales_mas:
            print(f"> \"{vocal}\"")

optInfo = input("\n¿Le gustaría ver información de las veces que aparece cada vocal? (Y/N)\n> ").upper()
if optInfo == "Y":
    print("\n")
    for vocal, cantidad in zip(vocales, cantidad_vocales):
        print(f"[{vocal}] = {cantidad}")

    input("\n...")

"""
Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres.
"""
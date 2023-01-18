"""
 * Enunciado: Calcula dónde estará un robot (sus coordenadas finales) que se
 * encuentra en una cuadrícula representada por los ejes "x" e "y".
 * - El robot comienza en la coordenada (0, 0).
 * - Para idicarle que se mueva, le enviamos un array formado por enteros 
 *   (positivos o negativos) que indican la secuencia de pasos a dar.
 * - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene,
 *   luego 5, se detiene, y finalmente 2. 
 *   El resultado en este caso sería (x: -5, y: 12)
 * - Si el número de pasos es negativo, se desplazaría en sentido contrario al
 *   que está mirando.
 * - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando
 *   hacia la parte positiva del eje "y".
 * - El robot tiene un fallo en su programación: cada vez que finaliza una
 *   secuencia de pasos gira 90 grados en el sentido contrario a las agujas
 *   del reloj.
"""

from dataclasses import dataclass

@dataclass
class Robot:
    coords = [0,0]
    rotation = 90

    def rotate(self):
        match self.rotation:
            case 0:
                self.rotation = 90
            case 90:
                self.rotation = 180
            case 180:
                self.rotation = 270
            case 270:
                self.rotation = 0
    
    def move_array(self, units_array):
        for units in units_array:
            self.move(units)
                
    def move(self, units):
        match self.rotation:
            case 0:
                print(f"Moviendome {units} unidades en el eje X positivo")
                self.coords[0] += units
            case 90:
                print(f"Moviendome {units} unidades en el eje Y positivo")
                self.coords[1] += units
            case 180:
                print(f"Moviendome {units} unidades en el eje X negativo")
                self.coords[0] -= units
            case 270:
                print(f"Moviendome {units} unidades en el eje Y negativo")
                self.coords[1] -= units

        self.rotate()

print("\t\t||| Bienvenido a ¿Dónde está el robot? |||")
print("Este programa le permitirá mover un robot a partir de una secuencia de pasos que usted ingresa")
print("Pero este robot tiene una falla en su programación, cada que finaliza una secuencia de pasos")
print("Gira 90 grados en el sentido contrario a las agujas del reloj. El robot empieza en 90 grados.")

print("\n")
pasos_array = input("Ingrese los pasos a dar separados por espacio: \n> ").split()

for i, paso in enumerate(pasos_array):
    pasos_array[i] = float(paso)

print("\n")
myRobot = Robot()
myRobot.move_array(pasos_array)
print("\n")

print(f"Las coordenadas finales del robot son:\nX = {myRobot.coords[0]}\nY = {myRobot.coords[1]}")

input("...")
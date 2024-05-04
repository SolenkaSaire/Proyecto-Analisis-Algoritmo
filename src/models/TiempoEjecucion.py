from src.models.DocumentoMatrices import LeerMatriz, GeneradorMatrices
from src.models.NaivOnArray import NaivOnArray
from src.models.NaivLoopUnrollingTwo import NaivLoopUnrollingTwo
from src.models.NaivLoopUnrollingFour import NaivLoopUnrollingFour
from src.models.WinogradOriginal import WinogradOriginal
from src.models.WinogradScaled import WinogradScaled
from src.models.StrassenNaiv import StrassenNaive
from src.models.StrassenWinograd import StrassenWinograd
from src.models.III3SequentialBlock import III3SequantialBlock
from src.models.III4ParallelBlock import III4ParallelBlock
from src.models.IV3SequentialBlock import IV3SequentialBlock
from src.models.IV4ParallelBlock import IV4ParallelBlock
from src.models.V3SequentialBlock import V3SequentialBlock
from src.models.V4ParallelBlock import V4ParallelBlock


import os
import sys
import time
import numpy as np


class TiempoEjecucion:
    def __init__(self, size, time):
        self.size = size
        self.time = time

    def __str__(self):
        return f"Tamaño {self.size}: {self.time:.6f} ms"
    

class AlgoritmoMultiplicacion:
    @staticmethod
    def ejecutar_algoritmo(matrices_filenames, algorithm):
        registros_directory = "src/file_cases"
        if not os.path.exists(registros_directory):
            os.makedirs(registros_directory)

        lst_te_aux = []
        for filename in matrices_filenames:
            # Filename debe ser string
            filename = str(filename)

            # Obtener la matrizA de un archivo
            matrizA = LeerMatriz.load_matrix_from_file(filename)
            n = len(matrizA)

            # Obtener la matrizB de un archivo
            filename2 = filename.replace("num1", "num2")
            matrizB = LeerMatriz.load_matrix_from_file(filename2)
            # Matriz resultado
            matrizC = np.zeros((n, n), dtype=float)
            
            # Obtener el nombre del método a usar según el número del algoritmo
            nombre_clase = algorithm
            nombre_metodo = "multiply"  # Reemplazar con el nombre correcto según el número

            try:
                # Obtener la clase
                clase = getattr(sys.modules[__name__], nombre_clase)
                # Obtener el método dentro de la clase
                metodo = getattr(clase, nombre_metodo)

                tiempo_inicio = time.time()
                # Llamar al método para multiplicar las matrices
                metodo(matrizA, matrizB, matrizC, n, n, n)
                tiempo_final = time.time()

                # Calcular el tiempo de ejecución en milisegundos
                tiempo_ejecucion = (tiempo_final - tiempo_inicio) * 1000

                # Crear objeto TiempoEjecucion y añadirlo a la lista
                te = TiempoEjecucion(n, tiempo_ejecucion)
                lst_te_aux.append(te)

                print(f"Multiplicación {n}x{n} realizada: {te.time:.6f} milisegundos")

            except Exception as e:
                print(e)
            
            

        # Escribir los tiempos de ejecución en el archivo
        with open(os.path.join(registros_directory, "execution_times.txt"), 'a') as file:
            # Solo añadir encabezado si el archivo está vacío
            if file.tell() == 0:
                file.write("Matriz Size\tAlgorithm\tExecution Time (s)\n")
            for te in lst_te_aux:
                file.write(f"{te.size}\t{algorithm}\t{te.time:.6f}\n")



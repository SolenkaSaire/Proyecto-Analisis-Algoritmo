import sys
from src.models.WinogradScaled import WinogradScaled
from src.models.StrassenNaiv import StrassenNaive
from src.models.DocumentoMatrices import LeerMatriz, GeneradorMatrices
from src.models.ChartGenerator import ChartGenerator
from src.models.TiempoEjecucion import TiempoEjecucion, AlgoritmoMultiplicacion

import numpy as np 
import os
import time

def generar_matrices():
    sizes = [2**n for n in range(4, 12)]  # Tamaños de matrices de 16 hasta 2048
    directory = "src/files_matrices"

    # Generar y guardar la lista devuelta
    GeneradorMatrices.generate_matrices(directory, sizes)
    


def main():
    # Algoritmo a ejecutar
    algorithm = ["NaivOnArray", "NaivLoopUnrollingTwo", "NaivLoopUnrollingFour", "WinogradOriginal", "WinogradScaled"]
    #algorithm = "NaivLoopUnrollingTwo"
    #algorithm = "NaivLoopUnrollingFour"
    #algorithm = "WinogradOriginal"
    #algorithm = "WinogradScaled"
    #algorithm = "StrassenNaive"
    #algorithm = "StrassenWinograd"
    #algorithm = "III3SequantialBlock"
    #algorithm = "III4ParallelBlock"
    #algorithm = "IV3SequentialBlock"
    #algorithm = "IV4ParallelBlock"
    #algorithm = "V3SequentialBlock"
    #algorithm = "V4ParallelBlock"


    # Generar y guardar matrices
    #generar_matrices()

    # Leer nombres de archivos de matrices
    matrices_filenames = GeneradorMatrices.read_matrices_names("src/files_matrices")
    # Multiplicar las matrices y registrar el tiempo de ejecución

    for algoritmo in algorithm:
        AlgoritmoMultiplicacion.ejecutar_algoritmo(matrices_filenames, algoritmo)
        # Generar gráfico de barras con los tiempos de ejecución
        ChartGenerator.plot_execution_times(algoritmo)


    # Directorio de registros
    #registros_directory = "src/registros"

    # Obtener el tiempo de ejecución máximo de cada algoritmo
    max_times = ChartGenerator.get_max_execution_time()

    # Generar gráfico de barras con los tiempos de ejecución máximo
    ChartGenerator.plot_max_execution_times(max_times)

if __name__ == "__main__":
    main()






"""
def multiplicar_matrices(matrices_filenames):
<<<<<<< HEAD
    # Explicación de los parámetros:
    # - matrizA: Matriz de tamaño NxP (N filas, P columnas)
    # - matrizB: Matriz de tamaño PxM (P filas, M columnas)
    # - matrizC: Matriz de resultado, de tamaño NxM (N filas, M columnas)
    # - N: Número de filas de la matrizA y matrizC
    # - P: Número de columnas de matrizA y número de filas de matrizB
    # - M: Número de columnas de la matrizB y matrizC
    registros_directory = "src/file_cases"
=======
    """
    Multiplica las matrices especificadas y registra el tiempo de ejecución.

    Args:
    - matrices_filenames: Lista de nombres de archivos de las matrices a multiplicar.
    """
    registros_directory = "src/registros/NaivOnArray"
>>>>>>> 487a6519b80bcc3f213faed1887168c816d66504
    if not os.path.exists(registros_directory):
        os.makedirs(registros_directory)

    for filename in matrices_filenames:
        # Obtener la matrizA de un archivo
        matrizA = LeerMatriz.load_matrix_from_file(filename)
        n = len(matrizA)
        # Obtener la mtrizB de un archivo
        filename2 = filename.replace("num1", "num2")
        matrizB = LeerMatriz.load_matrix_from_file(filename2)
        # Matriz resultado
        matrizC = np.zeros((n, n), dtype=int)

        #Calcular tiempo de ejecucion
        start_time = time.time()
<<<<<<< HEAD

        # Multiplicar las matrices

       # resultado = NaivOnArray.multiply(matrizA, matrizB, matrizC, n, n, n ) 
       # resultado = NaivLoopUnrollingTwo.multiply(matrizA, matrizB, matrizC, n, n, n)
       # resultado = NaivLoopUnrollingFour.multiply(matrizA, matrizB, matrizC, n, n, n)
       # resultado = WinogradOriginal.multiply(matrizA, matrizB, matrizC, n, n, n)
        resultado = StrassenNaive.multiply(matrizA, matrizB, matrizC, n, n, n)

=======
        resultado = NaivOnArray.multiply(matriz1, matriz2)  # Multiplicar matrices
       # resultado = NaivLoopUnrollingTwo.multiply(matriz1, matriz2)
       # resultado = NaivLoopUnrollingFour.multiply(matriz1, matriz2)
       # resultado = WinogradOriginal.multiply(matriz1,matriz2)
       # resultado = StrassenNaive.multiply(matriz1,matriz2)
>>>>>>> 487a6519b80bcc3f213faed1887168c816d66504
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convertir a milisegundos

        # Guardar tiempo de ejecución en archivo de registro
        with open(f"{registros_directory}/registro_{n}.txt", "w") as file:
            file.write(f"Tamaño de la matriz: {n}x{n}\n")
            file.write(f"Tiempo de ejecución: {execution_time} milisegundos\n\n")

        print(f"Matrices de tamaño {n}x{n} multiplicadas. Tiempo de ejecución: {execution_time} ms")
<<<<<<< HEAD
"""
=======




def main():
    # Directorio para guardar los archivos de matrices
    directory = "src/matrices/NaivOnArray"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Tamaños de las matrices elegidos manualmente, potencias de 2
    sizes = [12, 32, 64, 126, 256, 512]  

    # Generar y guardar matrices
    matrices_filenames = generar_matrices(directory, sizes)

    # Multiplicar las matrices y registrar el tiempo de ejecución
    multiplicar_matrices(matrices_filenames)

    # Generar gráfico de barras con los tiempos de ejecución
    algorithm = "NaivOnArray"
    ChartGenerator.plot_execution_times(algorithm, sizes)


    # Directorio de registros
    registros_directory = "src/registros"

    # Obtener el tiempo de ejecución máximo de cada algoritmo
    max_times = ChartGenerator.get_max_execution_time(registros_directory)

    # Generar gráfico de barras con los tiempos de ejecución máximo
    ChartGenerator.plot_max_execution_times(max_times)

if __name__ == "__main__":
    main()


>>>>>>> 487a6519b80bcc3f213faed1887168c816d66504

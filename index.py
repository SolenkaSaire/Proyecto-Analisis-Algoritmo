from src.models.DocumentoMatrices import LeerMatriz, GeneradorMatrices
from src.models.ChartGenerator import ChartGenerator
from src.models.NaivOnArray import NaivOnArray
from src.models.NaivLoopUnrollingTwo import NaivLoopUnrollingTwo
from src.models.NaivLoopUnrollingFour import NaivLoopUnrollingFour
from src.models.WinogradOriginal import WinogradOriginal
import os
import time

def generar_matrices(directory, sizes):
    """
    Genera y guarda matrices en el directorio especificado.

    Args:
    - directory: Directorio donde se guardarán las matrices.
    - sizes: Lista de tamaños de las matrices a generar.

    Returns:
    - List[str]: Lista de nombres de archivos de las matrices generadas.
    """
    matrices_filenames = []

    for n in sizes:
        filename_aux = f"{directory}/matriz_{n}_num1.txt"
        matrices_filenames.append(filename_aux)
        for number in range(1, 3):  # Crear dos matrices de cada tamaño para multiplicar entre sí
            filename = f"{directory}/matriz_{n}_num{number}.txt"
            GeneradorMatrices.generate_matrix_to_file(n, filename)
            print(f"Matriz {number} de tamaño {n}x{n} guardada en {filename}")

    print("Todas las matrices han sido generadas y almacenadas.")
    return matrices_filenames

def multiplicar_matrices(matrices_filenames):
    """
    Multiplica las matrices especificadas y registra el tiempo de ejecución.

    Args:
    - matrices_filenames: Lista de nombres de archivos de las matrices a multiplicar.
    """
    registros_directory = "src/registros/WinogradOriginal"
    if not os.path.exists(registros_directory):
        os.makedirs(registros_directory)

    for filename in matrices_filenames:
        matriz1 = LeerMatriz.load_matrix_from_file(filename)
        n = len(matriz1)
        # Obtener el nombre de la otra matriz del mismo tamaño
        filename2 = filename.replace("num1", "num2")
        matriz2 = LeerMatriz.load_matrix_from_file(filename2)
        
        start_time = time.time()
       # resultado = NaivOnArray.multiply(matriz1, matriz2)  # Multiplicar matrices
       # resultado = NaivLoopUnrollingTwo.multiply(matriz1, matriz2)
       # resultado = NaivLoopUnrollingFour.multiply(matriz1, matriz2)
        resultado = WinogradOriginal.multiply(matriz1,matriz2)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convertir a milisegundos

        # Guardar tiempo de ejecución en archivo de registro
        with open(f"{registros_directory}/registro_{n}.txt", "w") as file:
            file.write(f"Tamaño de la matriz: {n}x{n}\n")
            file.write(f"Tiempo de ejecución: {execution_time} milisegundos\n\n")

        print(f"Matrices de tamaño {n}x{n} multiplicadas. Tiempo de ejecución: {execution_time} ms")




def main():
    # Directorio para guardar los archivos de matrices
    directory = "src/algoritmos/WinogradOriginal"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Tamaños de las matrices elegidos manualmente, potencias de 2
    sizes = [16, 32, 64, 128, 256, 512]  

    # Generar y guardar matrices
    matrices_filenames = generar_matrices(directory, sizes)

    # Multiplicar las matrices y registrar el tiempo de ejecución
    multiplicar_matrices(matrices_filenames)

    # Generar gráfico de barras con los tiempos de ejecución
    algorithm = "WinogradOriginal"
    ChartGenerator.plot_execution_times(algorithm, sizes)


    # Directorio de registros
    registros_directory = "src/registros"

    # Obtener el tiempo de ejecución máximo de cada algoritmo
    max_times = ChartGenerator.get_max_execution_time(registros_directory)

    # Generar gráfico de barras con los tiempos de ejecución máximo
    ChartGenerator.plot_max_execution_times(max_times)

if __name__ == "__main__":
    main()



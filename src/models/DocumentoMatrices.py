import os
import random

class LeerMatriz:

    @staticmethod
    def load_matrix_from_file(filename):
        matrix = []
        with open(filename, 'r') as file:
            for line in file:
                row = list(map(int, line.strip().split(", ")))
                matrix.append(row)
        return matrix

class GeneradorMatrices:

    @staticmethod
    def generate_matrix(size):
        return [[random.randint(100000, 999999) for _ in range(size)] for _ in range(size)]

    @staticmethod
    def save_matrix(matrix, filename):
        with open(filename, 'w') as file:
            for row in matrix:
                file.write(", ".join(map(str, row)) + "\n")

    @staticmethod
    def generate_matrices(directory, sizes):
        """
        Genera y guarda matrices en el directorio especificado.
        Args:
            directory (str): Directorio donde se guardarán las matrices.
            sizes (list): Lista de tamaños de las matrices a generar.
        """
        matrices_filenames = []

        for size in sizes:
            for number in range(1, 3):  # Crear dos matrices de cada tamaño para multiplicar entre sí
                filename = os.path.join(directory, f"matriz_{size}_num{number}.txt")
                matrix = GeneradorMatrices.generate_matrix(size)
                GeneradorMatrices.save_matrix(matrix, filename)
                matrices_filenames.append(filename)
                print(f"Matriz {number} de tamaño {size}x{size} guardada en {filename}")

        print("Todas las matrices han sido generadas y almacenadas.")
        return matrices_filenames
    
    @staticmethod
    def read_matrices_names(directory):
        matrices_filenames = []
        for filename in os.listdir(directory):
            if filename.endswith("num1.txt"):
                matrices_filenames.append(os.path.join(directory, filename))
        
        # Convertir los nombres de archivo a tamaños de matriz (enteros)
        matriz_sizes = [int(filename.split('_')[1]) for filename in [os.path.basename(f) for f in matrices_filenames]]

        # Eliminar los tamaños de matriz 512, 1024 y 2048
        matrices_filenames_filtered = []
        for size, filename in zip(matriz_sizes, matrices_filenames):
        #    if size not in [ 512, 2048]:
            matrices_filenames_filtered.append(filename)

        # Ordenar las matrices restantes de menor a mayor
        matrices_filenames_sorted = [x for _, x in sorted(zip(matriz_sizes, matrices_filenames_filtered))]

        return matrices_filenames_sorted


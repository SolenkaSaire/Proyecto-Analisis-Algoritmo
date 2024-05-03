import matplotlib.pyplot as plt
import numpy as np
import os

class ChartGenerator:
    @staticmethod
    def plot_execution_times(algorithm, sizes):
        """
        Crea un diagrama de barras con el tiempo de ejecución de un algoritmo para cada tamaño de matriz.

        Args:
        - algorithm: Nombre del algoritmo.
        - sizes: Lista de tamaños de las matrices.
        """
        registros_directory = f"src/registros/{algorithm}"
        execution_times = []

        for size in sizes:
            filename = f"{registros_directory}/registro_{size}.txt"
            with open(filename, "r") as file:
                lines = file.readlines()
                # Obtener el tiempo de ejecución de la segunda línea
                execution_time = float(lines[1].split(": ")[1].strip().split(" ")[0])
                execution_times.append(execution_time)

        # Crear el gráfico de barras
        plt.figure(figsize=(10, 6))  # Tamaño del gráfico
        plt.bar(sizes, execution_times, color='red',  width=15)
        plt.xlabel('Tamaño (n) de la matriz')
        plt.ylabel('Tiempo de ejecución (ms)')
        plt.title(f'Tiempos de ejecución del algoritmo {algorithm} para cada caso de prueba')
        plt.xticks(sizes)
        plt.grid(True)
         #Guardar la figura en el directorio "imágenes"
        if not os.path.exists("imagenes"):
            os.makedirs("imagenes")
        plt.savefig(f"src/imagenes/{algorithm}_execution_times.png")
        plt.show()

    @staticmethod
    def get_max_execution_time(directory):
        max_times = {}
        for algorithm in os.listdir(directory):
            algorithm_dir = os.path.join(directory, algorithm)
            if os.path.isdir(algorithm_dir):
                max_time = 0
                for filename in os.listdir(algorithm_dir):
                    filepath = os.path.join(algorithm_dir, filename)
                    if os.path.isfile(filepath):
                        with open(filepath, "r") as file:
                            lines = file.readlines()
                            execution_time = float(lines[1].split(": ")[1].split(" ")[0])
                            max_time = max(max_time, execution_time)
                max_times[algorithm] = max_time
        return max_times


    @staticmethod
    def plot_max_execution_times(max_times):
        algorithms = list(max_times.keys())
        max_execution_times = list(max_times.values())

        plt.figure(figsize=(12, 7))
        plt.bar(algorithms, max_execution_times)
        plt.xlabel('Algoritmo')
        plt.ylabel('Tiempo de ejecución máximo (ms)')
        plt.title('Tiempo de ejecución máximo por algoritmo')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)

        #Guardar la figura en el directorio "imágenes"
        if not os.path.exists("imagenes"):
            os.makedirs("imagenes")
        plt.savefig(f"src/imagenes/General.png")
        plt.show()
import matplotlib.pyplot as plt
import numpy as np
import os

class ChartGenerator:
    @staticmethod
    def plot_execution_times(algorithm):
        # Leer los datos del archivo
        sizes = []
        times = []
        with open(os.path.join("src", "file_cases", "execution_times.txt"), 'r') as file:
            for line in file:
                size, algo, time = line.strip().split('\t')
                if algo == algorithm:
                    sizes.append(int(size))
                    times.append(float(time))

        # Ordenar los datos por tamaño de matriz
        sizes, times = zip(*sorted(zip(sizes, times)))

        # Crear el gráfico de barras con barras más gruesas
        plt.figure(figsize=(12, 7))
        bars = plt.bar(sizes, times, width=5, color='skyblue')

        plt.xlabel('Tamaño (n) de la matriz')
        plt.ylabel('Tiempo de ejecución (ms)')
        plt.title(f'Tiempos de ejecución para el algoritmo {algorithm}')

        # Personalizar las etiquetas del eje x
        plt.xticks(sizes, [str(s) for s in sizes])

        # Establecer la escala lineal en el eje x
        plt.xscale('linear')

        plt.grid(True)
        # Guardar el gráfico como imagen
        if not os.path.exists("images"):
            os.makedirs("images")
        plt.savefig(f"src/images/{algorithm}.png")

        # Agregar etiquetas encima de cada barra
        #for bar, size in zip(bars, sizes):
        #    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(size), ha='center', va='bottom')
        # Mostrar el gráfico
        #plt.show()


    @staticmethod
    def get_max_execution_time():
        max_times = {}
        with open("src/file_cases/execution_times.txt", 'r') as file:
            next(file)  # Omitir la primera línea que contiene los encabezados
            for line in file:
                if line.strip():  # Asegurarse de que la línea no esté vacía
                    size, algorithm, time = line.strip().split('\t')
                    print("el tiempo es "+time)
                    time = float(time)
                    
                    # Actualizar el máximo tiempo para cada algoritmo
                    if algorithm in max_times:
                        if time > max_times[algorithm]:
                            max_times[algorithm] = time
                    else:
                        max_times[algorithm] = time
        return max_times


    @staticmethod
    def plot_max_execution_times(max_times):
        algorithms = list(max_times.keys())
        max_execution_times = list(max_times.values())

        plt.figure(figsize=(12, 7))
        plt.bar(algorithms, max_execution_times, color='skyblue',width=0.2)
        #plt.bar(algorithms, max_execution_times)
        plt.xlabel('Algoritmo')
        plt.ylabel('Tiempo de ejecución máximo (ms)')
        plt.title('Tiempo de ejecución máximo por algoritmo')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        # Guardar el gráfico como imagen
        if not os.path.exists("images"):
            os.makedirs("images")
        plt.savefig(f"src/images/General.png")
        
        #plt.show()

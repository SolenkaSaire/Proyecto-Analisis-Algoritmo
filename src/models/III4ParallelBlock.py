from multiprocessing import Pool

class III4ParallelBlock:
    @staticmethod
    def multiply_block(args):
        """
        Realiza la multiplicación de bloques de matrices A y B y almacena el resultado en un bloque de la matriz C.

        Args:
            args (tuple): Una tupla que contiene los siguientes argumentos:
                - matrizA (list): Matriz A.
                - matrizB (list): Matriz B.
                - size (int): Tamaño de las matrices.
                - bsize (int): Tamaño del bloque.
                - i1 (int): Índice de inicio de las filas para el bloque actual.
                - j1 (int): Índice de inicio de las columnas para el bloque actual.
                - k1 (int): Índice de inicio de las columnas para la iteración sobre la dimensión compartida.

        Returns:
            tuple: Una tupla que contiene los siguientes valores:
                - i1 (int): Índice de inicio de las filas para el bloque actual.
                - j1 (int): Índice de inicio de las columnas para el bloque actual.
                - result_block (list): Matriz que representa el bloque de la matriz resultante.
        """
        matrizA, matrizB, size, bsize, i1, j1, k1 = args
        result_block = [[0] * size for _ in range(size)]
        
        # Itera sobre el bloque actual de la matriz resultante
        for i in range(i1, min(i1 + bsize, size)):
            for j in range(j1, min(j1 + bsize, size)):
                # Itera sobre la dimensión compartida (k)
                for k in range(k1, min(k1 + bsize, size)):
                    result_block[i][j] += matrizA[i][k] * matrizB[k][j]
        
        return (i1, j1, result_block)

    @staticmethod
    def multiply(matrizA, matrizB, matrizC, size, bsize, aux):
        """
        Realiza la multiplicación de matrices utilizando el algoritmo III4ParallelBlock.

        Args:
            matrizA (list): Matriz A.
            matrizB (list): Matriz B.
            matrizC (list): Matriz C, donde se almacenará el resultado.
            size (int): Tamaño de las matrices.
            bsize (int): Tamaño del bloque.

        Returns:
            None
        """
        # Prepara los argumentos para los bloques de la matriz resultante
        args = []
        for i1 in range(0, size, bsize):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    args.append((matrizA, matrizB, size, bsize, i1, j1, k1))
        
        # Ejecuta los bloques de multiplicación en paralelo
        with Pool() as pool:
            results = pool.map(III4ParallelBlock.multiply_block, args)
        
        # Combina los resultados de los bloques en la matriz resultante final
        for i1, j1, result_block in results:
            for i in range(i1, min(i1 + bsize, size)):
                for j in range(j1, min(j1 + bsize, size)):
                    matrizC[i][j] += result_block[i][j]
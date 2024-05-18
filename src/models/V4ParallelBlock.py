from concurrent.futures import ThreadPoolExecutor


class V4ParallelBlock:

    @staticmethod
    def multiply(matrizA, matrizB, matrizC, size, bsize, aux):
        """
        Realiza la multiplicación de matrices utilizando el algoritmo v4ParallelBlock.

        Args:
            matrizA (list): Matriz A.
            matrizB (list): Matriz B.
            matrizC (list): Matriz C, donde se almacenará el resultado.
            size (int): Tamaño de las matrices.
            bsize (int): Tamaño del bloque.

        """
        blocks = [(i1, j1, k1) for i1 in range(0, size, bsize)
                             for j1 in range(0, size, bsize)
                             for k1 in range(0, size, bsize)]
        with ThreadPoolExecutor() as executor:
            executor.map(lambda b: V4ParallelBlock._calculate_block(matrizA, matrizB, matrizC, size, bsize, b), blocks)



    @staticmethod
    def _calculate_block(matrizA, matrizB, matrizC, size, bsize):
        """
        Calcula la multiplicación de matrices para un bloque específico.

        Args:
            matrizA (list): Matriz A.
            matrizB (list): Matriz B.
            matrizC (list): Matriz C, donde se almacenará el resultado.
            size (int): Tamaño de las matrices.
            bsize (int): Tamaño del bloque.

        """
        for i1 in range(0, size, bsize):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                matrizC[k][i] += matrizA[k][j] * matrizB[j][i]

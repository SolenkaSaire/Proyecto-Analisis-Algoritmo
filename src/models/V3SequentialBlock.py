class V3SequentialBlock:

    @staticmethod
    def multiply(matrizA, matrizB, matrizC, size, bsize, aux):
        """
        Realiza la multiplicación de matrices utilizando el algoritmo v3SequentialBlock.

        Args:
            matrizA (list): Matriz A.
            matrizB (list): Matriz B.
            matrizC (list): Matriz C, donde se almacenará el resultado.
            size (int): Tamaño de las matrices.
            bsize (int): Tamaño del bloque.

        Returns:
            None
        """
        for i1 in range(0, size, bsize):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                matrizC[k][i] += matrizA[k][j] * matrizB[j][i]

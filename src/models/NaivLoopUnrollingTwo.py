class NaivLoopUnrollingTwo:
    @staticmethod
    def multiply(matrizA, matrizB, matrizC, N, P, M):
        for i in range(N):
            for j in range(M):
                aux = 0
                if P % 2 == 0:
                    for k in range(0, P, 2):
                        aux += matrizA[i][k] * matrizB[k][j] + matrizA[i][k + 1] * matrizB[k + 1][j]
                else:
                    PP = P - 1
                    for k in range(0, PP, 2):
                        aux += matrizA[i][k] * matrizB[k][j] + matrizA[i][k + 1] * matrizB[k + 1][j]
                    aux += matrizA[i][PP] * matrizB[PP][j]
                matrizC[i][j] = aux

    # Explicación de los parámetros:
    # - matrizA: Matriz de tamaño NxP (N filas, P columnas)
    # - matrizB: Matriz de tamaño PxM (P filas, M columnas)
    # - matrizC: Matriz de resultado, de tamaño NxM (N filas, M columnas)
    # - N: Número de filas de la matrizA y matrizC
    # - P: Número de columnas de matrizA y número de filas de matrizB
    # - M: Número de columnas de la matrizB y matrizC


class NaivOnArray:
    @staticmethod
    def multiply(matrizA, matrizB, matrizC, N, P, M):
        for i in range(N):
            for j in range(M):
                matrizC[i][j] = 0
                for k in range(P):
                    matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
        return matrizC

# Explicación de los parámetros:
# - matrizA: Matriz de tamaño NxP (N filas, P columnas)
# - matrizB: Matriz de tamaño PxM (P filas, M columnas)
# - matrizC: Matriz de resultado, de tamaño NxM (N filas, M columnas)
# - N: Número de filas de la matrizA y matrizC
# - P: Número de columnas de matrizA y número de filas de matrizB
# - M: Número de columnas de la matrizB y matrizC
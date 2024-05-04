class WinogradOriginal:
    @staticmethod
    def multiply(A, B, Result, N, P, M):
        upsilon = P % 2
        gamma = P - upsilon
        y = [0] * M
        z = [0] * N

        for i in range(M):
            aux = 0
            for j in range(0, gamma, 2):
                aux += A[i][j] * A[i][j + 1]
            y[i] = aux

        for i in range(N):
            aux = 0
            for j in range(0, gamma, 2):
                aux += B[j][i] * B[j + 1][i]
            z[i] = aux

        if upsilon == 1:
            # P is odd
            PP = P - 1
            for i in range(M):
                for k in range(N):
                    aux = 0
                    for j in range(0, gamma, 2):
                        aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                    Result[i][k] = aux - y[i] - z[k] + A[i][PP] * B[PP][k]
        else:
            # P is even
            for i in range(M):
                for k in range(N):
                    aux = 0
                    for j in range(0, gamma, 2):
                        aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                    Result[i][k] = aux - y[i] - z[k]
                    
# Explicación de los parámetros:
# - A: Matriz de tamaño MxP (M filas, P columnas)
# - B: Matriz de tamaño PxN (P filas, N columnas)
# - Result: Matriz de resultado, de tamaño MxN (M filas, N columnas)
# - N: Número de columnas de la matriz B y de la matriz Result
# - P: Número de columnas de la matriz A y número de filas de la matriz B
# - M: Número de filas de la matriz A y de la matriz Result
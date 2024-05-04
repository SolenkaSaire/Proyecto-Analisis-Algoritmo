class NaivLoopUnrollingFour:
    @staticmethod
    def multiply(A, B, Result, N, P, M):
        for i in range(N):
            for j in range(M):
                aux = 0
                if P % 4 == 0:
                    for k in range(0, P, 4):
                        aux += A[i][k] * B[k][j] + A[i][k+1] * B[k+1][j] + A[i][k+2] * B[k+2][j] + A[i][k+3] * B[k+3][j]
                elif P % 4 == 1:
                    PP = P - 1
                    for k in range(0, PP, 4):
                        aux += A[i][k] * B[k][j] + A[i][k+1] * B[k+1][j] + A[i][k+2] * B[k+2][j] + A[i][k+3] * B[k+3][j]
                    aux += A[i][PP] * B[PP][j]
                elif P % 4 == 2:
                    PP = P - 2
                    PPP = P - 1
                    for k in range(0, PP, 4):
                        aux += A[i][k] * B[k][j] + A[i][k+1] * B[k+1][j] + A[i][k+2] * B[k+2][j] + A[i][k+3] * B[k+3][j]
                    aux += A[i][PP] * B[PP][j] + A[i][PPP] * B[PPP][j]
                else:
                    PP = P - 3
                    PPP = P - 2
                    PPPP = P - 1
                    for k in range(0, PP, 4):
                        aux += A[i][k] * B[k][j] + A[i][k+1] * B[k+1][j] + A[i][k+2] * B[k+2][j] + A[i][k+3] * B[k+3][j]
                    aux += A[i][PP] * B[PP][j] + A[i][PPP] * B[PPP][j] + A[i][PPPP] * B[PPPP][j]
                Result[i][j] = aux

# Explicación de los parámetros:
# - A: Matriz de tamaño NxP (N filas, P columnas)
# - B: Matriz de tamaño PxM (P filas, M columnas)
# - Result: Matriz de resultado, de tamaño NxM (N filas, M columnas)
# - N: Número de filas de la matrizA y matrizC
# - P: Número de columnas de matrizA y número de filas de matrizB
# - M: Número de columnas de la matrizB y matrizC


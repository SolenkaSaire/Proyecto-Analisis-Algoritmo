import math
from src.models.WinogradOriginal import WinogradOriginal

class WinogradScaled:
    @staticmethod
    def multiply(A, B, Result, N, P, M):
        """
        Realiza la multiplicación de matrices utilizando el algoritmo de Winograd con escalado.

        Args:
            A (List[List[int]]): Matriz de entrada A de tamaño NxP.
            B (List[List[int]]): Matriz de entrada B de tamaño PxM.
            Result (List[List[int]]): Matriz de salida de tamaño NxM para almacenar el resultado.
            N (int): Número de filas de la matriz A y la matriz Result.
            P (int): Número de columnas de la matriz A y número de filas de la matriz B.
            M (int): Número de columnas de la matriz B y la matriz Result.
        """
        print("Winograd Scaled")
        print("N: ", N)
        print("P: ", P)
        # Crear copias escaladas de A y B
        CopyA = [[0 for _ in range(P)] for _ in range(N)]
        CopyB = [[0 for _ in range(M)] for _ in range(P)]
        
        # Calcular factores de escala
        a = WinogradScaled.NormInf(A, N, P)
        b = WinogradScaled.NormInf(B, P, M)
        lambda_val = math.floor(0.5 + math.log(b/a)/math.log(4))
        
        # Escalar
        WinogradScaled.MultiplyWithScalar(A, CopyA, N, P, 2 ** lambda_val)
        WinogradScaled.MultiplyWithScalar(B, CopyB, P, M, 2 ** -lambda_val)
        
        # Usar Winograd con las matrices escaladas
        WinogradOriginal.multiply(CopyA, CopyB, Result, N, P, M)

    @staticmethod
    def MultiplyWithScalar(A, B, N, M, scalar):
        """
        Multiplica la matriz A por un escalar y almacena el resultado en la matriz B.

        Args:
            A (List[List[int]]): Matriz de entrada.
            B (List[List[int]]): Matriz de salida donde se almacenará el resultado.
            N (int): Número de filas de la matriz.
            M (int): Número de columnas de la matriz.
            scalar (int): Escalar por el cual multiplicar la matriz A.
        """
        for i in range(N):
            for j in range(M):
                B[i][j] = A[i][j] * scalar

    @staticmethod
    def NormInf(A, N, M):
        """
        Calcula la norma infinito de una matriz.

        Args:
            A (List[List[int]]): Matriz de entrada.
            N (int): Número de filas de la matriz.
            M (int): Número de columnas de la matriz.

        Returns:
            int: Valor de la norma infinito de la matriz.
        """
        max_val = float('-inf')
        for i in range(N):
            sum_val = sum(abs(A[i][j]) for j in range(M))
            max_val = max(max_val, sum_val)
        return max_val

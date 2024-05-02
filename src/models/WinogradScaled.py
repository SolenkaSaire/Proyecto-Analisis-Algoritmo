from src.models.WinogradOriginal import WinogradOriginal

class WinogradScaled:
    @staticmethod
    def multiply(matriz1, matriz2):
        """ Multiplica dos matrices utilizando el algoritmo de Winograd escalado.
        Args:
            - matriz1 (list): Primera matriz (N x P).
            - matriz2 (list): Segunda matriz (P x M).
        Returns:
            - list: Resultado de la multiplicación de matrices matriz1 y matriz2.
        """
        # Dimensiones de las matrices
        N = len(matriz1)
        P = len(matriz1[0])
        P2 = len(matriz2)
        M = len(matriz2[0])
        if P != P2:
            raise ValueError("Las dimensiones interiores de las matrices deben coincidir.")

        # Calcular factores de escala basados en la norma infinito
        a = WinogradScaled.norma_infinito(matriz1)
        b = WinogradScaled.norma_infinito(matriz2)
        if a == 0 or b == 0:
            raise ValueError("La norma de una de las matrices es cero, lo que puede indicar una matriz vacía.")

        # Calcular lambda para el escalado
        lambda_ = int(0.5 + WinogradScaled.log(b / a, 4))

        # Escalar las matrices
        CopyMatriz1 = WinogradScaled.escalar_matriz(matriz1, 2 ** lambda_)
        CopyMatriz2 = WinogradScaled.escalar_matriz(matriz2, 2 ** -lambda_)

        # Multiplicar usando el algoritmo de Winograd
        Result = WinogradOriginal.multiply(CopyMatriz1, CopyMatriz2)
        return Result

    @staticmethod
    def norma_infinito(matriz):
        N = len(matriz)
        M = len(matriz[0])
        norma = 0
        for i in range(N):
            suma_fila = sum(abs(x) for x in matriz[i])
            norma = max(norma, suma_fila)
        return norma

    @staticmethod
    def log(x, base):
        return WinogradScaled.ln(x) / WinogradScaled.ln(base)

    @staticmethod
    def ln(x):
        n = 100000
        return n * ((x ** (1 / n)) - 1)

    @staticmethod
    def escalar_matriz(matriz, escalar):
        N = len(matriz)
        M = len(matriz[0])
        matriz_escalada = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                matriz_escalada[i][j] = matriz[i][j] * escalar
        return matriz_escalada
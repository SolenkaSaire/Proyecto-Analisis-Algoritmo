class StrassenNaive:
    @staticmethod
    def multiply(A, B):
        # Obtener las dimensiones de las matrices
        N = len(A)
        P = len(A[0])
        P2 = len(B)
        M = len(B[0])
        if P != P2:
            raise ValueError("Las dimensiones interiores de las matrices A y B deben coincidir.")

        # Encuentra el tamaño máximo para redimensionar las matrices
        MaxSize = max(N, P, M)
        if MaxSize < 16:
            MaxSize = 16  # Fijar un mínimo para que el algoritmo funcione correctamente

        # Calcular k y m basados en MaxSize
        k = int(StrassenNaive.log2(MaxSize)) - 4
        m = int(MaxSize * 2**(-k)) + 1
        NewSize = m * (2**k)

        # Crear nuevas matrices con tamaño ajustado llenas de ceros
        NewA = StrassenNaive.crear_matriz(NewSize, NewSize)
        NewB = StrassenNaive.crear_matriz(NewSize, NewSize)

        # Copiar los datos originales en las nuevas matrices
        for i in range(N):
            for j in range(P):
                NewA[i][j] = A[i][j]
        for i in range(P):
            for j in range(M):
                NewB[i][j] = B[i][j]

        # Multiplicar usando el método de Strassen
        AuxResult = StrassenNaive.strassen_naiv_step(NewA, NewB, NewSize, m)

        # Extraer el resultado en el tamaño original
        Result = StrassenNaive.crear_matriz(N, M)
        for i in range(N):
            for j in range(M):
                Result[i][j] = AuxResult[i][j]

        return Result

    @staticmethod
    def crear_matriz(N, M):
        matriz = [[0 for _ in range(M)] for _ in range(N)]
        return matriz

    @staticmethod
    def log2(x):
        n = 100000
        return StrassenNaive.ln(x) / StrassenNaive.ln(2)

    @staticmethod
    def ln(x):
        n = 100000
        return n * ((x ** (1 / n)) - 1)

    @staticmethod
    def strassen_naiv_step(A, B, N, m):
        if N <= m:
            # Caso base: multiplicar matrices pequeñas directamente
            C = StrassenNaive.crear_matriz(N, N)
            for i in range(N):
                for j in range(N):
                    sum = 0
                    for k in range(N):
                        sum += A[i][k] * B[k][j]
                    C[i][j] = sum
            return C

        # Dividir matrices en cuadrantes
        a11, a12, a21, a22 = StrassenNaive.dividir_matriz(A, N)
        b11, b12, b21, b22 = StrassenNaive.dividir_matriz(B, N)

        # Calcular productos de matrices
        p1 = StrassenNaive.strassen_naiv_step(a11, StrassenNaive.restar_matrices(b12, b22, N // 2), N // 2, m)
        p2 = StrassenNaive.strassen_naiv_step(StrassenNaive.sumar_matrices(a11, a12, N // 2), b22, N // 2, m)
        p3 = StrassenNaive.strassen_naiv_step(StrassenNaive.sumar_matrices(a21, a22, N // 2), b11, N // 2, m)
        p4 = StrassenNaive.strassen_naiv_step(a22, StrassenNaive.sumar_matrices(b21, b22, N // 2), N // 2, m)
        p5 = StrassenNaive.strassen_naiv_step(StrassenNaive.sumar_matrices(a11, a22, N // 2), StrassenNaive.sumar_matrices(b11, b22, N // 2), N // 2, m)
        p6 = StrassenNaive.strassen_naiv_step(StrassenNaive.restar_matrices(a12, a22, N // 2), StrassenNaive.sumar_matrices(b21, b11, N // 2), N // 2, m)
        p7 = StrassenNaive.strassen_naiv_step(StrassenNaive.restar_matrices(a11, a21, N // 2), StrassenNaive.sumar_matrices(b11, b12, N // 2), N // 2, m)

        # Calcular cuadrantes de la matriz resultante
        c11 = StrassenNaive.sumar_matrices(StrassenNaive.restar_matrices(StrassenNaive.sumar_matrices(p5, p4, N // 2), p2, N // 2), p6, N // 2)
        c12 = StrassenNaive.sumar_matrices(p1, p2, N // 2)
        c21 = StrassenNaive.sumar_matrices(p3, p4, N // 2)
        c22 = StrassenNaive.sumar_matrices(StrassenNaive.restar_matrices(StrassenNaive.sumar_matrices(p5, p1, N // 2), p3, N // 2), p7, N // 2)

        # Combinar cuadrantes en una sola matriz
        C = StrassenNaive.combinar_matrices(c11, c12, c21, c22, N)
        return C

    @staticmethod
    def dividir_matriz(A, N):
        mid = N // 2
        a11 = [row[:mid] for row in A[:mid]]
        a12 = [row[mid:] for row in A[:mid]]
        a21 = [row[:mid] for row in A[mid:]]
        a22 = [row[mid:] for row in A[mid:]]
        return a11, a12, a21, a22

    @staticmethod
    def sumar_matrices(A, B, N):
        C = StrassenNaive.crear_matriz(N, N)
        for i in range(N):
            for j in range(N):
                C[i][j] = A[i][j] + B[i][j]
        return C

    @staticmethod
    def restar_matrices(A, B, N):
        C = StrassenNaive.crear_matriz(N, N)
        for i in range(N):
            for j in range(N):
                C[i][j] = A[i][j] - B[i][j]
        return C

    @staticmethod
    def combinar_matrices(a11, a12, a21, a22, N):
        A = StrassenNaive.crear_matriz(N, N)
        mid = N // 2
        for i in range(mid):
            for j in range(mid):
                A[i][j] = a11[i][j]
                A[i][j + mid] = a12[i][j]
                A[i + mid][j] = a21[i][j]
                A[i + mid][j + mid] = a22[i][j]
        return A
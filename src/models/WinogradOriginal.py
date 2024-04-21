class WinogradOriginal:
    @staticmethod
    def multiply(A, B):
        N = len(A)
        P = len(B)
        M = len(A[0])

        upsilon = P % 2
        gamma = P - upsilon
        y = [0] * M
        z = [0] * N

        # Compute y
        for i in range(M):
            aux = 0.0
            for j in range(0, gamma, 2):
                aux += A[i][j] * A[i][j + 1]
            y[i] = aux

        # Compute z
        for i in range(N):
            aux = 0.0
            for j in range(0, gamma, 2):
                aux += B[j][i] * B[j + 1][i]
            z[i] = aux

        # Initialize result matrix
        Result = [[0] * N for _ in range(M)]

        if upsilon == 1:
            # P is odd
            PP = P - 1
            for i in range(M):
                for k in range(N):
                    aux = 0.0
                    for j in range(0, gamma, 2):
                        aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                    Result[i][k] = aux - y[i] - z[k] + A[i][PP] * B[PP][k]
        else:
            # P is even
            for i in range(M):
                for k in range(N):
                    aux = 0.0
                    for j in range(0, gamma, 2):
                        aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                    Result[i][k] = aux - y[i] - z[k]

        return Result

import math
from src.models.NaivOnArray import NaivOnArray

class StrassenWinograd:

    @staticmethod
    def multiply(matrizA, matrizB, matrizC, N, P, M):
        MaxSize = max(N, P, M)
        if MaxSize < 16:
            MaxSize = 16  # otherwise it is not possible to compute k
        k = int(math.floor(math.log(MaxSize) / math.log(2))) - 4
        m = int(math.floor(MaxSize * 2 ** (-k))) + 1
        NewSize = m * 2 ** k

        # add zero rows and columns to use Strassens algorithm
        NewA = [[0] * NewSize for _ in range(NewSize)]
        NewB = [[0] * NewSize for _ in range(NewSize)]
        AuxResult = [[0] * NewSize for _ in range(NewSize)]

        for i in range(N):
            for j in range(P):
                NewA[i][j] = matrizA[i][j]
        for i in range(P):
            for j in range(M):
                NewB[i][j] = matrizB[i][j]
    

    @staticmethod
    def StrassenWinogradStep(A, B, Result, N, m):
        if (N % 2 == 0) and (N > m):  # recursive use of StrassenNaivStep
            NewSize = N // 2

            # decompose A and B
            # create ResultPart, Aux1,...,Aux7 and Helper1, Helper2
            A1 = [[0] * NewSize for _ in range(NewSize)]
            A2 = [[0] * NewSize for _ in range(NewSize)]
            B1 = [[0] * NewSize for _ in range(NewSize)]
            B2 = [[0] * NewSize for _ in range(NewSize)]

            A11 = [[0] * NewSize for _ in range(NewSize)]
            A12 = [[0] * NewSize for _ in range(NewSize)]
            A21 = [[0] * NewSize for _ in range(NewSize)]
            A22 = [[0] * NewSize for _ in range(NewSize)]
            B11 = [[0] * NewSize for _ in range(NewSize)]
            B12 = [[0] * NewSize for _ in range(NewSize)]
            B21 = [[0] * NewSize for _ in range(NewSize)]
            B22 = [[0] * NewSize for _ in range(NewSize)]

            ResultPart11 = [[0] * NewSize for _ in range(NewSize)]
            ResultPart12 = [[0] * NewSize for _ in range(NewSize)]
            ResultPart21 = [[0] * NewSize for _ in range(NewSize)]
            ResultPart22 = [[0] * NewSize for _ in range(NewSize)]

            Helper1 = [[0] * NewSize for _ in range(NewSize)]
            Helper2 = [[0] * NewSize for _ in range(NewSize)]

            Aux1 = [[0] * NewSize for _ in range(NewSize)]
            Aux2 = [[0] * NewSize for _ in range(NewSize)]
            Aux3 = [[0] * NewSize for _ in range(NewSize)]
            Aux4 = [[0] * NewSize for _ in range(NewSize)]
            Aux5 = [[0] * NewSize for _ in range(NewSize)]
            Aux6 = [[0] * NewSize for _ in range(NewSize)]
            Aux7 = [[0] * NewSize for _ in range(NewSize)]
            Aux8 = [[0] * NewSize for _ in range(NewSize)]
            Aux9 = [[0] * NewSize for _ in range(NewSize)]

            for i in range(NewSize):
                A1[i] = [0] * NewSize
                A2[i] = [0] * NewSize
                B1[i] = [0] * NewSize
                B2[i] = [0] * NewSize
                A11[i] = [0] * NewSize
                A12[i] = [0] * NewSize
                A21[i] = [0] * NewSize
                A22[i] = [0] * NewSize
                B11[i] = [0] * NewSize
                B12[i] = [0] * NewSize
                B21[i] = [0] * NewSize
                B22[i] = [0] * NewSize

                ResultPart11[i] = [0] * NewSize
                ResultPart12[i] = [0] * NewSize
                ResultPart21[i] = [0] * NewSize
                ResultPart22[i] = [0] * NewSize

                Helper1[i] = [0] * NewSize
                Helper2[i] = [0] * NewSize

                Aux1[i] = [0] * NewSize
                Aux2[i] = [0] * NewSize
                Aux3[i] = [0] * NewSize
                Aux4[i] = [0] * NewSize
                Aux5[i] = [0] * NewSize
                Aux6[i] = [0] * NewSize
                Aux7[i] = [0] * NewSize
                Aux8[i] = [0] * NewSize
                Aux9[i] = [0] * NewSize
        
            # fill new matrices
            for i in range(NewSize):
                for j in range(NewSize):
                    A11[i][j] = A[i][j]
                    A12[i][j] = A[i][NewSize + j]
                    A21[i][j] = A[NewSize + i][j]
                    A22[i][j] = A[NewSize + i][NewSize + j]
                    B11[i][j] = B[i][j]
                    B12[i][j] = B[i][NewSize + j]
                    B21[i][j] = B[NewSize + i][j]
                    B22[i][j] = B[NewSize + i][NewSize + j]

            # calculate helper matrices
            # computing the 4 + 9 aux. variables
            StrassenWinograd.Minus(A11, A21, A1, NewSize, NewSize)
            StrassenWinograd.Minus(A22, A1, A2, NewSize, NewSize)
            StrassenWinograd.Minus(B22, B12, B1, NewSize, NewSize)
            StrassenWinograd.Plus(B1, B11, B2, NewSize, NewSize)

            StrassenWinograd.StrassenWinogradStep(A11, B11, Aux1, NewSize, m)
            StrassenWinograd.StrassenWinogradStep(A12, B21, Aux2, NewSize, m)
            StrassenWinograd.StrassenWinogradStep(A2, B2, Aux3, NewSize, m)
            StrassenWinograd.Plus(A21, A22, Helper1, NewSize, NewSize)
            StrassenWinograd.Minus(B12, B11, Helper2, NewSize, NewSize)
            StrassenWinograd.StrassenWinogradStep(Helper1, Helper2, Aux4, NewSize, m)
            StrassenWinograd.StrassenWinogradStep(A1, B1, Aux5, NewSize, m)
            StrassenWinograd.Minus(A12, A2, Helper1, NewSize, NewSize)
            StrassenWinograd.StrassenWinogradStep(Helper1, B22, Aux6, NewSize, m)
            StrassenWinograd.Minus(B21, B2, Helper1, NewSize, NewSize)
            StrassenWinograd.StrassenWinogradStep(A22, Helper1, Aux7, NewSize, m)
            StrassenWinograd.Plus(Aux1, Aux3, Aux8, NewSize, NewSize)
            StrassenWinograd.Plus(Aux8, Aux4, Aux9, NewSize, NewSize)

            # computing the four parts of the result
            StrassenWinograd.Plus(Aux1, Aux2, ResultPart11, NewSize, NewSize)
            StrassenWinograd.Plus(Aux9, Aux6, ResultPart12, NewSize, NewSize)
            StrassenWinograd.Plus(Aux8, Aux5, Helper1, NewSize, NewSize)
            StrassenWinograd.Plus(Helper1, Aux7, ResultPart21, NewSize, NewSize)
            StrassenWinograd.Plus(Aux9, Aux5, ResultPart22, NewSize, NewSize)

            # fill result matrix
            # store results in the "result matrix"
            for i in range(NewSize):
                for j in range(NewSize):
                    Result[i][j] = ResultPart11[i][j]

            for i in range(NewSize):
                for j in range(NewSize):
                    Result[i][NewSize + j] = ResultPart12[i][j]

            for i in range(NewSize):
                for j in range(NewSize):
                    Result[NewSize + i][j] = ResultPart21[i][j]

            for i in range(NewSize):
                for j in range(NewSize):
                    Result[NewSize + i][NewSize + j] = ResultPart22[i][j]

            # free helper variables
            A1 = None
            A2 = None
            B1 = None
            B2 = None

            A11 = None
            A12 = None
            A21 = None
            A22 = None

            B11 = None
            B12 = None
            B21 = None
            B22 = None

            ResultPart11 = None
            ResultPart12 = None
            ResultPart21 = None
            ResultPart22 = None

            Helper1 = None
            Helper2 = None

            Aux1 = None
            Aux2 = None
            Aux3 = None
            Aux4 = None
            Aux5 = None
            Aux6 = None
            Aux7 = None

        else:
            # use naiv algorithm
            NaivOnArray.multiply(A, B, Result, N, N, N)




    @staticmethod
    def Minus(matrixA, matrixB, result, rows, cols):
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrixA[i][j] - matrixB[i][j]

    @staticmethod
    def Plus(matrixA, matrixB, result, rows, cols):
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrixA[i][j] + matrixB[i][j]

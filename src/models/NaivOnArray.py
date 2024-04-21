class NaivOnArray:
    @staticmethod
    def multiply(a, b):
        rowsA = len(a)
        colsA = len(a[0])
        rowsB = len(b)
        colsB = len(b[0])

        if colsA != rowsB:
            raise ValueError("Las matrices no se pueden multiplicar. El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        c = [[0] * colsB for _ in range(rowsA)]
        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    c[i][j] += a[i][k] * b[k][j]
        return c

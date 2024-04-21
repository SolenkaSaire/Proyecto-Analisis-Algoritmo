class NaivLoopUnrollingTwo:
    @staticmethod
    def multiply(a, b):
        size = len(a)
        result = [[0] * size for _ in range(size)]

        for i in range(0, size, 2):
            for j in range(0, size, 2):
                for k in range(0, size, 2):
                    sum1 = a[i][k] * b[k][j] + a[i][k + 1] * b[k + 1][j]
                    sum2 = a[i][k] * b[k][j + 1] + a[i][k + 1] * b[k + 1][j + 1]
                    sum3 = a[i + 1][k] * b[k][j] + a[i + 1][k + 1] * b[k + 1][j]
                    sum4 = a[i + 1][k] * b[k][j + 1] + a[i + 1][k + 1] * b[k + 1][j + 1]
                    result[i][j] += sum1
                    result[i][j + 1] += sum2
                    result[i + 1][j] += sum3
                    result[i + 1][j + 1] += sum4

        return result

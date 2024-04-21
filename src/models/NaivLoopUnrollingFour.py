class NaivLoopUnrollingFour:
    @staticmethod
    def multiply(a, b):
        size = len(a)
        result = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(0, size, 4):
            for j in range(0, size, 4):
                for k in range(0, size, 4):
                    for i1 in range(i, min(i + 4, size)):
                        for j1 in range(j, min(j + 4, size)):
                            for k1 in range(k, min(k + 4, size)):
                                result[i1][j1] += a[i1][k1] * b[k1][j1]

        return result

from multiprocessing import Pool

class IV5EnhancedParallelBlock:
    @staticmethod
    def multiply_block(args):
        i1, j1, k1, bsize, size, matrizA, matrizB, matrizC = args
        for i in range(i1, min(i1 + bsize, size)):
            for j in range(j1, min(j1 + bsize, size)):
                for k in range(k1, min(k1 + bsize, size)):
                    matrizC[i][k] += matrizA[i][j] * matrizB[j][k]

    @staticmethod
    def multiply(matrizA, matrizB, matrizC, bsize, size, csize):
        pool = Pool(processes=2)  # Dos procesos para ejecutar en paralelo
        pool.map(IV5EnhancedParallelBlock.multiply_block, [
            (i1, j1, k1, bsize, size, matrizA, matrizB, matrizC)
            for i1 in range(0, size, size // 2)
            for j1 in range(0, size, bsize)
            for k1 in range(0, size, bsize)
        ])
        pool.close()
        pool.join()

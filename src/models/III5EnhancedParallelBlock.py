from multiprocessing import Process

class III5EnhancedParallelBlock:
    
    @staticmethod
    def calculate_block(i1, j1, k1, A, B, C, bsize, size):
        for i in range(i1, min(i1 + bsize, size)):
            for j in range(j1, min(j1 + bsize, size)):
                for k in range(k1, min(k1 + bsize, size)):
                    A[i][j] += B[i][k] * C[k][j]

    @staticmethod
    def process_block(i1, j1, k1, A, B, C, bsize, size):
        III5EnhancedParallelBlock.calculate_block(i1, j1, k1, A, B, C, bsize, size)

    @staticmethod
    def multiply(A, B, C, bsize, size, csize):
        processes = []

        # Proceso para la primera mitad del trabajo
        p1 = Process(target=III5EnhancedParallelBlock.process_block, args=(0, 0, 0, A, B, C, bsize, size))
        p1.start()
        processes.append(p1)

        # Proceso para la segunda mitad del trabajo
        p2 = Process(target=III5EnhancedParallelBlock.process_block, args=(size // 2, 0, 0, A, B, C, bsize, size))
        p2.start()
        processes.append(p2)

        # Esperar a que ambos procesos terminen
        for p in processes:
            p.join()

# Ejemplo de uso
#size = 10
#bsize = 2
#A = [[0] * size for _ in range(size)]
#B = [[1] * size for _ in range(size)]
#C = [[2] * size for _ in range(size)]

#III5EnhancedParallelBlock.multiply(A, B, C, bsize, size, size)

# Imprimir resultado
#for# row in A:
#    print(row)

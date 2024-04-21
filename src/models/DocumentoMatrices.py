import random

class LeerMatriz:

    @staticmethod
    def load_matrix_from_file(filename):
        matrix = []
        with open(filename, 'r') as file:
            for line in file:
                row = list(map(int, line.strip().split(", ")))
                matrix.append(row)
        return matrix

class GeneradorMatrices:

    @staticmethod
    def generate_matrix_to_file(size, filename):
        matrix = [[random.randint(100000, 999999) for _ in range(size)] for _ in range(size)]
        with open(filename, 'w') as file:
            for row in matrix:
                file.write(", ".join(map(str, row)) + "\n")



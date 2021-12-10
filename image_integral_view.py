import random


def print_matrix(matrix: list[list]):
    for row in matrix:
        print(*row)


def generate_random_matrix(width: int, height: int) -> list[list]:
    return [[random.randint(0, 255) for x in range(width)] for y in range(height)]


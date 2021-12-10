import random
import copy


def print_matrix(matrix: list[list]):
    for row in matrix:
        print(*row)


def generate_random_matrix(width: int, height: int) -> list[list]:
    return [[random.randint(0, 255) for x in range(width)] for y in range(height)]


def integral_view(image: list[list]) -> list[list]:
    integral_matrix = copy.deepcopy(image)

    for y in range(len(integral_matrix)):
        for x in range(len(integral_matrix[0])):
            left_cell = integral_matrix[y][x - 1] if x > 0 else 0
            up_cell = integral_matrix[y - 1][x] if y > 0 else 0
            diagonal_cell = integral_matrix[y - 1][x - 1] if x > 0 and y > 0 else 0
            integral_matrix[y][x] += left_cell + up_cell - diagonal_cell

    return integral_matrix

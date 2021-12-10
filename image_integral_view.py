import random


def print_matrix(matrix: list[list]):
    for row in matrix:
        print(*row)


def generate_random_matrix(width: int, height: int) -> list[list]:
    return [[random.randint(0, 255) for x in range(width)] for y in range(height)]


def integral_view(image: list[list]) -> list[list]:
    integral_matrix = list(image)

    for y in range(len(image)):
        for x in range(len(image[0])):
            left_cell = integral_matrix[y][x - 1] if x > 0 else 0
            up_cell = integral_matrix[y - 1][x] if y > 0 else 0
            diagonal_cell = integral_matrix[y - 1][x - 1] if x > 0 and y > 0 else 0
            integral_matrix[y][x] += left_cell + up_cell - diagonal_cell

    return integral_matrix


def rect_sum(image: list[list], x1: int, y1: int, x2: int, y2: int) -> int:
    integral_matrix = integral_view(image)

    a_sum = integral_matrix[y1 - 1][x1 - 1] if y1 > 0 and x1 > 0 else 0
    b_sum = integral_matrix[y1 - 1][x2] if y1 > 0 else 0
    c_sum = integral_matrix[y2][x2]
    d_sum = integral_matrix[y2][x1 - 1] if x1 > 0 else 0

    return a_sum + c_sum - d_sum - b_sum

def get_square_side(square_side: float) -> tuple:
    """
        Take the side of the square and return 3 values: perimeter, area, and diagonal of the square
    """
    square_perimeter = square_side * 4
    square_area = pow(square_side, 2)
    square_diagonal = round(square_side * (2 ** (0.5)))
    return square_perimeter, square_area, square_diagonal


if __name__ == "__main__":
    square_parameters = get_square_side(float(input("Please, enter the square side: ")))
    print(f'Square perimeter = {square_parameters[0]}\n'
          f'Square area = {square_parameters[1]}\n'
          f'Square diagonal = {square_parameters[2]}')

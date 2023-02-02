import re


def no_digits_file(text_file_name: str):
    """
    Take the text file and remove all numbers from each line of the file.
    """
    with open(text_file_name, 'r') as file:
        new_file = file.readlines()
        text_without_digits = []

        for line in new_file:
            text_without_digits.append(re.sub(r'\d+', '', line))
    return text_without_digits


if __name__ == "__main__":
    print(no_digits_file("text_file_name"))

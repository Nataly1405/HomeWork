class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < 0:
            raise ValueError('negative values is unsupported for start index')
        elif self.__start_index > self.__end_index:
            raise ValueError('Start index can not be bigger or equal to the end index')
        elif self.__start_index > len(self.__sequence):
            raise ValueError('unexpected start index')
        elif self.__end_index > len(self.__sequence):
            self.__end_index = len(self.__sequence)
        elif self.__start_index < self.__end_index:
            item = self.__sequence[self.__start_index]
            self.__start_index += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    custom_iterator = CustomIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 8)

    for number in custom_iterator:
        print(number)

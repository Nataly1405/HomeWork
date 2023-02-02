class Train:
    def __init__(self, wagons: list):
        self.__wagons = wagons

    @property
    def wagons(self):
        return self.__wagons

    @wagons.setter
    def wagons(self, wagon_number: int):
        if wagon_number in self.__wagons:
            print(f"Oops, number {wagon_number} is already exist")
        elif wagon_number <= 0:
            print(f'number {wagon_number} is unsupported')
        else:
            self.__wagons.append(wagon_number)

    def __len__(self):
        return len(self.__wagons)

    def __str__(self):
        train_wagons = '<=[HEAD]'
        for wagon_number in sorted(self.__wagons):
            train_wagons += f'-[{wagon_number}]'
        return train_wagons


if __name__ == '__main__':
    train = Train([1, 3, 4, 5, 2])
    print(train)
    print(len(train))

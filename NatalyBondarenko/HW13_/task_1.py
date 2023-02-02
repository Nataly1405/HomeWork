class Tent:
    def __init__(self, firm_name: str, weight: float, tent_capacity: int, price: float):
        self.__firm_name = firm_name
        self.__weight = weight
        self.__tent_capacity = tent_capacity
        self.__price = price

    @property
    def firm_name(self):
        return self.__firm_name

    @firm_name.setter
    def firm_name(self, another_firm_name: str):
        if not another_firm_name:
            print("Empty value is not supported for firm name")
        else:
            self.__firm_name = another_firm_name.capitalize()

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight_value: float):
        if weight_value < 1:
            print(f'Tent weight can not be equal to {weight_value}')
        elif weight_value > 5:
            print(f'{weight_value} kilograms is too much weight for a tent, lets take another one')
        else:
            print(f'{weight_value} kilograms is an acceptable weight for a tent, lets take it')

    @property
    def tent_capacity(self):
        return self.__tent_capacity

    @tent_capacity.setter
    def tent_capacity(self, tent_capacity_value: int):
        if tent_capacity_value < 1:
            print(f'{tent_capacity_value} is unsupported value')
        elif 5 > tent_capacity_value >= 1:
            print(f'Tent for {tent_capacity_value} people - suits us. Lets buy!')
        else:
            print(f'Tent for {tent_capacity_value} people - too big for us, lets take a smaller one')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price < 1:
            print(f'{new_price} - this value is not available for the tent price')
        elif new_price > 400:
            print(f'wow, {new_price} dollars is too expensive for tent ')
        else:
            print(f'{new_price} dollars - it is a good price. Lets take it!')

    def __str__(self):
        tent = f'{self.__class__.__name__}:\n{{\n\tfirm name: {self.__firm_name}\n}}\n' \
               f'{{\n\tweight: {self.__weight}\n}}\n' \
               f'{{\n\ttent capacity: {self.__tent_capacity}\n}}\n' \
               f'{{\n\tprice: {self.__price}\n}}'
        return tent


if __name__ == '__main__':
    my_tent = Tent('Mountain Safety Research', 900, 3, 150)
    print(my_tent)

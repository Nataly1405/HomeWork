class Worker:
    def __init__(self, first_name: str, last_name: str, age: int, position: str, salary: float):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__position = position
        self.__salary = salary

    @property
    def first_name(self):
        """
        Method  getting the worker's name
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name: str):
        """
        method allows to change the name of the worker
        """
        if new_first_name:
            self.__first_name = new_first_name.capitalize()
        else:
            print('Empty value is not supported for worker name')

    @first_name.deleter
    def first_name(self):
        """
        method will protect code against class design break
        """
        pass

    @property
    def last_name(self):
        """
        Method  getting the worker's last name
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name: str):
        if self.__last_name == new_last_name:
            print(f'{new_last_name} - this last name already exists for this worker')
        elif not new_last_name:
            print('Empty value is not supported for worker last name')
        else:
            self.__last_name = new_last_name.capitalize()

    @last_name.deleter
    def last_name(self):
        """
        method will protect code against class design break
        """
        pass

    @property
    def age(self):
        """
        Method  getting the worker's age
        """
        return self.__age

    def age_verification(self):
        """
        Method verified that worker's age is more than 18 years old
        """
        if self.__age < 18:
            print(f'Sorry, people under 18 years old can not works in our company')
        else:
            print('We are glad that you are part of our company')

    def grow_up(self):
        self.__age += 1

    @age.deleter
    def age(self):
        """
        method will protect code against class design break
        """
        pass

    @property
    def position(self):
        """
        Method  getting the worker's position
        """
        return self.__position

    @position.setter
    def position(self, new_position: str):
        """
        Method to update the worker's position in the company
        """
        if self.__position == new_position:
            print('this position is identical to the one in which the employee is already works')
        elif not new_position:
            print('Empty value is not supported for determine the position')
        else:
            self.__position = new_position

    @position.deleter
    def position(self):
        """
        method will protect code against class design break
        """
        pass

    @property
    def salary(self):
        """
        Method  getting the worker's salary
        """
        return self.__salary

    @salary.setter
    def salary(self, salary_increase: int):
        """
        Method to increase the worker's salary
        """
        if salary_increase < 1:
            print(f'{salary_increase} is unsupported value for salary_increase')
        elif salary_increase <= self.__salary:
            print('salary cannot be lower than current salary')
        else:
            self.__salary = salary_increase

    def worker_bonus(self):
        """
        Method to count the  worker's bonus based on worker's age
        """
        if self.__age < 30:
            return self.__salary + 1000
        elif 30 < self.__age < 40:
            return self.__salary + 2000
        else:
            return self.__salary + 5000

    @staticmethod
    def annual_bonus():
        """
        Method to count the  annual bonus for each employee
        """
        return 274 * 50 + 100


if __name__ == '__main__':
    worker = Worker('Benedict', 'Eggs', 37, 'Technical support', 12000)

    worker.first_name = 'lucas'
    print(worker.first_name)
    worker.first_name = ''
    del worker.first_name
    print(worker.first_name)

    worker.last_name = 'Eggs'
    print(worker.last_name)
    worker.last_name = 'Eggs'
    worker.last_name = 'brauni'
    print(worker.last_name)
    print(worker.age)
    worker.grow_up()
    print(worker.age)

    worker.position = 'Technical support'
    worker.position = ''
    print(worker.position)
    worker.position = 'Team Lead Technical Support'
    del worker.position
    print(worker.position)

    worker.salary = 1
    print(worker.salary)
    worker.salary = 15000
    print(worker.salary)

    print(worker.annual_bonus())
    print(worker.worker_bonus())

class School:
    def __init__(self, school_number: int, director: str, secretary: str, number_of_students: int):
        self.__school_number = school_number
        self.__director = director
        self.__secretary = secretary
        self.__number_of_students = number_of_students

    def school_number(self):
        return self.__school_number

    @property
    def director(self):
        """ Encapsulation"""

        return self.__director.capitalize()

    @property
    def secretary(self):
        return self.__secretary

    def number_of_students(self):
        return self.__number_of_students

    def school_bio(self):
        return f"School number is: {self.__school_number}\n" \
               f"Director of the schools is: {self.__director}\n" \
               f"Secretary of the school is: {self.__secretary}\n" \
               f"Total number of students in school is: {self.__number_of_students}\n"


class Classes:
    """ Polymorphism"""

    def __init__(self, number_of_class: int, flor_in_the_school: int):
        self.__number_of_class = number_of_class
        self.__flor_in_the_school = flor_in_the_school

    def number_of_class(self):
        return self.__number_of_class

    def flor_in_the_school(self):
        return self.__flor_in_the_school


class ClassOfMath(Classes):
    def __init__(self, number_of_class: int, flor_in_the_school: int, subject: str):
        super(ClassOfMath, self).__init__(number_of_class, flor_in_the_school)
        self.__subject = subject

    def subject(self):
        return self.__subject

    def class_info(self):
        return print(f"This is class of {self.__subject}, number of the classroom is {self.number_of_class()}, "
                     f"and you can find it on the {self.flor_in_the_school()} flor\n")


class ClassOfSport(Classes):
    def __init__(self, number_of_class: int, flor_in_the_school: int, subject: str):
        super(ClassOfSport, self).__init__(number_of_class, flor_in_the_school)
        self.__subject = subject

    def subject(self):
        return self.__subject

    def class_info(self):
        return print(f"This is class of {self.__subject}, number of the classroom is {self.number_of_class()}, "
                     f"and you can find it on the {self.flor_in_the_school()} flor\n")


class ClassOfHistory(Classes):
    def __init__(self, number_of_class: int, flor_in_the_school: int, subject: str):
        super(ClassOfHistory, self).__init__(number_of_class, flor_in_the_school)
        self.__subject = subject

    def subject(self):
        return self.__subject

    def class_info(self):
        return print(f"This is class of {self.__subject}, number of the classroom is {self.number_of_class()}, "
                     f"and you can find iе on the {self.flor_in_the_school()} flor\n")


if __name__ == '__main__':
    myFirstSchool = School(46, "Tatiana Dmytrivna", "Elena Volodymyrivna", 1200)
    print(myFirstSchool.school_bio())

    class_of_math = ClassOfMath(10, 1, "Math")
    class_of_sport = ClassOfSport(20, 2, "Sport")
    class_of_history = ClassOfHistory(30, 3, "History")

    class_of_math.class_info()
    class_of_sport.class_info()
    class_of_history.class_info()

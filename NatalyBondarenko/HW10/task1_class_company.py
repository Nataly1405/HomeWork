class Company:
    """
    The class Company constructor accepts the following information:
    company_name, company_products, number_of_employees and company_locations
    """

    def __init__(self, company_name: str, company_products: list, number_of_employees: int, company_locations: list):
        self.__company_name = company_name
        self.__company_products = company_products
        self.__number_of_employees = number_of_employees
        self.__company_locations = company_locations

    @property
    def company_name(self):
        """
        Method  getting the company's name
        """
        return self.__company_name.capitalize()

    @company_name.setter
    def company_name(self, new_company_name: str):
        """
        Method changing the company's name
        """
        if new_company_name:
            self.__company_name = new_company_name
        else:
            print('Empty value is not supported for company name')

    @company_name.deleter
    def company_name(self):
        """
        method will protect code against class design break
        """
        pass

    @property
    def company_products(self):
        """
        Method getting list of the company's products
        """
        return self.__company_products

    @company_products.setter
    def company_products(self, new_company_product: str):
        """
        Method to update the company products
        """
        if new_company_product in self.__company_products:
            print(f"{new_company_product} is already in the company products list")
        elif not new_company_product:
            print('Empty value is not supported for company product')
        else:
            self.__company_products.append(new_company_product)

    def product_to_remove(self, product_to_remove: str):
        """
        Method to remove the company products
        """
        if product_to_remove in self.__company_products:
            return self.__company_products.remove(product_to_remove)
        else:
            print(f'{product_to_remove} can not be found in company product list')

    @property
    def number_of_employees(self):
        """
        Method getting the number of the company's employees
        """
        return self.__number_of_employees

    @number_of_employees.setter
    def number_of_employees(self, new_employees: int):
        """
        Method to update the number of the company's employees
        """
        if new_employees < 1:
            print(f'{new_employees} unsupported number of employees')
        else:
            self.__number_of_employees += new_employees

    def dismissal_employees(self, dismissal_employees: int):
        """
        Method to dismissal number of company employees
        """
        if dismissal_employees < 1:
            print('the number of dismissed employees cannot be less than 1')
        else:
            self.__number_of_employees = self.__number_of_employees - dismissal_employees

    @property
    def company_locations(self):
        """
        Method getting the list of the company locations
        """
        return self.__company_locations

    @company_locations.setter
    def company_locations(self, new_company_location: str):
        """
        Method to update the list of the company locations
        """
        if new_company_location in self.__company_locations:
            print(f"{new_company_location} is already in the company location list")
        elif not new_company_location:
            print('Empty value is not supported for company location')
        else:
            self.__company_locations.append(new_company_location)

    def location_to_remove(self, location_to_remove: str):
        """
        Method to remove the company products
        """
        if location_to_remove in self.__company_locations:
            return self.__company_locations.remove(location_to_remove)
        else:
            print(f'{location_to_remove} can not be found in company product list')


if __name__ == '__main__':
    my_company_Dell = Company('Dell', ['Computer', 'Mouse', 'Keyboard'], 150000,
                              ['Toronto', 'Bangkok', 'Kiev'])

    my_company_Dell.company_name = 'samsung'
    print(my_company_Dell.company_name)
    my_company_Dell.company_name = ''
    print(my_company_Dell.company_name)
    del my_company_Dell.company_name
    print(my_company_Dell.company_name)

    my_company_Dell.company_products = 'Camera'
    print(my_company_Dell.company_products)
    my_company_Dell.company_products = ''
    print(my_company_Dell.company_products)
    my_company_Dell.product_to_remove('Camera')
    print(my_company_Dell.company_products)

    my_company_Dell.number_of_employees = 100
    my_company_Dell.number_of_employees = 0
    print(my_company_Dell.number_of_employees)

    my_company_Dell.company_locations = 'Jerusalem'
    my_company_Dell.company_locations = 'Kiev'
    print(my_company_Dell.company_locations)
    my_company_Dell.company_locations = ''
    print(my_company_Dell.company_locations)


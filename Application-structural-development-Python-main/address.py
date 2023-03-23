class Address(object):
    """
    Class used to represent an address
    """
    def __init__(self, neighborhood: str = "Neighborhood", street: str = "Street", building: str = "Building",
                 city: str = "City", department: str = "Department", postal_code: str = "Postal code"):
        """ Address constructor object.
        :param neighborhood: neighborhood of address.
        :type neighborhood: str
        :param street: street number of address.
        :type street: str
        :param building: building's name of address.
        :type building: str
        :param city: city of address.
        :type city: str
        :param department: department of address.
        :type department: str
        :param postal_code: postal code of address.
        :type postal_code: str
        :returns: Address object
        :rtype: Address
        """
        self._neighborhood = neighborhood
        self._street = street
        self._building = building
        self._city = city
        self._department = department
        self._postal_code = postal_code

    @property
    def neighborhood(self) -> str:
        """ Returns neighborhood of the address.
          :returns: neighborhood of address.
          :rtype: str
        """
        return self._neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood: str):
        """ The neighborhood of the address.
        :param neighborhood: neighborhood of address.
        :type: str
        """
        self._neighborhood = neighborhood

    @property
    def street(self) -> str:
        """ Returns street of the address.
          :returns: street of address.
          :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street: str):
        """ The street of the address.
        :param street: street of address.
        :type: str
        """
        self._street = street

    @property
    def building(self) -> str:
        """ Returns building of the address.
          :returns: building of address.
          :rtype: str
        """
        return self._building

    @building.setter
    def building(self, building: str):
        """ The building of the address.
        :param building: building of address.
        :type: str
        """
        self._building = building

    @property
    def city(self) -> str:
        """ Returns city of the address.
          :returns: city of address.
          :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """ The city of the address.
        :param city: city of address.
        :type: str
        """
        self._city = city

    @property
    def department(self) -> str:
        """ Returns department of the address.
          :returns: department of address.
          :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department: str):
        """ The department of the address.
        :param department: department of address.
        :type: str
        """
        self._department = department

    @property
    def postal_code(self) -> str:
        """ Returns postal code of the address.
          :returns: postal code of address.
          :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code: str):
        """ The postal code of the address.
        :param postal_code: postal_code of address.
        :type: str
        """
        self._postal_code = postal_code

    def __str__(self):
        """ Returns string representation of the Address.
          :returns: string address
          :rtype: str
        """
        return '(Neighborhood: {0}, Street: {1}, Building: {2}, City: {3}, Department: {4}, Postal code: {5})'\
            .format(self.neighborhood, self.street, self.building, self.city, self.department, self.postal_code)

    def __eq__(self, other):
        """
        Determines whether two Address instances are equal by comparing their attribute values.
        :param other: The other Address instance to compare to.
        :type other: Address
        :return: True if the two instances are equal, False otherwise.
        :rtype: bool
        """
        if isinstance(other, Address):
            return (
                    self.neighborhood == other.neighborhood and
                    self.street == other.street and
                    self.building == other.building and
                    self.city == other.city and
                    self.department == other.department and
                    self.postal_code == other.postal_code
            )
        return False


if __name__ == '__main__':

    address_1 = Address(neighborhood="Parque Heredia", street="35", building="Salamandra", city="Cartagena",
                        department="Bolivar", postal_code="13001")
    print(address_1)
    address_1.street = "39"
    print(address_1)

    address_2 = Address()
    print(address_2)

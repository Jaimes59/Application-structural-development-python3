from validation import is_int, is_greater_than_zero


class Package(object):
    """
    Class used to represent a Package
    """
    W_GR_100 = 1.0

    def __init__(self, id_package: int = 0, weight: float = 0.1, description: str = 'Description', cost: float = 0.1):
        """ Package constructor object.
        :param id_package: id of package.
        :type id_package: int
        :param weight: weight of the package in kg.
        :type weight: float
        :param description: description of the package.
        :type description: str
        :param cost: cost per gram.
        :type cost: float
        :returns: Package object
        :rtype: Package
        """
        if is_int(id_package):
            self._id_package = id_package
        else:
            raise TypeError("The id package should be an integer")

        if is_greater_than_zero(weight):
            self._weight = weight
        else:
            raise TypeError("The weight should be greater than zero")

        self._description = description

        if is_greater_than_zero(cost):
            self._cost = cost
        else:
            raise TypeError("The cost should be greater than zero")

    @property
    def id_package(self) -> int:
        """ Returns id package of the package.
          :returns: id of package.
          :rtype: int
        """
        return self._id_package

    @id_package.setter
    def id_package(self, id_package: int):
        """ The id of the package.
        :param id_package: id of package.
        :type: int
        """
        self._id_package = id_package

    @property
    def weight(self) -> float:
        """ Returns weight of the package.
        :return: weight of the package in kg.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        """ The weight of the package in kg.
        :param weight: weight of package in kg.
        :type: float
        """
        self._weight = weight

    @property
    def description(self) -> str:
        """ Returns description of the package.
        :return: description of the package.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """ The description of the package.
        :param description: description of the package.
        :type: str
        """
        self._description = description

    @property
    def cost(self) -> float:
        """ Returns cost per gram of the package.
        :return: cost per gram of the package.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost: float):
        """ The cost of the package per gram
        :param cost: cost per gram of the package.
        :type: float
        """
        self._cost = cost

    def calculate(self) -> float:
        """ Calculate shipping cost of package.
        :returns: shipping cost
        :rtype: float
        """
        return (self.weight * 1000) * (Package.W_GR_100 * self.cost)

    def __str__(self):
        """ Returns string representation of the package.
          :returns: string package
          :rtype: str
        """
        return '(Id package: {0}, Weight: {1}, Description: {2}, Cost: {3}, Shipping cost: {4})'\
            .format(self.id_package, self.weight, self.description, self.cost, self.calculate())

    def __eq__(self, other):
        """
        Determines whether two Package instances are equal by comparing their attribute values.
        :param other: The other Package instance to compare to.
        :type other: Package
        :return: True if the two instances are equal, False otherwise.
        :rtype: bool
        """
        if isinstance(other, Package):
            return (
                    self.id_package == other.id_package and
                    self.weight == other.weight and
                    self.description == other.description and
                    self.cost == other.cost
            )
        return False


if __name__ == '__main__':

    package_1 = Package(id_package=73577376, weight=2, description="shoes", cost=5)
    print(package_1)
    package_1.weight = 5
    print(package_1)

    package_2 = Package()
    print(package_2)

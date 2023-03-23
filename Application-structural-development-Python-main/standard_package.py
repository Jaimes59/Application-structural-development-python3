from package import Package


class StandardPackage(Package):
    """
    Class used to represent a standard package, inheriting from Package class
    """
    TWO_DAY_SHIPPING_FEE = 15000.0

    def __init__(self, id_package: int = 0, weight: float = 0.001, description: str = 'Description', cost: float = 0.1):
        """ Standard Package constructor object.
        :param id_package: id of package.
        :type id_package: int
        :param weight: weight of the package in kg.
        :type weight: float
        :param description: description of the package.
        :type description: str
        :param cost: cost per gram.
        :type cost: float
        :returns: Standard Package object
        :rtype: StandardPackage
        """
        super().__init__(id_package, weight, description, cost)
        self.two_day_shipping_fee = StandardPackage.TWO_DAY_SHIPPING_FEE

    def calculate(self) -> float:
        """
        Calculates the total cost of shipping for a standard package
        :return: the total shipping cost
        """
        return (self.weight * 1000) * (Package.W_GR_100 * self.cost) + self.two_day_shipping_fee

    def __str__(self):
        """ Returns string representation of the package.
          :returns: string package
          :rtype: str
        """
        return '(Id package: {0}, Weight: {1}, Description: {2}, Cost: {3}, Fee for 2 days shipping {4}, ' \
               'Shipping cost: {5})'.format(self.id_package, self.weight, self.description, self.cost,
                                            self.two_day_shipping_fee, self.calculate())

    def __eq__(self, other):
        """
        Determines whether two StandardPackage instances are equal by comparing their attribute values.
        :param other: The other StandardPackage instance to compare to.
        :type other: StandardPackage
        :return: True if the two instances are equal, False otherwise.
        :rtype: bool
        """
        if isinstance(other, StandardPackage):
            return (
                    self.id_package == other.id_package and
                    self.weight == other.weight and
                    self.description == other.description and
                    self.cost == other.cost and
                    self.calculate() == other.calculate()
            )
        return False


if __name__ == '__main__':

    package_3 = StandardPackage(id_package=73577376, weight=3, description="shoes", cost=2)
    print(package_3)
    package_3.weight = 6
    print(package_3)

    package_2 = StandardPackage()
    print(package_2)

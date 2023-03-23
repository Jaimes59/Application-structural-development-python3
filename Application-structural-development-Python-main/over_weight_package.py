from package import Package
from validation import *


class OverWeightPackage(Package):
    """
    Class used to represent an over weight package, inheriting from Package class
    """

    def __init__(self, id_package: int = 0, weight: float = 0.001, description: str = 'Description',
                 cost: float = 0.1, over_weight: float = 0.1):
        """ Over Weight Package constructor object.
        :param id_package: id of package.
        :type id_package: int
        :param weight: weight of the package in kg.
        :type weight: float
        :param description: description of the package.
        :type description: str
        :param cost: cost per gram.
        :type cost: float
        :param over_weight: over weight of the package in gram.
        :type over_weight: float
        :returns: OverWeightPackage object
        :rtype: Over Weight Package
        """
        super().__init__(id_package, weight, description, cost)
        if is_greater_than_zero(over_weight):
            self._over_weight = over_weight
        else:
            raise TypeError("The over weight should be greater than zero")

    @property
    def over_weight(self) -> float:
        """ Returns over_weight of the package.
        :return: over_weight of the package in kg.
        :rtype: float
        """
        return self._over_weight

    @over_weight.setter
    def over_weight(self, over_weight: float):
        """ The over_weight of the package in kg.
        :param over_weight: over_weight of package in kg.
        :type: float
        """
        self._over_weight = over_weight

    def calculate(self) -> float:
        """
        Calculates the total cost of shipping for an over weight package
        :return: the total shipping cost
        """
        return ((self.weight + self.over_weight) * 1000) * Package.W_GR_100 * self.cost

    def __str__(self):
        """ Returns string representation of the package.
          :returns: string package
          :rtype: str
        """
        return '(Id package: {0}, Weight: {1}, Over Weight: {5}, Description: {2}, Cost: {3}, Shipping cost: {4})'\
            .format(self.id_package, self.weight, self.description, self.cost, self.calculate(), self.over_weight)

    def __eq__(self, other):
        """
        Determines whether two OverWeightPackage instances are equal by comparing their attribute values.
        :param other: The other OverWeightPackage instance to compare to.
        :type other: OverWeightPackage
        :return: True if the two instances are equal, False otherwise.
        :rtype: bool
        """
        if isinstance(other, OverWeightPackage):
            return (
                    self.id_package == other.id_package and
                    self.weight == other.weight and
                    self.description == other.description and
                    self.cost == other.cost and
                    self.calculate() == other.calculate() and
                    self.over_weight == other.over_weight
            )
        return False


if __name__ == '__main__':

    package_3 = OverWeightPackage(id_package=73577376, weight=3, description="shoes", cost=2, over_weight=1)
    print(package_3)
    package_3.weight = 6
    print(package_3)

    package_2 = OverWeightPackage()
    print(package_2)

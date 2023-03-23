from validation import *


class Payment(object):
    """
    Class used to represent a delivery
    """

    def __init__(self, payment_id: int = 0, payment_date: str = "Payment date", payment_method: str = "Payment method",
                 amount: float = 0.1):
        """ Payment constructor object.
        :param payment_id:
        :type payment_id: int
        :param payment_date:
        :type payment_date: str
        :param payment_method:
        :type payment_method: str
        :param amount:
        :type amount: float
        :returns: Payment object
        :rtype: Payment
        """
        self._payment_id = payment_id
        self._payment_date = payment_date
        self._payment_method = payment_method
        if is_greater_than_zero(amount):
            self._amount = amount
        else:
            raise TypeError("The amount should be greater than zero")

    @property
    def payment_id(self) -> int:
        """ Returns id of the payment.
          :returns: id of payment.
          :rtype: int
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id: int):
        """ The id of the payment.
        :param payment_id: id of payment.
        :type: int
        """
        self._payment_id = payment_id

    @property
    def payment_date(self) -> str:
        """ Returns date of the payment.
          :returns: date of payment.
          :rtype: str
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date: str):
        """ The date of the payment.
        :param payment_date: date of payment.
        :type: str
        """
        self._payment_date = payment_date

    @property
    def payment_method(self) -> str:
        """ Returns payment method of the payment.
          :returns: payment method of payment.
          :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method: str):
        """ The payment method of the payment.
        :param payment_method: payment method of payment.
        :type: str
        """
        self._payment_method = payment_method

    @property
    def amount(self) -> float:
        """ Returns amount of the payment.
        :return: amount of the payment.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """ The amount of the payment.
        :param amount: amount of the payment.
        :type: float
        """
        self._amount = amount

    def __str__(self):
        """ Returns string representation of the Payment.
          :returns: string payment
          :rtype: str
        """
        return '(Id payment: {0}, Payment date: {1}, Payment method: {2}, amount: {3}'\
            .format(self.payment_id, self.payment_date, self.payment_method, self.amount)

    def __eq__(self, other):
        """
        Determines whether two Package instances are equal by comparing their attribute values.
        :param other: The other Package instance to compare to.
        :type other: Package
        :return: True if the two instances are equal, False otherwise.
        :rtype: bool
        """
        if isinstance(other, Payment):
            return (
                    self.payment_id == other.payment_id and
                    self.payment_date == other.payment_date and
                    self.payment_method == other.payment_method and
                    self.amount == other.amount
            )
        return False


if __name__ == '__main__':

    payment_1 = Payment(payment_id=1234, payment_date="15 march", payment_method="credit card", amount=14000)
    print(payment_1)
    payment_1.payment_method = "cash"
    print(payment_1)

    payment_2 = Payment()
    print(payment_2)

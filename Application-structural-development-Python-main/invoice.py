from person import Person
from package import Package
from address import Address
from standard_package import StandardPackage
from over_weight_package import OverWeightPackage
from typing import List


class Invoice(object):
    """
    Class used to represent an invoice
    """

    def __init__(self, item=None, id_invoice: int = 0, client: Person = Person(), client_address: Address = Address(),
                 amount: float = 0.1, date: str = "Date"):
        """

        :param item:
        :type item: List
        :param id_invoice:
        :type id_invoice: int
        :param client:
        :type client: Person
        :param client_address: Address client
        :type client_address: Address
        :param amount:
        :type amount: float
        :param date:
        :type date: str
        :returns: invoice object
        :rtype: Invoice
        """

        self._id_invoice = id_invoice
        self._client = client
        self._client_address = client_address
        self._amount = amount
        self._date = date
        if item is None:
            self._item = []
        else:
            self._item = item

    @property
    def id_invoice(self) -> int:
        """ Returns id of the invoice.
          :returns: id of invoice.
          :rtype: int
        """
        return self._id_invoice

    @id_invoice.setter
    def id_invoice(self, id_invoice: int):
        """ The id of the invoice.
        :param id_invoice: id of invoice.
        :type: int
        """
        self._id_invoice = id_invoice

    @property
    def client(self) -> Person:
        """ Returns client of the invoice.
          :returns: client of invoice.
          :rtype: Person
        """
        return self._client

    @client.setter
    def client(self, client: Person):
        """ The client of the invoice.
        :param client: client of invoice.
        :type: Person
        """
        self._client = client

    @property
    def client_address(self) -> Address:
        """ Returns sender address of the invoice.
          :returns: sender address of invoice.
          :rtype: Address
        """
        return self._client_address

    @client_address.setter
    def client_address(self, client_address: Address):
        """ The sender address of the invoice.
        :param client_address: sender address of invoice.
        :type: Address
        """
        self._client_address = client_address

    @property
    def amount(self) -> float:
        """ Returns amount of the invoice.
        :return: amount of the invoice.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """ The amount of the invoice
        :param amount: amount of the invoice.
        :type: float
        """
        self._amount = amount

    @property
    def date(self) -> str:
        """ Returns date of the invoice.
          :returns: date of invoice.
          :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date: str):
        """ The date of the invoice.
        :param date: date of invoice.
        :type: str
        """
        self._date = date

    @property
    def item(self) -> List:
        """ Returns item of the delivery.
          :returns: item of Delivery.
          :rtype: List
        """
        return self._item

    @item.setter
    def item(self, item: List):
        """ The item of the delivery.
        :param item: item of delivery.
        :type: List
        """
        self._item = item

    def __str__(self):
        """ Returns string representation of the Invoice.
          :returns: string Invoice
          :rtype: str
        """
        list_item = ", ".join(str(element) for element in self.item)
        return '(id Invoice: {1}, Date: {2}, Client: {3}, Address client: {4}, items: {0}'\
            .format(list_item, self.id_invoice, self.date, self.client, self.client_address)

    def __eq__(self, other):
        """
        Determines whether two Invoice instances are equal by comparing their attribute values.
        :param other: The other Invoice instance to compare to.
        :type other: Invoice
        :return: True if the two instances are equal, False otherwise.
        :rtype: bool
        """
        if isinstance(other, Invoice):
            return (
                    self.item == other.item and
                    self.id_invoice == other.id_invoice and
                    self.date == other.date and
                    self.client == other.client and
                    self.client_address == other.client_address
            )
        return False


if __name__ == '__main__':
    person_1 = Person(id_person=73577376, name="Diego", last_name="Jaime", phone_number="3225555", email="diego@utb.co")

    address_1 = Address(neighborhood="Parque Heredia", street="35", building="Salamandra", city="Cartagena",
                        department="Bolivar", postal_code="13001")

    package_3 = StandardPackage(id_package=73577376, weight=3, description="shoes", cost=2)
    package_1 = OverWeightPackage(id_package=73577376, weight=2, description="shoes", cost=5, over_weight=1)

    all_package = [package_1, package_3]

    invoice_1 = Invoice(item=all_package, id_invoice=123456, date="26 march 2023", client=person_1,
                        client_address=address_1)
    print(invoice_1)
    invoice_1.client_address.street = "39"
    print(invoice_1)

    invoice_2 = Invoice()
    print(invoice_2)

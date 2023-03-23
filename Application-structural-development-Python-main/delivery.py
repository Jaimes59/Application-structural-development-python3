from person import Person
from address import Address
from package import Package
from standard_package import StandardPackage
from over_weight_package import OverWeightPackage
from payment import Payment
from invoice import Invoice
from typing import List


class Delivery(object):
    """
    Class used to represent a delivery
    """

    def __init__(self, item_list=None, id_delivery: int = 0, date: str = "Date", time: str = "Time",
                 sender: Person = Person(), receiver: Person = Person(), sender_address: Address = Address(),
                 receiver_address: Address = Address(), contact: Person = Person(),
                 payment_delivery: Payment = Payment(), invoice_delivery: Invoice = Invoice()):
        """ Delivery constructor object.
        :param item_list: items of delivery.
        :type item_list: List
        :param id_delivery: id delivery of delivery.
        :type id_delivery: int
        :param date: date of delivery.
        :type date: str
        :param time: time of delivery.
        :type time: str
        :param sender: sender of delivery.
        :type sender: Person
        :param receiver: receiver of delivery.
        :type receiver: Person
        :param sender_address: sender address of delivery.
        :type sender_address: Address
        :param receiver_address: receiver address of delivery.
        :type receiver_address: Address
        :param contact: contact person of delivery.
        :type contact: Person
        :param payment_delivery: payment information of delivery.
        :type payment_delivery: Payment
        :param invoice_delivery: Invoice information of delivery.
        :type invoice_delivery: Invoice
        :returns: Delivery object
        :rtype: Delivery
        """

        self._id_delivery = id_delivery
        self._date = date
        self._time = time
        self._sender = sender
        self._receiver = receiver
        self._sender_address = sender_address
        self._receiver_address = receiver_address
        self._contact = contact
        self._payment_delivery = payment_delivery
        self._invoice_delivery = invoice_delivery
        if item_list is None:
            self._item_list = []
        else:
            self._item_list = item_list

    @property
    def id_delivery(self) -> int:
        """ Returns id of the delivery.
          :returns: id of Delivery.
          :rtype: int
        """
        return self._id_delivery

    @id_delivery.setter
    def id_delivery(self, id_delivery: int):
        """ The id of the delivery.
        :param id_delivery: id of delivery.
        :type: int
        """
        self._id_delivery = id_delivery

    @property
    def date(self) -> str:
        """ Returns date of the delivery.
          :returns: date of Delivery.
          :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date: str):
        """ The date of the delivery.
        :param date: date of delivery.
        :type: str
        """
        self._date = date

    @property
    def time(self) -> str:
        """ Returns time of the delivery.
          :returns: time of Delivery.
          :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """ The time of the delivery.
        :param time: time of delivery.
        :type: str
        """
        self._time = time

    @property
    def sender(self) -> Person:
        """ Returns sender of the delivery.
          :returns: sender of Delivery.
          :rtype: Person
        """
        return self._sender

    @sender.setter
    def sender(self, sender: Person):
        """ The sender of the delivery.
        :param sender: sender of delivery.
        :type: Person
        """
        self._sender = sender

    @property
    def receiver(self) -> Person:
        """ Returns receiver of the delivery.
          :returns: receiver of Delivery.
          :rtype: Person
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: Person):
        """ The receiver of the delivery.
        :param receiver: receiver of delivery.
        :type: Person
        """
        self._receiver = receiver

    @property
    def sender_address(self) -> Address:
        """ Returns sender address of the delivery.
          :returns: sender address of Delivery.
          :rtype: Address
        """
        return self._sender_address

    @sender_address.setter
    def sender_address(self, sender_address: Address):
        """ The sender address of the delivery.
        :param sender_address: sender address of delivery.
        :type: Address
        """
        self._sender_address = sender_address

    @property
    def receiver_address(self) -> Address:
        """ Returns receiver address of the delivery.
          :returns: receiver address of Delivery.
          :rtype: Address
        """
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, receiver_address: Address):
        """ The receiver address of the delivery.
        :param receiver_address: receiver address of delivery.
        :type: Address
        """
        self._receiver_address = receiver_address

    @property
    def contact(self) -> Person:
        """ Returns contact of the delivery.
          :returns: contact of Delivery.
          :rtype: Person
        """
        return self._contact

    @contact.setter
    def contact(self, contact: Person):
        """ The contact of the delivery.
        :param contact: contact of delivery.
        :type: Person
        """
        self._contact = contact

    @property
    def payment_delivery(self) -> Payment:
        """ Returns payment information of the delivery.
          :returns: payment information of Delivery.
          :rtype: Payment
        """
        return self._payment_delivery

    @payment_delivery.setter
    def payment_delivery(self, payment_delivery: Payment):
        """ The payment information of the delivery.
        :param payment_delivery: payment information of delivery.
        :type: Payment
        """
        self._payment_delivery = payment_delivery

    @property
    def invoice_delivery(self) -> Invoice:
        """ Returns invoice information of the delivery.
          :returns: invoice information of Delivery.
          :rtype: Invoice
        """
        return self._invoice_delivery

    @invoice_delivery.setter
    def invoice_delivery(self, invoice_delivery: Invoice):
        """ The invoice information of the delivery.
        :param invoice_delivery: invoice information of delivery.
        :type: invoice_delivery
        """
        self._invoice_delivery = invoice_delivery

    @property
    def item_list(self) -> List:
        """ Returns item of the delivery.
          :returns: item of Delivery.
          :rtype: List
        """
        return self._item_list

    @item_list.setter
    def item_list(self, item_list: List):
        """ The item of the delivery.
        :param item_list: item of delivery.
        :type: List
        """
        self._item_list = item_list

    def __str__(self):
        """ Returns string representation of the Delivery.
          :returns: string Delivery
          :rtype: str
        """
        list_item = ", ".join(str(element) for element in self.item_list)
        return '(id delivery: {1}, Date: {2}, Time: {3}, sender: {4}, Sender address: {6}, Receiver: {5}, ' \
               'Receiver address: {7}), Contact: {8}, Payment information: {9}, invoice ID: {10}, items: {0}'\
            .format(list_item, self.id_delivery, self.date, self.time, self.sender, self.receiver, self.sender_address,
                    self.receiver_address, self.contact, self.payment_delivery, self.invoice_delivery.id_invoice)

    def __eq__(self, other):
        """
        Determines whether two Delivery instances are equal by comparing their attribute values.
        :param other: The other Delivery instance to compare to.
        :type other: Delivery
        :return: True if the two instances are equal, False otherwise.
        :rtype: bool
        """
        if isinstance(other, Delivery):
            return (
                    self.item_list == other.item_list and
                    self.id_delivery == other.id_delivery and
                    self.date == other.date and
                    self.time == other.time and
                    self.sender == other.sender and
                    self.receiver == other.receiver and
                    self.sender_address == other.sender_address and
                    self.receiver_address == other.receiver_address and
                    self.contact == other.contact and
                    self.payment_delivery == other.payment_delivery and
                    self.invoice_delivery == other.invoice_delivery
            )
        return False


if __name__ == '__main__':
    person_1 = Person(id_person=73577376, name="Diego", last_name="Jaime", phone_number="3225555", email="diego@utb.co")
    person_2 = Person(id_person=73577376, name="Juana", last_name="Rodino", phone_number="312555", email="Juana@utb.co")
    person_3 = Person(id_person=73577376, name="Wilmer", last_name="Granado", phone_number="300255", email="Wil@utb.co")

    address_1 = Address(neighborhood="Parque Heredia", street="35", building="Salamandra", city="Cartagena",
                        department="Bolivar", postal_code="13001")
    address_2 = Address(neighborhood="Parque Heredia", street="29", building="Coral", city="Cartagena",
                        department="Bolivar", postal_code="13001")

    payment_1 = Payment(payment_id=1234, payment_date="15 march", payment_method="credit card", amount=40000)

    package_2 = StandardPackage(id_package=73577376, weight=5, description="shoes", cost=2)
    package_1 = OverWeightPackage(id_package=73577376, weight=2, description="shoes", cost=5, over_weight=1)

    all_package = [package_1, package_2]

    invoice_1 = Invoice(item=all_package, id_invoice=123456, date="26 march 2023", client=person_1,
                        client_address=address_1)

    delivery_1 = Delivery(item_list=all_package, id_delivery=123456, date="26 march 2023", time="11:30 AM",
                          sender=person_1, receiver=person_2, sender_address=address_1, receiver_address=address_2,
                          contact=person_3, payment_delivery=payment_1, invoice_delivery=invoice_1)
    print(delivery_1)
    delivery_1.sender_address.street = "39"
    print(delivery_1)

    delivery_2 = Delivery()
    print(delivery_2)

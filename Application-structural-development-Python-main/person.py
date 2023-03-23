class Person(object):
    """
    Class used to represent a Person
    """

    def __init__(self, id_person: int = 0, name: str = 'Name', last_name: str = "LastName",
                 phone_number: str = "ContactNumber", email: str = "Email"):
        """ Person constructor object.
        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :param phone_number: Contact number of person.
        :type phone_number: str
        :param email: email of person.
        :type email: str
        :returns: Person object
        :rtype: Person
        """
        self._id_person = id_person
        self._name = name
        self._last_name = last_name
        self._phone_number = phone_number
        self._email = email

    @property
    def id_person(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_person

    @id_person.setter
    def id_person(self, id_person: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_person = id_person

    @property
    def name(self) -> str:
        """ Returns name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._name = name

    @property
    def last_name(self) -> str:
        """ Returns last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._last_name = last_name

    @property
    def phone_number(self) -> str:
        """ Returns contact number of the person.
        :return: number of person.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        """ The contact number of the person.
        :param phone_number: number of person.
        :return: str
        """
        self._phone_number = phone_number

    @property
    def email(self) -> str:
        """ Returns email of the person.
        :return: email of the person.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """ The email of the person.
        :param email: email of person.
        :return: str
        """
        self._email = email

    def __str__(self):
        """ Returns string representation of the person.
          :returns: string person
          :rtype: str
        """
        return '(Name: {1}, Last Name: {2}, id: {0}, Contact number: {3}, email: {4})'\
            .format(self.id_person, self.name, self.last_name, self.phone_number, self.email)

    def __eq__(self, other):
        """
        Determines whether two Person instances are equal by comparing their attribute values.
        :param other: The other Person instance to compare to.
        :type other: Person
        :return: True if the two instances are equal, False otherwise.
        :rtype: bool
        """
        if isinstance(other, Person):
            return (
                    self.id_person == other.id_person and
                    self.name == other.name and
                    self.last_name == other.last_name and
                    self.phone_number == other.phone_number and
                    self.email == other.email
            )
        return False


if __name__ == '__main__':

    diego = Person(id_person=73577376, name="Diego", last_name="Jaime", phone_number="3002225555", email="diego@utb.co")
    print(diego)
    diego.name = "Felipe"
    print(diego)

    juan = Person()
    print(juan)

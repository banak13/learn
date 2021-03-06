from faker import Faker

fake = Faker("pl_PL")


class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone_number}, {self.email_address}"

    def __repr__(self):
        return f"BaseContact(first_name={self.first_name} last_name={self.last_name}, phone_number={self.phone_number}, email_address={self.email_address})"

    def contact_priv(self):
        return f"Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}"

    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name), 1])


class BusinessContact(BaseContact):
    def __init__(self, company, position, business_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_phone_number = business_phone_number

    def __str__(self):
        return f"{self.company} {self.position}, {self.business_phone_number}"

    def __repr__(self):
        return f"BusinessContact(first_name={self.first_name} last_name={self.last_name}, email_address={self.email_address}, company={self.company} position={self.position}, business_phone_number={self.business_phone_number})"

    def contact_job(self):
        return f"Wybieram numer {self.business_phone_number} i dzwonię do {self.first_name} {self.last_name}, stanowisko: {self.position} z firmy {self.company}"

    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name), 1])


person_priv = BaseContact(
                          first_name=fake.first_name(),
                          last_name=fake.last_name(),
                          phone_number=fake.phone_number(),
                          email_address=fake.email())
person_business = BusinessContact(
                          first_name=fake.first_name(),
                          last_name=fake.last_name(),
                          phone_number=fake.phone_number(),
                          email_address=fake.email(),
                          company=fake.company(),
                          position=fake.job(),
                          business_phone_number=fake.phone_number()
                                  )

type_of_contact = ("private", "business")
how_many = 0
contact = ""
list_of_contacts = []


def create_contacts(type_of_contact, how_many):
    for i in range(how_many):
        if type_of_contact == "private":
            contact = BaseContact(first_name=fake.first_name(),
                                  last_name=fake.last_name(),
                                  phone_number=fake.phone_number(),
                                  email_address=fake.email())
            list_of_contacts.append(contact)

        elif type_of_contact == "business":
            contact = BusinessContact(first_name=fake.first_name(),
                                      last_name=fake.last_name(),
                                      phone_number=fake.phone_number(),
                                      email_address=fake.email(),
                                      company=fake.company(),
                                      position=fake.job(),
                                      business_phone_number=fake.phone_number())
            list_of_contacts.append(contact)
        else:
            exit(1)
    return list_of_contacts


print(create_contacts("private", 4))
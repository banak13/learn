from faker import Faker

class Contacts:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email

fake = Faker()

person = Contacts (
    first_name = fake.first_name(),
    last_name = fake.last_name(),
    company = fake.company(),
    position = "NONE"(),
    email = fake.email()
)


def create_contacts():
    for i in range(5):
        print(person.first_name(), person.last_name(), person.email())

create_contacts()
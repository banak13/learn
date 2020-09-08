class AdressContacts:
    def __init__(self, name, last_name, company, position, e_mail):
        self.name = name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.e_mail = e_mail

Vience = AdressContacts(
    name = 'Vince',
    last_name = 'J. Hiles',
    company = 'Gas Legion',
    position = 'Range manager',
    e_mail = 'VinceJHiles@rhyta.com'
)

Pawel = AdressContacts(
    name = 'Pawel',
    last_name = 'Banak',
    company = 'Zapsoft',
    position = 'IT_programmer',
    e_mail = 'banak13@o2.pl'
)

Mateusz = AdressContacts(
    name = 'Mateusz',
    last_name = 'Serafin',
    company = 'SKY',
    position = 'DataAdministrator',
    e_mail = 'nifares@wp.pl'
)

Agnieszka = AdressContacts(
    name = 'Agniszka',
    last_name = 'Bieszczad',
    company = 'Pasta Food',
    position = 'Supervisor',
    e_mail = 'agnes@wp.pl'
)

Iwona = AdressContacts(
    name = 'Iwona',
    last_name = 'Nifares',
    company = 'NONE',
    position = 'NONE',
    e_mail = 'iwex@wp.pl'
)

Mirek = AdressContacts(
    name = 'Mirosław',
    last_name = 'Zarzycki',
    company = 'self_employment',
    position = 'handlarz',
    e_mail = 'mirex@wp.pl'
)

def create_contacts():
    for AdressContacts in range(5):
        print(Mirek.name, Mirek.last_name, Mirek.company, Mirek.position, Mirek.e_mail)

print(create_contacts())

def __str__(self):
    return f'{self.name} {self.last_name} {self.company} {self.position} {self.e_mail}'


print(Mirek)
print(Agnieszka)
print(Pawel)
print(Iwona)
print(Mateusz)



business_cards = [Pawel, Mateusz, Agnieszka, Iwona, Mirek]
by_name = sorted(business_cards, key=lambda id: id.name)
by_last_name = sorted(business_cards, key=lambda id: id.name)
by_e_mail = sorted(business_cards, key=lambda id: id.e_mail)

print(by_name)
print(by_last_name)
print(by_e_mail)
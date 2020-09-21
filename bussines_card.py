



def create_contacts(card_type = input('Wpisz "private" lub "business"' , qnt = int())):
    if card_type == 'private':
        print(f"""{fake.first_name}+' '+{fake.last_name}\n
{fake.phone_number}\n
{fake.ascii_email}""")
    if card_type == 'business':
        print(f"""{fake.first_name}+' '+{fake.last_name}\n
{fake.company}\n
{fake.position}\n
{fake.phone_number}\n
{fake.ascii_email}""")
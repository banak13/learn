print("LISTA ZAKUPOW")

lista_zakupów = {
    "piekarnii": ["chleb", "bułki", "pączek"],
    "warzywniaka": ["marchew", "seler", "rukola"]
}

for sklep, rzeczy in lista_zakupów.items():
    rzeczy_tekst = ''
    for produkt in rzeczy:
        rzeczy_tekst += " {},".format(produkt.capitalize())
    print("Idę do {} i kupuje tam{}".format(sklep.capitalize(), rzeczy_tekst))
    x = 0

    for key in lista_zakupów.values():
        x += len(key)
print("W sumie kupuję {} produktów.".format(x))

zmiany zmiany zmiany


asdfafafdsfsfa
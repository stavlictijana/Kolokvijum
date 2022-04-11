lista = ['Namena prostora', 'QGIS', ('voda', 'reka'), ('putevi', 'drzavni'), ('zemljiste', 'livade'),
         ('vegetacija', 'sume'), ('poljoprivredno', 'obradivo'), ('izgradjeno', 'objekti'),
         ('industrija', 'teska')]
print(lista)

# promena layera po unosu atributa

promena = input('Unesite rec za promenu layera: ')

for x in range(len(lista)-2):
    atribut = input('Unesite atribut: ')
    lista[2+x] = promena + " " + atribut
    print(lista)

# ukoliko ne postoji atribut

x=str(input('Unesi atribut:'))
if x == lista:
    print('Postoji' + x)
else:
    print('Ne postoji')

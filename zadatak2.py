# prezime je Stavlic

lista = ['Namena prostora', 'QGIS', 'voda', 'putevi', 'zemljiste', 'vegetacija',
         'poljoprivredno', 'izgradjeno', 'industrija']

# broj indeksa je 96
t = 96 % 5
lista.pop(t)
lista.insert(t, 'Python programiranje')
print(lista)

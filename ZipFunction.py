names = ("Prachi","Bhushan","Prashan")
number = (1,2,3)

zipped = list(zip(names,number))
#zipped = dict(zip(names,number))
#zipped = set(zip(names,number))

for row in zipped:
    print(row)
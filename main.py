import random
import time

print('wybierz liczbe od 0 do 10 ')
time.sleep(5)

modulo = input('Czy twoja liczba jest parzysta? : ')
modulo.lower()
lower_higher = input('Czy twoja liczba jest większa od 5 ?: ')
lower_higher.lower()

while True:
    if modulo == 'tak':
        if lower_higher == 'tak' :
            guess = random.choice([6,8,10])
        elif lower_higher == 'nie':
            guess = random.choice(0,2,4)
    elif modulo == 'nie':
        if lower_higher == 'tak':
            guess = random.choice([7,9])
        elif lower_higher == 'nie':
            guess = random.choice([1,3,5])

    bol = input('Czy ' + str(guess) + ' to twoja liczba : ')
    bol = bol.lower()
    if bol == 'tak':
        print('Wygrana !')
        break
    elif bol == 'nie':
        continue
    else :
        print('Wpisz tylko tak lub nie. ')





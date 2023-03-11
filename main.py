import random
import time

print('wybierz liczbe od 0 do 10 ')
time.sleep(5)

while True:
    guess = random.randrange(11)

    bol = input('Czy ' + str(guess) + ' to twoja liczba :')
    bol = bol.lower()
    if bol == 'tak':
        print('Wygrana !')
        break
    elif bol == 'nie':
        continue
    else :
        print('Wpisz tylko tak lub nie. ')





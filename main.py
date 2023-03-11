import random
import time
import tkinter as tk

window = tk.Tk()
window.geometry('400x400')
label = tk.Label(text='Wybierz liczbe od 0 do 10')
time.sleep(5)



def newwindow():
    newwindow = tk.Toplevel(window)
    label = tk.Label(newwindow, text='Czy twoja liczba jest parzysta? ')
    label.pack()
    entry = tk.Entry(newwindow,width=40)
    entry.pack()
    button = tk.Button(command=secondwindow())
    button.pack()
def secondwindow():
    secondwindow = tk.Toplevel(newwindow)
    label = tk.Label(secondwindow,text='Czy twoja liczba jest większa od 5?')
    label.pack()
    entry1 = tk.Entry(secondwindow,width=40)
    entry1.pack()
    button1 = tk.Button(command=math)

def math():


modulo.lower()
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



window.mainloop()

print('Lenkaa')
if 3 > 2:
    print('fungujee')
else:
    print('nefunguje')

hlasitost = 153
if hlasitost < 20:
    print("Je to pomerne tiche.")
elif 20 <= hlasitost < 40:
    print("Je to fajn ako hudba na pozadi")
elif 40 <= hlasitost < 60:
    print("Super, pocujem vsetky detaily")
elif 60 <= hlasitost < 80:
    print("Fajn na party")
elif 80 <= hlasitost < 100:
    print("Trochu hlasne!")
else:
    print("Bolia ma usi! :(")
    print(hlasitost) 


def ahoj(meno):
    print('Ahoj ' + meno + '!')

dievcata = ['Katka', 'Kika', 'Zuza', 'Ola', 'Ty']
for meno in dievcata:
    ahoj(meno)
    print('Dalsie dievca')
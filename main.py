#BY THE VIGILANTE (AP)

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_special = ["/", "?", "!", ":", "-", ";", "."]

list_chiffre = []

def init():
    for i in range(10):
        list_chiffre.append(i)

password = []

def make(length=15):
    password = []
    chiffre_str = [str(x) for x in list_chiffre]
    
    for j in range(length):
        if j == 0:
            password.append(random.choice(ALPHABET))
        elif j == length - 1:
            password.append(random.choice(char_special))
        else:
            if random.choice([True, False]):
                password.append(random.choice(alphabet))
            else:
                password.append(random.choice(chiffre_str))

    shuffled_password = list(password)
    random.shuffle(shuffled_password)
    print(''.join(shuffled_password))

init()
make()

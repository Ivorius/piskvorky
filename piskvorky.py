import random

def vyhodnot(str):
    stri = str.lower()

    for i,c in enumerate(stri):
        if(c != "-" and (len(stri) > i+2) and stri[i+1] == c and stri[i+2] == c): 
            return c
        
    if('-' not in stri):
        return '!'
    else:
        return '-'


def tah(pole, cislo_policka, symbol):
    if(cislo_policka < 0 or cislo_policka > 19): 
        raise ValueError('Pozice v rozmezí 0 až 19 pouze')
    
    if(pole[cislo_policka] != '-'):
        raise ValueError('Na pozici {x} je již jiný symbol'.format(x=cislo_policka))
    
    nove_pole = pole[:cislo_policka] + symbol + pole[cislo_policka+1:]

    return nove_pole


def tah_hrace(pole):
    odpoved = input('Na jakou pozici chcete vložit symbol?')
    nastaveno = False

    while(nastaveno != True):
        try:
            cislo = int(odpoved)
            pole = tah(pole, cislo, 'x')
        except ValueError as e:
            s = str(e)
            print(s)
            odpoved = input('Na jakou pozici chcete vložit symbol?')
        else:
            nastaveno = True

    return pole


def tah_pocitace(pole):
    nastaveno = False

    while(nastaveno != True):
        try:
            cislo_policka = random.randrange(0,20)
            pole = tah(pole, cislo_policka, 'o')
        except ValueError:
           nastaveno = False
        else:
            nastaveno = True
   
    return pole

def nove_pole(integer):
    pole = '-' *  integer
    return pole


def piskvorky1d():
    pole = nove_pole(20)
    vitez = '-'

    i = 0
    while(vitez == '-'):
        i+=1
        if(i % 2 != 0):
            pole = tah_hrace(pole)
        else:
            print('Počítač táhne')
            pole = tah_pocitace(pole)

        print(pole)

        vitez = vyhodnot(pole)
       
        if(vitez == '!'):
            print('Je to plichta')
        elif(vitez != '-'):
            print('Vyhrává {x}'.format(x=vitez))



piskvorky1d()



import sys

def paverstiISkaiciu(ivestis):
    reiksme = None
    try: 
        reiksme = int(ivestis)
    except ValueError:
        pass
    return reiksme

def Intervalas(sk1, sk2):
    for i in range(sk1, sk2+1):
        if ArPirminis(i):
           print (i)

def ArPirminis(skaicius):
    if skaicius < 2:
        return 0
    for i in range(2, skaicius):
        if (skaicius%i) == 0:
            return False
    return True

print ("pirminių skaičių paieškos programa.")
print ("Programa ras pirminius skaičius nurodytame intervale.")
a = input ("Įveskite intervalo pradžią: ")
b = input ("Įveskite intervalo pabaigą: ")
skaicius1 = paverstiISkaiciu(a)

if skaicius1 == None:
    print ("Privaloma ivesti sveikaji skaiciu")
    sys.exit(0)
skaicius2 = paverstiISkaiciu(b)
if skaicius2 == None:
    print ("Privaloma ivesti sveikaji skaiciu")
    sys.exit(0)
if skaicius1<0:
    print("Privaloma ivesti teigiama skaiciu")
    sys.exit(0)
if skaicius1<0:
    print ("Privaloma ivesti teigiama skaiciu")
    sys.exit(0)
if skaicius1>skaicius2:
    print ("Privaloma ivesti antra skaiciu didesni uz pirma")
    sys.exit(0)

print ("Pirminių skaičių ieškome intervale [", a, ";", b, "]")
Intervalas(skaicius1, skaicius2)
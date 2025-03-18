import random

valik = ["kivi", "paber", "käärid"] #list võimalikest valikutest
tulemused = []  #list tulemuste jaoks appendi abil lisame tulemused listi
kellega = input("Kahe inimesega või robotiga? ").lower()    #küsime kas mängitakse kahe inimesega või robotiga lower() abil muudame vastuse väikesteks tähtedeks
viik = 0 
pobedy_mangija1 = 0
pobedy_mangija2 = 0

if kellega in ["kahe inimesega", "inimesega"]: #kui mängitakse kahe inimesega, siis küsime 2 mängijate nimed
    mangija = input("Sisesta nimi 1: ").title() #title() abil muudame esimese tähe suureks
    mangija2 = input("Sisesta nimi 2: ").title()
elif kellega in ["robotiga", "üksi", "robot"]: #kui mängitakse arvutiga, siis küsime ainult 1 mängija nime
    mangija = input("Sisesta nimi: ").title()
    mangija2 = "arvuti"  #mängija 2 on arvuti
else: 
    print("Proovi uuesti!")
    exit()

print("game start! Kirjutage 'exit', et lõpetada mäng.")
while True:
    try:
        valik1 = input(f"{mangija}, vali: kivi, paber või käärid (või 'exit' lõpetamiseks): ").lower() #küsime mängijalt valikut
        if valik1 == "exit":    #kui mängija kirjutab exit, siis lõpetame mängu
            break
        if valik1 not in valik: #kui kasutaja sisestab midagi muud kui kivi, paber või käärid, siis programm ütleb, et see on vale valik ja küsib uuesti
            print("Vale valik, proovi uuesti.")
            continue

        if mangija2 == "arvuti": #kui mängitakse arvutiga, siis arvuti valib suvaliselt kivi, paberi või käärid
            valik2 = random.choice(valik)
            print(f"Arvuti valis: {valik2}")
        else:
            valik2 = input(f"{mangija2}, vali: kivi, paber või käärid (või 'exit' lõpetamiseks): ").lower()
            if valik2 == "exit":
                break
            if valik2 not in valik: #kui kasutaja sisestab midagi muud kui kivi, paber või käärid, siis programm ütleb, et see on vale valik ja küsib uuesti
                print("Vale valik, proovi uuesti.")
                continue

        if valik1 == valik2: #kui mõlemad valivad sama, siis on viik
            voitja = "Viik"
            viik += 1
            print("Viik!")
        elif (valik1 == "kivi" and valik2 == "käärid") or \
             (valik1 == "käärid" and valik2 == "paber") or \
             (valik1 == "paber" and valik2 == "kivi"):
            pobedy_mangija1 += 1 #lisame võidu mängijale
            voitja = mangija
            print(f"{mangija} võitis!")
        else:
            pobedy_mangija2 += 1 #lisame võidu mängijale
            voitja = mangija2
            print(f"{mangija2} võitis!")
        
        tulemused.append(f"{mangija} valis {valik1}, {mangija2} valis {valik2}. Võitja: {voitja}") #lisame tulemused listi
    
    except:
        print("Viga, proovi uuesti.")

print("Kokkuvõte:")
print(f"{mangija} võite: {pobedy_mangija1}")
print(f"{mangija2} võite: {pobedy_mangija2}")
print(f"Viike: {viik}")
print("mang on lõpetatud! ty")

import random

valik = ["kivi", "paber", "käärid"]
tulemused = []  
kellega = input("Kahe inimesega või robotiga? ").lower()
viik = 0 
pobedy_mangija1 = 0
pobedy_mangija2 = 0

if kellega in ["kahe inimesega", "inimesega"]:
    mangija = input("Sisesta nimi 1: ").title()
    mangija2 = input("Sisesta nimi 2: ").title()
elif kellega in ["robotiga", "üksi", "robot"]:
    mangija = input("Sisesta nimi: ").title()
    mangija2 = "arvuti"
else: 
    print("Proovi uuesti!")
    exit()

print("Mäng alustati! Kirjutage 'exit', et lõpetada mäng.")

while True:
    try:
        valik1 = input(f"{mangija}, vali: kivi, paber või käärid (või 'exit' lõpetamiseks): ").lower()
        if valik1 == "exit":
            break
        if valik1 not in valik:
            print("Vale valik, proovi uuesti.")
            continue

        if mangija2 == "arvuti":
            valik2 = random.choice(valik)
            print(f"Robot valis: {valik2}")
        else:
            valik2 = input(f"{mangija2}, vali: kivi, paber või käärid (või 'exit' lõpetamiseks): ").lower()
            if valik2 == "exit":
                break
            if valik2 not in valik:
                print("Vale valik, proovi uuesti.")
                continue

        if valik1 == valik2:
            voitja = "Viik"
            viik += 1
            print("Viik!")
        elif (valik1 == "kivi" and valik2 == "käärid") or \
             (valik1 == "käärid" and valik2 == "paber") or \
             (valik1 == "paber" and valik2 == "kivi"):
            voitja = mangija
            pobedy_mangija1 += 1
            print(f"{mangija} võitis!")
        else:
            voitja = mangija2
            pobedy_mangija2 += 1
            print(f"{mangija2} võitis!")

        tulemused.append(f"{mangija} valis {valik1}, {mangija2} valis {valik2}. Võitja: {voitja}")

    except ValueError:
        print("Viga, proovi uuesti.")

print("Kokkuvõte:")
print(f"{mangija} võite: {pobedy_mangija1}")
print(f"{mangija2} võite: {pobedy_mangija2}")
print(f"Viike: {viik}")
print("mang on lopetatud! ty!")
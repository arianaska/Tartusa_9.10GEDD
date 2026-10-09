def ir_vesels_skaitlis(teksts):
    teksts = teksts.strip()
    if teksts.startswith("-") or teksts.startswith("+"):
        return teksts[1:].isdigit()
    return teksts.isdigit()


atlikums = 100

while True:
    print("\n1 — apskatīt atlikumu")
    print("2 — iemaksāt naudu")
    print("3 — izņemt naudu")
    print("4 — beigt darbu")

    izvele = input("Izvēlies darbību: ")

    if izvele == "1":
        print(f"Atlikums: {atlikums}")
    elif izvele == "2" or izvele == "3":
        summa_ievade = input("Ievadi summu: ")

        if not ir_vesels_skaitlis(summa_ievade):
            print("Kļūda: ievadi veselu skaitli.")
            continue

        summa = int(summa_ievade)

        if summa <= 0:
            print("Summai jābūt lielākai par 0.")
        elif izvele == "2":
            atlikums += summa
            print(f"Iemaksāti {summa}. Atlikums: {atlikums}")
        elif summa > atlikums:
            print("Kontā nav pietiekami daudz naudas.")
        else:
            atlikums -= summa
            print(f"Izņemti {summa}. Atlikums: {atlikums}")
    elif izvele == "4":
        print("Darbs pabeigts.")
        break
    else:
        print("Nezināma izvēle. Izvēlies skaitli no 1 līdz 4.")
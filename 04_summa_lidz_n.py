ievade = input("Ievadi pozitīvu veselu skaitli n: ").strip()
if ievade.isdigit():
    n = int(ievade)

    if n > 0:
        summa = 0
        skaitlis = 1

        # Pieskaita skaitļus no 1 līdz n.
        while skaitlis <= n:
            summa += skaitlis
            skaitlis += 1

        print(f"Skaitļu no 1 līdz {n} summa ir {summa}.")
    else:
        print("Kļūda: n jābūt pozitīvam skaitlim.")
else:
    print("Kļūda: ievadi veselu skaitli.")
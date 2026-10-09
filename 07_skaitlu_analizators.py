def ir_vesels_skaitlis(teksts):
    teksts = teksts.strip()
    if teksts.startswith("-") or teksts.startswith("+"):
        return teksts[1:].isdigit()
    return teksts.isdigit()


ievade = input("Cik skaitļus ievadīsi? ")

if not ir_vesels_skaitlis(ievade):
    print("Kļūda: ievadi veselu skaitli.")
elif int(ievade) < 0:
    print("Skaitļu skaits nevar būt negatīvs.")
else:
    daudzums = int(ievade)
    summa = 0
    pozitīvi = 0
    negatīvi = 0
    nulles = 0
    pāra = 0
    nepāra = 0

    for i in range(daudzums):
        while True:
            ievade = input(f"Ievadi {i + 1}. skaitli: ")
            if ir_vesels_skaitlis(ievade):
                skaitlis = int(ievade)
                break
            print("Kļūda: ievadi veselu skaitli.")

        summa += skaitlis

        if skaitlis > 0:
            pozitīvi += 1
        elif skaitlis < 0:
            negatīvi += 1
        else:
            nulles += 1

        if skaitlis % 2 == 0:
            pāra += 1
        else:
            nepāra += 1

    print(f"Summa: {summa}")
    print(f"Pozitīvi: {pozitīvi}, negatīvi: {negatīvi}, nulles: {nulles}")
    print(f"Pāra: {pāra}, nepāra: {nepāra}")

    if daudzums > 0:
        print(f"Vidējais aritmētiskais: {summa / daudzums}")
    else:
        print("Vidējo aprēķināt nevar, jo skaitļi netika ievadīti.")
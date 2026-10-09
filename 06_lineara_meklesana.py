def ir_vesels_skaitlis(teksts):
    teksts = teksts.strip()
    if teksts.startswith("-") or teksts.startswith("+"):
        return teksts[1:].isdigit()
    return teksts.isdigit()


skaitli = [4, 7, 2, 9, 7, 1]
ievade = input("Ievadi meklējamo skaitli: ")

if not ir_vesels_skaitlis(ievade):
    print("Kļūda: ievadi veselu skaitli.")
else:
    meklējamais = int(ievade)
    atrastie_indeksi = []

    for indekss in range(len(skaitli)):
        if skaitli[indekss] == meklējamais:
            atrastie_indeksi.append(indekss)

    if atrastie_indeksi:
        print(f"Pirmais indekss: {atrastie_indeksi[0]}")
        print(f"Visi atrastie indeksi: {atrastie_indeksi}")
    else:
        print("Nav atrasts")
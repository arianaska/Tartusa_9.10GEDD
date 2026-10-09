ievade = input("Ievadi veselu skaitli: ").strip()

if ievade.isdigit() or (
    ievade.startswith("-") and ievade[1:].isdigit()
):
    skaitlis = int(ievade)

    for reizinatajs in range(1, 11):
        print(f"{skaitlis} x {reizinatajs} = {skaitlis * reizinatajs}")
else:
    print("Kļūda: ievadi veselu skaitli.")
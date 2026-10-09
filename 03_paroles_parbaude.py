pareiza_parole = "67"
atlikušie_meginajumi = 3

while atlikušie_meginajumi > 0:
    parole = input("Ievadi paroli: ")

    if parole == pareiza_parole:
        print("Piekļuve atļauta")
        break

    atlikušie_meginajumi -= 1

    if atlikušie_meginajumi > 0:
        print(f"Nepareiza parole. Atlikuši mēģinājumi: {atlikušie_meginajumi}")
    else:
        print("Piekļuve bloķēta")
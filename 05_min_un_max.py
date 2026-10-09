def ir_vesels_skaitlis(teksts):
    teksts = teksts.strip()
    if teksts.startswith("-") or teksts.startswith("+"):
        return teksts[1:].isdigit()
    return teksts.isdigit()


ievade = input("Cik skaitļus ievadīsi? ")

if not ir_vesels_skaitlis(ievade):
    print("Kļūda: ievadi veselu skaitli.")
elif int(ievade) <= 0:
    print("Skaitļu skaitam jābūt lielākam par 0.")
else:
    daudzums = int(ievade)

    for i in range(daudzums):
        while True:
            ievade = input(f"Ievadi {i + 1}. skaitli: ")
            if ir_vesels_skaitlis(ievade):
                skaitlis = int(ievade)
                break
            print("Kļūda: ievadi veselu skaitli.")

        if i == 0:
            mazākais = skaitlis
            lielākais = skaitlis
        else:
            if skaitlis < mazākais:
                mazākais = skaitlis
            if skaitlis > lielākais:
                lielākais = skaitlis

    print(f"Mazākais skaitlis: {mazākais}")
    print(f"Lielākais skaitlis: {lielākais}")
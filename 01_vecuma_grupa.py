vecums = int(input("Ievadi savu vecumu: ").strip())

if vecums < 0:
    print("Kļūda vecumsnevar būt negatīvs.")
elif vecums <= 12:
    print("Bērns")
elif vecums <= 17:
    print("Pusaudzis")
elif vecums <= 64:
    print("Pieaugušais")
else:
    print("seniors")


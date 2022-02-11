summe = 0

for feld in range(64):
    reiskorn = 2**feld
    summe = summe + reiskorn
    print("feld {} = {:>30,} Reiskoerner und damit insgesammt {:>30,} Reiskoerner".format(feld+1,reiskorn,summe))
    # Der Doppelpunkt bedeuter Komma setzen
    Gewicht=(summe*0.02)/(10**6)
    print("Reiskoerner in Tonnen {:,.0f}".format(Gewicht)) #0f bedeutet 0 Nachkomma stellen bei einer float 
import matplotlib.pyplot as plt
feldliste = [] #Leere Liste anlegen



summe = 0

    for feld in range(64):
        reiskorn = 2**feld
        feldliste.append(reiskorn) #append = anhängen der liste wird also immer der aktuelle wert zugewiesen
        summe = summe + reiskorn
        print("feld {} = {:>30,} Reiskoerner und damit insgesammt {:>30,} Reiskoerner".format(feld+1,reiskorn,summe))
        # Der Doppelpunkt bedeuter Komma setzen
        Gewicht=(summe*0.02)/(10**6)
        print("Reiskoerner in Tonnen {:,.0f}".format(Gewicht)) #0f bedeutet 0 Nachkomma stellen bei einer float 

  plt.plot(feldliste)
  plt.show()
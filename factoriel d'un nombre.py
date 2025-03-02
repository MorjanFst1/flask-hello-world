try:# executer le code et tester les erreurs
    N=int(input("entrer un nombre :\n"))
    S=1
    for i in range(1,N+1):
        S=i*S
    print("le factorielle de ",N ,"est" ,S)
except:# traiter les erreurs
    print("vous devez entrer un nombre")
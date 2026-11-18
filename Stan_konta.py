stan_konta = input("Podaj stan konta: ")
print(stan_konta)

dzienna_stawka = input("Ile zarabiasz dziennie: ")

naile = input("Wybierz na jaki okres mam przeliczyc twoj stan konta (tydzien, miesiac, rok): ")

if naile == "tydzien":
    calkowity_stan_konta = float(stan_konta) + (float(dzienna_stawka) * 7)
    print("Po tygodniu na twoim kondzie bedzie ", calkowity_stan_konta  )
elif naile == "miesiac":
    calkowity_stan_konta = float(stan_konta) + (float(dzienna_stawka) * 30)
    print("Po miesiacu na twoim kondzie bedzie", calkowity_stan_konta  )
elif naile == "rok":
    calkowity_stan_konta = float(stan_konta) + (float(dzienna_stawka) * 365)
    print("Po roku na twoim kondzie bedzie", calkowity_stan_konta  )

dodatkowe = input("dostajesz jakies napiwki lub dodatki do pensji, tak lub nie ?")

if dodatkowe == "nie":
    print("To twoj stan konta bedzie wynosil:",calkowity_stan_konta  )
    
elif dodatkowe == "tak":
    ile_okolo = float(input("Ile dodatkowo zazwyczaj dostajesz na dzien?"  ))
    if naile == "tydzien":
        print("Zarobisz okolo", (calkowity_stan_konta) + ile_okolo * 7 )
    elif naile == "miesiac":
        print("Zarobisz okolo", (calkowity_stan_konta) + ile_okolo * 30)
    elif naile == "rok":
        print("Zarobisz okolo", (calkowity_stan_konta) + ile_okolo * 365)
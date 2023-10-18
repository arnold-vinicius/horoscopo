dia = input("Dia em que você nasceu\n")
mes = input("Mes em que você nasceu\n")

if dia >= "21" and mes == "3" or dia <= "19" and mes == "4":
    print("Aries")
else:
    if dia >= "20" and mes == "4" or dia <= "20" and mes == "5":
        print("Touro")
    else:
        if dia >= "21" and mes == "5" or dia <= "20" and mes == "6":
            print("Gêmeos")
        else:
            if dia >= "22" and mes == "6" or dia <= "22" and mes == "7":
                print("Cancer")
            else:
                if dia >= "23" and mes == "7" or dia <= "22" and mes == "8":
                    print("Leão")
                else:
                    if dia >= "23" and mes == "8" or dia <= "22" and mes == "9":
                        print("Virgem")
                    else:
                        if dia >= "23" and mes == "9" or dia <= "22" and mes == "10":
                            print("Libra")
                        else:
                            if dia >= "23" and mes == "10" or dia <= "21" and mes == "11":
                                print("Escorpião")
                            else:
                                if dia >= "22" and mes == "11" or dia <= "21" and mes == "12":
                                    print("Sagitário")
                                else:
                                    if dia >= "22" and mes == "12" or dia <= "19" and mes == "1":
                                        print("Capricornio")
                                    else:
                                        if dia >= "20" and mes == "1" or dia <= "18" and mes == "2":
                                            print("Aquario")
                                        else:
                                            if dia >= "19" and mes == "2" or dia <= "20" and mes == "3":
                                                print("Peixes")
                                            else:
                                                print("Erro")

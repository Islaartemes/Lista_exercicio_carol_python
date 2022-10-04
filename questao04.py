from calendar import isleap

ano = int (input("Informe o ano que deseja: "))

if isleap(ano):
    print ("O ano é bissexto!")

else:
    print("O ano não é bissexto!")


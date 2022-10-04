nota1 = float(input ("Digite a primneira nota: "))
nota2 = float(input ("Digite a seguda nota: "))
nota3 = float(input ("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:

    print("Aprovado com distinção")


elif media >= 7:
    print("Aprovado")

else:
    print("Reprovado")

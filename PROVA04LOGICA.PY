inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

soma_pares = 0
tem_par = False

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
        tem_par = True
else:
    if not tem_par:
        print("Não há números pares nesse intervalo.")

if tem_par:
    print("A soma dos números pares é:", soma_pares)

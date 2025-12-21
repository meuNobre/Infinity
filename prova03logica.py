numero_correto = 7


tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1

    if palpite == numero_correto:
        print("Parabéns! Você acertou!")
        break  
else:
    
    print("Suas tentativas acabaram. Tente novamente da próxima vez!")

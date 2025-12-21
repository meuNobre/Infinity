numero_alunos = int(input("Digite o número de alunos: "))

soma_geral = 0

for _ in range(numero_alunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)
    
    media = sum(notas) / 3
    soma_geral += media
    
    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"
    
    print(f"\nAluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}\n")

media_geral = soma_geral / numero_alunos
print(f"Média geral da turma: {media_geral:.2f}")

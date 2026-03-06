## cálculo de média e situação final de alunos

def calcular_mencao(notas):
    return sum(notas) / len(notas)


def calcular_situacao(media):
    if media >= 7:
        return ("APROVADO!")
    elif media >= 5:
        return ("RECUPERAÇÃO")
    else:
        return ("REPROVADO")


alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nAluno {i+1}")
    nome = input("Nome: ")

    notas = []
    for j in range(3):
        nota = float(input(f"Nota {j+1}: "))
        notas.append(nota)

    media = calcular_mencao(notas)
    situacao = calcular_situacao(media)

    alunos.append({
        "nome": nome,
        "media": media,
        "situacao": situacao
    })

print("\n======== RESULTADO FINAL =========")
for aluno in alunos:
    print(f"\nAluno: {aluno['nome']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")

from pathlib import Path


def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um valor numérico válido.")


def main():
    alunos = []

    for numero_aluno in range(1, 4):
        nome = input(f"Nome do aluno {numero_aluno}: ").strip()
        while not nome:
            print("O nome não pode ficar vazio.")
            nome = input(f"Nome do aluno {numero_aluno}: ").strip()

        notas = [ler_nota(numero) for numero in range(1, 5)]
        media = sum(notas) / len(notas)

        if media >= 7:
            situacao = "Aprovado(a)"
        elif media >= 5:
            situacao = "Em recuperação"
        else:
            situacao = "Reprovado(a)"

        alunos.append((nome, media, situacao))

    aprovados = sum(1 for _, _, situacao in alunos if situacao == "Aprovado(a)")
    resumo = ["Resumo dos alunos:"]
    resumo.extend(
        f"{nome}: média {media:.2f} - {situacao}"
        for nome, media, situacao in alunos
    )
    resumo.append(f"Alunos aprovados: {aprovados} de 3")

    texto_resumo = "\n".join(resumo)
    print(f"\n{texto_resumo}")

    caminho_boletim = Path(__file__).with_name("boletim.txt")
    caminho_boletim.write_text(f"{texto_resumo}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
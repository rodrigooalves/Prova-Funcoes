def calcular_media(notas):
    if len(notas) == 0:
        return 0  # Retorna 0 se não houver notas

    soma = sum(notas)
    media = soma / len(notas)
    return media

def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    notas = []
    while True:
        try:
            nota = float(input("Digite uma nota (ou qualquer valor não numérico para calcular a média): "))
            notas.append(nota)
        except ValueError:
            break  # Sai do loop se um valor não numérico for inserido

    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    print(f"Média do aluno: {media:.2f}")
    print(f"Situação do aluno: {situacao}")

if __name__ == "__main__":
    main()

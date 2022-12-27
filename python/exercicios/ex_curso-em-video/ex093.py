#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

def main():
    jogador = dict()
    jogador['nome'] = input("Nome do jogador: ")
    qtdPartidas = int(input("Quantidade de partidas jogadas: "))
    jogador['gols'] = list()
    for i in range(qtdPartidas):
        jogador['gols'].append(int(input(f"gols na partida {i+1}: ")))
    jogador['totalGols'] = sum(jogador['gols'])
    print("\n\n", jogador, "\n\n")
    print(f"Na posição nome contem o valor: {jogador['nome']}")
    print(f"Na posição gols contem o valor: {jogador['gols']}")
    print(f"Na posição TotalGols contem o valor: {jogador['totalGols']}")
    print("\n\n")
    print(f"O jogador {jogador['nome']} jogou {qtdPartidas} de partidas: ")
    for i in range(qtdPartidas):
        print(f"=> Na partida {i+1} ele fez {jogador['gols'][i]} gols ")
    print(f"No total o jogador fez {jogador['totalGols']} gols ")


if __name__=="__main__":
    main()

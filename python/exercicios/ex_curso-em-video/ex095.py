#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
def main():
    time = list()
    op = 's'
    while(op in "sS"):
        jogador = dict()
        jogador['nome'] = input("Nome do jogador: ")
        qtdPartidas = int(input("Quantidade de partidas jogadas: "))
        jogador['gols'] = list()
        for i in range(qtdPartidas):
            jogador['gols'].append(int(input(f"gols na partida {i+1}: ")))
        jogador['totalGols'] = sum(jogador['gols'])
        time.append(jogador)
        del(jogador)
        while(True):
            op = input("Deseja adicionar outro jogador?[S/N]: ")
            if op in "sSNn":
                break
            print("Opção invalida")
    print("Cod Nome             gols                 Total")
    print("+="*30)
    for i, v in enumerate(time):
        print(f"{i:2} {v['nome']:16} {str(v['gols']):<20} {v['totalGols']}")
    cod = 0
    while(True):
        cod = int(input("Monstrar dados de qual jogador?[999 para sair]"))
        if cod == 999:
            break
        print(f"O jogador {time[cod]['nome']} fez:")
        for i, v in enumerate(time[cod]['gols']):
            print(f"{v:2} gols no jogo {i+1}.")
        print("-"*30)   
 
if __name__ == "__main__":
    main()

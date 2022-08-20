#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.(substitui chapecoense pelo flamengo)
def main():
    times = ("Palmeiras", "Flamengo", "Corinthians", "Fluminense", "Athletico", "Internacional", "Atlético-MG", "América-MG", "Bragantino", "Santos", "Goiás", "São Paulo", "Botafogo", "Ceará", "Fortaleza", "Cuiabá", "Avaí", "Coritiba", "Atlético-GO", "Juventude")
    print(f"Tabela do brasileirão: {times}")
    print("--"*40)
    print(f"os 5 primeiros colocados são: {times[:5]}")
    print("--"*40)
    print(f"Os 4 ultimos são {times[-4:]}")
    print("--"*40)
    print(f"Os times em ordem alfabetica: {sorted(times)}")
    print("--"*40)
    print(f"O Flamengo está na {times.index('Flamengo')+1}º posição ")

if __name__ == "__main__":
    main()
import urllib.request
def main():
    try:
        site = urllib.request.urlopen('http://www.pudim.com.br')
    except:
        print("Não foi possivel acessar o pudim")
    else:
        print("O site do pudim está acessivel")

if __name__=="__main__":
    main()
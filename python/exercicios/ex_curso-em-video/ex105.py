def passou(n):
    """
        n: medía do aluno
        Retorna: Se o aluno está aprovado ou reprovado
    """
    if n >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

def notas(*notas, sit=False):
    """
        notas: Todas as notas do aluno
        sit: se deseja que a situação seja calculada
        Retorna: Um dicionario com Total de notas, a maior nota, a menor nota, a medía e se requisistado a situação
    """
    resp = dict()
    resp['Total'] = len(notas)
    resp['Maior'] = max(notas)
    resp['Menor'] = min(notas)
    resp['Medía'] = round((sum(notas)/len(notas)), 2)
    if sit:
        resp['Situação'] = passou(resp['Medía'])
    return resp

def main():
    resp = notas(6.0, 10.0, 5.5, 8.0, sit=True)
    print(resp)

if __name__=="__main__":
    main()
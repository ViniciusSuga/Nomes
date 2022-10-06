import re
def mais_curto(lista_de_nomes):
    global lista
    nome_list = []
    for i in string(lista_de_nomes): #A func 'string' retorna a lista só com strings
        if regex(i):
            nome_list.append(regex(i)) #A func 'Regex' retorna apenas os nomes sem número e que começam com maiúsculo
            nome = nome_list[0]
            for i in nome_list:
                if len(i)<len(nome):
                    nome = i
    print (nome)

def string(nome_lista):
    for i in nome_lista:
        if type(i) != str:
            nome_lista.remove(i)
    return (nome_lista)

def regex(nomes): #Vai receber uma só string
    nomes.split(' ')
    if len(nomes)<=1:
        return False
    else:
        x = re.search("^[a-z]", nomes) 
        if x:
            return False#Retorna False a str que começar com minusculo
        x = re.search("[0-9]", nomes)
        if x:
            return False #Retorna False a str que tem números
        else:
            return nomes

lista = ['Predro 123 Certezas', 'Kylian Pedro Carlos', 'Yassna Parracho Pequeno', 'Cristina Cartaxo Teodoro', 'dfsjaiodjiaso Aufiasu Ehudahui', 'a               ', '', 'Luke Xavier Pedroso', 2, 'Laércio França Pimentel']
mais_curto(lista)
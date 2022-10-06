import re
import csv
import os


class MenorNome():
    def __init__(self,file:list) -> None:
        self.file = file


    def mais_curto(self):
        nomes = self.ler_csv()
        mais_curto = nomes[0]

        for i in nomes:

            if len(i)<len(mais_curto):
                mais_curto = i


        return print(mais_curto)


    def regex_v2(self,nomes:str) -> str or bool:
        """This function receives a string and process it using regex

        Args:
            nomes (str): a string containing a brazilian name

        Returns:
            str or bool: if the given string does not pass on regex check, return a bool, else, return the given string
        """
        nome_separado = nomes.split(' ')

        if len(nome_separado) <=1:
            return False

        else:
            search_case = re.search("^[a-z]", nome_separado[0])
            x = re.search("[0-9]", nomes)
            dot_case = re.search("\.", nomes)

            if x or search_case:
                return False

            elif dot_case:
                return (nomes[nomes.rfind('.')+2:])

            else:
                return (nomes)


    def ler_csv(self) -> list:
        """This function receives a csv and process it, calling the function regex

        Returns:
            list: return a list of the shortest name from the given csv list
        """


        lista_nomes = []
        for i in file:

            with open(fr'csv/{i}','r') as f:

                names = csv.reader(f) #Aqui , o names faz a leitura de cada um dos csv.

                for i in names: #Separa cada lista do csv (No csv, cada linha é uma lista)
                    for j in i: #Separa cada string das listas

                        if type(j) != str:
                            pass

                        else:

                            if self.regex_v2(j):
                                if len (self.regex_v2(j).split()) <=1:
                                    pass
                                else:
                                    lista_nomes.append(self.regex_v2(j))


        return (lista_nomes)



file = [f for f in os.listdir(r"C:/Users/Vinicius/Documents/Estudos Python/Basico/nomes/csv") if f.endswith('.csv')]


run = MenorNome(file)
run.mais_curto()

import re 
from loguru import logger


class MenorNome():
    def __init__(self,lista:list,logger) -> None:
        self.lista = lista
        self.logger = logger


    def mais_curto(self):
        lista = self.lista
        
        for i in lista:
            self.logger.info(i)
            if type(i) != str:
                self.logger.error(i)
                pass
            else:
                self.logger.info(self.regex_v2(i))
                if not self.regex_v2(i):
                    logger.success(i)

        return print(lista)


    def regex_v2(self,nomes:str) -> str or bool:
        """This function receives a string and process it using regex

        Args:
            nomes (str): a string containing a brazilian name

        Returns:
            str or bool: if the given string does not pass on regex check, return a bool, else, return the given string
        """
        nomes.split(' ')
        if len(nomes) <=1:
            return False
        else:
            search_case = re.search("^[a-z]", nomes[0])
            x = re.search("[0-9]", nomes)

            if x or search_case:
                return False

            else:
                return nomes



lista = ['Predro 123 Certezas', 'Kylian Pedro Carlos', 'Yassna Parracho Pequeno', 'Cristina Cartaxo Teodoro', 'dfsjaiodjiaso Aufiasu Ehudahui', 'a               ', '', 'Luke Xavier Pedroso', 2, 'Laércio França Pimentel']

run = MenorNome(lista,logger)
run.mais_curto_v2()

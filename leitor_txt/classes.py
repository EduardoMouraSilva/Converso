# Classe para a manipulação do arquivo em .txt
# Criada por Eduardo


class Leitor():
    def __init__(self, arquivo):
        self.arquivo = arquivo

        self.abrir()

    def abrir(self):

        with open(self.arquivo, 'r') as arq:
            linhas = arq.readlines()

            self.caracteres = 0
            self.caracteres_sem = 0
            self.palavras = 0

            for linha in linhas:
                linha = linha.replace('\n', '')
                linha = linha.replace('\t', ' ')
                self.caracteres += len(linha)
                
                linha = linha.split(' ')
                if linha[0] == '':
                    del(linha[0])
                self.palavras += len(linha)

                for pala in linha:
                    self.caracteres_sem += len(pala)

        self.linhas = len(linhas)
                
    def mostrar(self):
        print('O arquivo tem: \n')
        print(f'\t{self.palavras} palavrs')
        print(f'\t{self.caracteres} caracteres')
        print(f'\t{self.caracteres_sem} caracteres sem espaço')
        print(f'\t{self.linhas} linhas')

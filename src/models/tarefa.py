class Tarefa:
    def __init__(self,nome):

        if not isinstance(nome,str):
            raise TypeError('o nome deve ser uma string')

        if nome == '':
            raise ValueError('o nome da tarefa nao pode ser vazio')


        self.nome=nome
    def retornar_como_dicionario(self):
        return {'nome':self.nome}
    
    @classmethod # para chamar a funcao a partir da classe e não do objeto
    def dicionario_para_objeto(cls,dicionario):#cls é a classe que o chamou 
        return cls(dicionario['nome'])


        


from models.tarefa import Tarefa

class Sessao:
    def __init__(self,tarefa,data,tempo=0):
        if not isinstance(tarefa,Tarefa) and tarefa is not None:
            raise TypeError('a tarefa deve ser um objeto Tarefa ou None')

        if not isinstance(tempo,int):
            raise TypeError('o tempo deve ser um numero inteiro')
        
        if tempo<0:
            raise ValueError('o tempo nao pode ser negativo')
        
        if not isinstance(data,str):
            raise TypeError('a data deve ser uma string')
        self.tarefa=tarefa
        self.data=data
        self.tempo=tempo

    def retornar_como_dicionario(self):
        return {'tarefa': None if self.tarefa is None else self.tarefa.retornar_como_dicionario(),'data':self.data,'tempo':self.tempo}
    
    @classmethod
    def dicionario_para_objeto(cls,dicionario):
        tarefa=None if dicionario['tarefa'] is None else Tarefa.dicionario_para_objeto(dicionario['tarefa'])
        return cls(tarefa,dicionario['data'],dicionario['tempo'])#retorna para a funcao o objeto

    
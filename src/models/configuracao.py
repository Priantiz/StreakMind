class Configuracao:
    def __init__(self, meta_diaria=30, dias_obrigatorios=None):

        if not isinstance(meta_diaria, int):
            raise TypeError('a meta diaria deve ser um numero inteiro')
        
        if meta_diaria <20:
            raise ValueError('A meta diaria deve ser maior ou igual que vinte')

        if dias_obrigatorios is None:
            dias_obrigatorios = [0,1,2,3,4,5,6]

        if not isinstance (dias_obrigatorios, list):
            raise TypeError('os dias obrigatorios devem ser uma lista')
        if len(dias_obrigatorios) == 0:
            raise ValueError('deve existir pelo menos um dia obrigatorio')
        for dia in dias_obrigatorios:
            if not isinstance (dia, int):
                raise TypeError('Cada dia obrigatorio deve ser um numero inteiro')
            if dia <0 or dia >6:
                raise ValueError('os dias obrigatorios devem estar entre 0 e 6')
        
        if len(dias_obrigatorios)!= len(set(dias_obrigatorios)):
            raise ValueError('os dias obrigatorios nao podem ser repetidos')
        self.meta_diaria = meta_diaria
        self.dias_obrigatorios = dias_obrigatorios
    
    def retornar_como_dicionario(self):
        return {'meta_diaria':self.meta_diaria,'dias_obrigatorios':self.dias_obrigatorios}
    
    @classmethod
    def dicionario_para_objeto(cls,dicionario):
        return cls(dicionario['meta_diaria'],dicionario['dias_obrigatorios'])
    

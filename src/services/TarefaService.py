from models.tarefa import Tarefa


class TarefaService:
    def __init__(
        self,
        lista_tarefas=None,
        repositorio=None,
        sessao_service=None,
        configuracao=None,
        streak_service=None
    ):
        lista_tarefas = [] if lista_tarefas is None else lista_tarefas

        if not isinstance(lista_tarefas, list):
            raise TypeError('lista_tarefas deve ser uma lista')

        for tarefa in lista_tarefas:
            if not isinstance(tarefa, Tarefa):
                raise TypeError('todos os itens da lista devem ser objetos Tarefa')

        self.lista_tarefas = lista_tarefas
        self.repositorio = repositorio
        self.sessao_service = sessao_service
        self.configuracao = configuracao
        self.streak_service = streak_service

    def salvar_dados(self):
        if self.repositorio is not None:
            self.repositorio.salvar(
                tarefa_service=self,
                sessao_service=self.sessao_service,
                configuracao=self.configuracao,
                streak_service=self.streak_service
            )   
   
    def adicionar_tarefa(self,nome_tarefa):
        
        if not isinstance(nome_tarefa,str):
            raise TypeError('o nome da tarefa deve ser uma string')
        for tarefa in self.lista_tarefas:
            if tarefa.nome == nome_tarefa:
                raise ValueError('ja existe uma tarefa com esse nome')
        nova_tarefa=Tarefa(nome_tarefa)
        self.lista_tarefas.append(nova_tarefa)
        self.salvar_dados()
        return nova_tarefa
    
    def remover_tarefa(self,nome_tarefa):
        if not isinstance(nome_tarefa,str):
            raise TypeError('o nome da tarefa deve ser uma string')
        for tarefa in self.lista_tarefas:
            if tarefa.nome==nome_tarefa:
                self.lista_tarefas.remove(tarefa)
                self.salvar_dados()
                return True
        return False
    
    def listar_tarefas(self):
        return self.lista_tarefas
    


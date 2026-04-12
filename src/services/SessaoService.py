from models.sessao import Sessao
from datetime import datetime

class SessaoService:
    def __init__(
        self,
        tarefa_service,
        streak_service,
        sessao_ativa=None,
        lista_sessoes=None,
        repositorio=None,
        configuracao=None
    ):
        if sessao_ativa is not None and not isinstance(sessao_ativa, Sessao):
            raise TypeError('a sessao_ativa deve ser um objeto Sessao ou None')

        lista_sessoes = [] if lista_sessoes is None else lista_sessoes

        if not isinstance(lista_sessoes, list):
            raise TypeError('lista_sessoes deve ser uma lista')

        for sessao in lista_sessoes:
            if not isinstance(sessao, Sessao):
                raise TypeError('todos os itens da lista devem ser objetos sessao')

        self.sessao_ativa = sessao_ativa
        self.lista_sessoes = lista_sessoes
        self.tarefa_service = tarefa_service
        self.streak_service = streak_service
        self.horario_inicial = None
        self.horario_final = None
        self.repositorio = repositorio
        self.configuracao = configuracao

    def salvar_dados(self):
        if self.repositorio is not None:
            self.repositorio.salvar(
                tarefa_service=self.tarefa_service,
                sessao_service=self,
                configuracao=self.configuracao,
                streak_service=self.streak_service
            )

    def iniciar_sessao(self,tarefa):
        if self.sessao_ativa is not None:
            return
        data_de_hoje = datetime.now().strftime("%Y-%m-%d")
        if tarefa is None:
            nova_sessao = Sessao(tarefa,data_de_hoje)
            self.sessao_ativa=nova_sessao
            self.horario_inicial = datetime.now()
        elif tarefa in self.tarefa_service.listar_tarefas():
            nova_sessao = Sessao(tarefa,data_de_hoje)
            self.sessao_ativa=nova_sessao
            self.horario_inicial = datetime.now()

    def encerrar_sessao(self):
        if self.sessao_ativa is not None:
            self.horario_final = datetime.now()
            diferenca = self.horario_final - self.horario_inicial
            diferenca = diferenca.total_seconds() / 60
            self.sessao_ativa.tempo = int(diferenca)
            self.lista_sessoes.append(self.sessao_ativa)
            self.streak_service.atualizar_streak()
            self.horario_inicial = None
            self.horario_final = None
            self.sessao_ativa = None
            self.salvar_dados()
            
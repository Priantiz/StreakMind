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
        self.tempo_pausado_segundos = 0
        self.sessao_pausada = False
    
    def salvar_dados(self):
        if self.repositorio is not None:
            self.repositorio.salvar(
                tarefa_service=self.tarefa_service,
                sessao_service=self,
                configuracao=self.configuracao,
                streak_service=self.streak_service
        )
    def iniciar_sessao(self, tarefa):
        if self.sessao_ativa is not None:
            return

        data_de_hoje = datetime.now().strftime("%Y-%m-%d")

        if tarefa is None:
            nova_sessao = Sessao(tarefa, data_de_hoje)
            self.sessao_ativa = nova_sessao
            self.horario_inicial = datetime.now()
            self.tempo_pausado_segundos = 0
            self.sessao_pausada = False

        elif tarefa in self.tarefa_service.listar_tarefas():
            nova_sessao = Sessao(tarefa, data_de_hoje)
            self.sessao_ativa = nova_sessao
            self.horario_inicial = datetime.now()
            self.tempo_pausado_segundos = 0
            self.sessao_pausada = False

    def pausar_sessao(self):
        if self.sessao_ativa is not None and not self.sessao_pausada:
            self.horario_final = datetime.now()
            diferenca = self.horario_final - self.horario_inicial
            self.tempo_pausado_segundos += int(diferenca.total_seconds())
            self.sessao_pausada = True

    def retomar_sessao(self):
        if self.sessao_ativa is not None and self.sessao_pausada:
            self.horario_inicial = datetime.now()
            self.sessao_pausada = False

    def encerrar_sessao(self):
        if self.sessao_ativa is not None:
            if not self.sessao_pausada:
                self.horario_final = datetime.now()
                diferenca = self.horario_final - self.horario_inicial
                self.tempo_pausado_segundos += int(diferenca.total_seconds())

            self.sessao_ativa.tempo = self.tempo_pausado_segundos // 60
            self.lista_sessoes.append(self.sessao_ativa)
            self.streak_service.atualizar_streak()

            self.horario_inicial = None
            self.horario_final = None
            self.sessao_ativa = None
            self.tempo_pausado_segundos = 0
            self.sessao_pausada = False
            self.salvar_dados()
            
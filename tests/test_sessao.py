import sys
import os
from datetime import timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from services.TarefaService import TarefaService
from services.SessaoService import SessaoService


class StreakServiceFake:
    def __init__(self):
        self.atualizou = False

    def atualizar_streak(self):
        self.atualizou = True

    def retornar_como_dicionario(self):
        return {
            'streak_atual': 0,
            'dia_ja_validado': False,
            'data_ultimo_dia': None,
            'cumpriu_meta_no_dia': False
        }


def test_iniciar_sessao_com_tarefa_valida():
    tarefa_service = TarefaService()
    tarefa = tarefa_service.adicionar_tarefa('Python')
    streak_service = StreakServiceFake()

    sessao_service = SessaoService(
        tarefa_service=tarefa_service,
        streak_service=streak_service
    )

    sessao_service.iniciar_sessao(tarefa)

    assert sessao_service.sessao_ativa is not None
    assert sessao_service.sessao_ativa.tarefa == tarefa


def test_iniciar_sessao_livre():
    tarefa_service = TarefaService()
    streak_service = StreakServiceFake()

    sessao_service = SessaoService(
        tarefa_service=tarefa_service,
        streak_service=streak_service
    )

    sessao_service.iniciar_sessao(None)

    assert sessao_service.sessao_ativa is not None
    assert sessao_service.sessao_ativa.tarefa is None


def test_encerrar_sessao_salva_na_lista():
    tarefa_service = TarefaService()
    tarefa = tarefa_service.adicionar_tarefa('Python')
    streak_service = StreakServiceFake()

    sessao_service = SessaoService(
        tarefa_service=tarefa_service,
        streak_service=streak_service
    )

    sessao_service.iniciar_sessao(tarefa)
    sessao_service.horario_inicial -= timedelta(minutes=10)
    sessao_service.encerrar_sessao()

    assert len(sessao_service.lista_sessoes) == 1
    assert sessao_service.lista_sessoes[0].tarefa == tarefa
    assert sessao_service.lista_sessoes[0].tempo == 10
    assert sessao_service.sessao_ativa is None


def test_encerrar_sessao_atualiza_streak():
    tarefa_service = TarefaService()
    tarefa = tarefa_service.adicionar_tarefa('Python')
    streak_service = StreakServiceFake()

    sessao_service = SessaoService(
        tarefa_service=tarefa_service,
        streak_service=streak_service
    )

    sessao_service.iniciar_sessao(tarefa)
    sessao_service.horario_inicial -= timedelta(minutes=5)
    sessao_service.encerrar_sessao()

    assert streak_service.atualizou is True


def test_nao_inicia_outra_sessao_se_ja_existir_uma_ativa():
    tarefa_service = TarefaService()
    tarefa1 = tarefa_service.adicionar_tarefa('Python')
    tarefa2 = tarefa_service.adicionar_tarefa('Java')
    streak_service = StreakServiceFake()

    sessao_service = SessaoService(
        tarefa_service=tarefa_service,
        streak_service=streak_service
    )

    sessao_service.iniciar_sessao(tarefa1)
    sessao_ativa_inicial = sessao_service.sessao_ativa

    sessao_service.iniciar_sessao(tarefa2)

    assert sessao_service.sessao_ativa == sessao_ativa_inicial
    assert sessao_service.sessao_ativa.tarefa == tarefa1
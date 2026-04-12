import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from models.configuracao import Configuracao
from services.StreakService import StreakService


class DashboardFake:
    def __init__(self, tempo_total):
        self.tempo_total = tempo_total

    def calcular_tempo_total(self):
        return self.tempo_total


def test_streak_sobe_ao_bater_meta():
    configuracao = Configuracao(meta_diaria=30)
    dashboard = DashboardFake(35)

    streak_service = StreakService(
        configuracao=configuracao,
        dashboard_service=dashboard,
        streak_atual=0,
        dia_ja_validado=False
    )

    streak_service.atualizar_streak()

    assert streak_service.streak_atual == 1
    assert streak_service.cumpriu_meta_no_dia is True


def test_streak_nao_sobe_abaixo_da_meta():
    configuracao = Configuracao(meta_diaria=30)
    dashboard = DashboardFake(20)

    streak_service = StreakService(
        configuracao=configuracao,
        dashboard_service=dashboard,
        streak_atual=0,
        dia_ja_validado=False
    )

    streak_service.atualizar_streak()

    assert streak_service.streak_atual == 0
    assert streak_service.cumpriu_meta_no_dia is False


def test_streak_nao_sobe_duas_vezes_no_mesmo_dia():
    configuracao = Configuracao(meta_diaria=30)
    dashboard = DashboardFake(40)

    streak_service = StreakService(
        configuracao=configuracao,
        dashboard_service=dashboard,
        streak_atual=0,
        dia_ja_validado=False
    )

    streak_service.atualizar_streak()
    streak_service.atualizar_streak()

    assert streak_service.streak_atual == 1


def test_streak_zera_se_perder_dia_obrigatorio():
    configuracao = Configuracao(meta_diaria=30)
    dashboard = DashboardFake(0)

    ontem = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    streak_service = StreakService(
        configuracao=configuracao,
        dashboard_service=dashboard,
        streak_atual=5,
        dia_ja_validado=True,
        data_ultimo_dia=ontem,
        cumpriu_meta_no_dia=False
    )

    streak_service.atualizar_streak()

    assert streak_service.streak_atual == 0
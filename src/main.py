from storage.json_repository import JsonRepository
from services.TarefaService import TarefaService
from services.SessaoService import SessaoService
from services.DashboardService import DashboardService
from services.StreakService import StreakService
from services.ConfiguracaoService import ConfiguracaoService
from ui.app_window import AppWindow


def main():
    repositorio = JsonRepository()
    dados = repositorio.carregar()

    tarefas = dados['tarefas']
    sessoes = dados['sessoes']
    configuracao = dados['configuracao']
    streak_dict = dados['streak']

    tarefa_service = TarefaService(
        lista_tarefas=tarefas,
        repositorio=repositorio,
        configuracao=configuracao
    )

    sessao_service = SessaoService(
        tarefa_service=tarefa_service,
        streak_service=None,
        lista_sessoes=sessoes,
        repositorio=repositorio,
        configuracao=configuracao
    )

    dashboard_service = DashboardService(sessao_service)

    streak_service = StreakService(
        configuracao=configuracao,
        dashboard_service=dashboard_service,
        streak_atual=streak_dict.get('streak_atual', 0),
        dia_ja_validado=streak_dict.get('dia_ja_validado', False),
        data_ultimo_dia=streak_dict.get('data_ultimo_dia', None),
        cumpriu_meta_no_dia=streak_dict.get('cumpriu_meta_no_dia', False)
    )

    configuracao_service = ConfiguracaoService(
        configuracao=configuracao,
        repositorio=repositorio,
        tarefa_service=tarefa_service,
        sessao_service=sessao_service,
        streak_service=streak_service
    )

    sessao_service.streak_service = streak_service
    tarefa_service.sessao_service = sessao_service
    tarefa_service.streak_service = streak_service

    janela = AppWindow(
        tarefa_service=tarefa_service,
        sessao_service=sessao_service,
        dashboard_service=dashboard_service,
        streak_service=streak_service,
        configuracao_service=configuracao_service
    )

    janela.iniciar()


if __name__ == '__main__':
    main()
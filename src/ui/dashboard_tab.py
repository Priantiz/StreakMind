from tkinter import ttk
from datetime import datetime

class DashboardTab:
    def __init__(self, parent, dashboard_service, streak_service, configuracao_service):
        self.parent = parent
        self.dashboard_service = dashboard_service
        self.streak_service = streak_service
        self.configuracao_service = configuracao_service

        self.frame = ttk.Frame(self.parent)

        self.criar_widgets()
        self.atualizar_dashboard()

    def criar_widgets(self):
        self.titulo_label = ttk.Label(
            self.frame,
            text='Dashboard',
            font=('Arial', 16)
        )
        self.titulo_label.pack(pady=20)

        self.streak_label = ttk.Label(self.frame, text='')
        self.streak_label.pack(pady=5)

        self.meta_label = ttk.Label(self.frame, text='')
        self.meta_label.pack(pady=5)

        self.tempo_total_label = ttk.Label(self.frame, text='')
        self.tempo_total_label.pack(pady=5)

        self.status_label = ttk.Label(self.frame, text='')
        self.status_label.pack(pady=5)

        self.resumo_titulo_label = ttk.Label(
            self.frame,
            text='Resumo por tarefa do dia:'
        )
        self.resumo_titulo_label.pack(pady=(20, 5))

        self.resumo_label = ttk.Label(self.frame, text='', justify='left')
        self.resumo_label.pack(pady=5)

    def atualizar_dashboard(self):
        streak = self.streak_service.streak_atual
        meta = self.configuracao_service.configuracao.meta_diaria
        tempo_total = self.dashboard_service.calcular_tempo_total()
        tempo_por_tarefa = self.dashboard_service.calcular_tempo_cada_tarefa()

        self.streak_label.config(text=f'Streak atual: {streak}')
        self.meta_label.config(text=f'Meta diária: {meta} min')
        self.tempo_total_label.config(text=f'Tempo total hoje: {tempo_total} min')

        dia_da_semana_hoje = datetime.now().weekday()
        dias_obrigatorios = self.configuracao_service.configuracao.dias_obrigatorios
        if dia_da_semana_hoje not in dias_obrigatorios:
            self.status_label.config(text='Status: hoje não é um dia obrigatório')
        else:

            if tempo_total >= meta:
                self.status_label.config(text='Status do dia: meta atingida')
            else:
                faltam = meta - tempo_total
                self.status_label.config(text=f'Status do dia: faltam {faltam} min')

        if not tempo_por_tarefa:
            self.resumo_label.config(text='Nenhum estudo registrado hoje.')
        else:
            linhas = []
            for nome_tarefa, tempo in tempo_por_tarefa.items():
                linhas.append(f'{nome_tarefa}: {tempo} min')

            self.resumo_label.config(text='\n'.join(linhas))  
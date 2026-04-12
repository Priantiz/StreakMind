from tkinter import ttk
import tkinter as tk

from ui.dashboard_tab import DashboardTab
from ui.tarefas_tab import TarefasTab
from ui.configuracoes_tab import ConfiguracoesTab
from ui.sessao_tab import SessaoTab

class AppWindow:
    def __init__(
        self,
        tarefa_service,
        sessao_service,
        dashboard_service,
        streak_service,
        configuracao_service
    ):
        self.tarefa_service = tarefa_service
        self.sessao_service = sessao_service
        self.dashboard_service = dashboard_service
        self.streak_service = streak_service
        self.configuracao_service = configuracao_service

        self.root = tk.Tk()
        self.root.title('StudyFlow')
        self.root.geometry('300x400')
        self.root.resizable(False, False)

        self.criar_abas()

    def criar_abas(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        self.dashboard_tab = DashboardTab(
            self.notebook,
            self.dashboard_service,
            self.streak_service,
            self.configuracao_service
        )

        self.sessao_tab = SessaoTab(
            self.notebook,
            self.tarefa_service,
            self.sessao_service,
            self.dashboard_tab
        )

        self.tarefas_tab = TarefasTab(
            self.notebook,
            self.tarefa_service,
            self.sessao_tab
        )

        self.configuracoes_tab = ConfiguracoesTab(
            self.notebook,
            self.configuracao_service,
            self.dashboard_tab
        )

        self.notebook.add(self.dashboard_tab.frame, text='Dashboard')
        self.notebook.add(self.sessao_tab.frame, text='Sessão')
        self.notebook.add(self.tarefas_tab.frame, text='Tarefas')
        self.notebook.add(self.configuracoes_tab.frame, text='Configurações')
    def iniciar(self):
        self.root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class SessaoTab:
    def __init__(self, parent, tarefa_service, sessao_service, dashboard_tab=None):
        self.parent = parent
        self.tarefa_service = tarefa_service
        self.sessao_service = sessao_service
        self.dashboard_tab = dashboard_tab

        self.frame = ttk.Frame(self.parent)

        self.timer_rodando = False
        self.tempo_decorrido = 0

        self.criar_widgets()
        self.atualizar_lista_tarefas()

    def criar_widgets(self):

        self.selecao_frame = ttk.Frame(self.frame)
        self.selecao_frame.pack(pady=20)

        self.tarefa_label = ttk.Label(self.selecao_frame, text='Tarefa:')
        self.tarefa_label.grid(row=0, column=0, padx=5, pady=5)

        self.tarefa_combobox = ttk.Combobox(
            self.selecao_frame,
            state='readonly',
            width=30
        )
        self.tarefa_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.estudo_livre_var = tk.BooleanVar()
        self.estudo_livre_check = ttk.Checkbutton(
            self.frame,
            text='Sessão livre',
            variable=self.estudo_livre_var,
            command=self.alternar_modo_estudo
        )
        self.estudo_livre_check.pack(pady=10)

        self.timer_label = ttk.Label(
            self.frame,
            text='00:00:00',
            font=('Arial', 24)
        )
        self.timer_label.pack(pady=20)

        self.botoes_frame = ttk.Frame(self.frame)
        self.botoes_frame.pack(pady=10)

        self.iniciar_button = ttk.Button(
            self.botoes_frame,
            text='Iniciar sessão',
            command=self.iniciar_sessao,
            width=20
        )
        self.iniciar_button.pack(pady=5)

        self.pausar_button = ttk.Button(
            self.botoes_frame,
            text='Pausar sessão',
            command=self.pausar_ou_retomar_sessao,
            width=20
        )
        self.pausar_button.pack(pady=5)

        self.encerrar_button = ttk.Button(
            self.botoes_frame,
            text='Encerrar sessão',
            command=self.encerrar_sessao,
            width=20
        )
        self.encerrar_button.pack(pady=5)


    def atualizar_lista_tarefas(self):
        nomes_tarefas = [tarefa.nome for tarefa in self.tarefa_service.listar_tarefas()]
        self.tarefa_combobox['values'] = nomes_tarefas

        if nomes_tarefas:
            self.tarefa_combobox.current(0)

    def alternar_modo_estudo(self):
        if self.estudo_livre_var.get():
            self.tarefa_combobox.config(state='disabled')
        else:
            self.tarefa_combobox.config(state='readonly')

    def iniciar_sessao(self):
        if self.sessao_service.sessao_ativa is not None:
            messagebox.showwarning('Aviso', 'Já existe uma sessão ativa.')
            return

        if self.estudo_livre_var.get():
            tarefa_escolhida = None
        else:
            nome_tarefa = self.tarefa_combobox.get()

            if not nome_tarefa:
                messagebox.showwarning('Aviso', 'Selecione uma tarefa ou marque estudo livre.')
                return

            tarefa_escolhida = None
            for tarefa in self.tarefa_service.listar_tarefas():
                if tarefa.nome == nome_tarefa:
                    tarefa_escolhida = tarefa
                    break

        self.sessao_service.iniciar_sessao(tarefa_escolhida)

        if self.sessao_service.sessao_ativa is not None:
            self.timer_rodando = True
            self.tempo_decorrido = 0
            self.pausar_button.config(text='Pausar sessão')
            self.atualizar_timer()

    def pausar_ou_retomar_sessao(self):
        if self.sessao_service.sessao_ativa is None:
            messagebox.showwarning('Aviso', 'Não há sessão ativa.')
            return

        if self.sessao_service.sessao_pausada:
            self.sessao_service.retomar_sessao()
            self.timer_rodando = True
            self.pausar_button.config(text='Pausar sessão')
            self.atualizar_timer()
        else:
            self.sessao_service.pausar_sessao()
            self.timer_rodando = False
            self.pausar_button.config(text='Retomar sessão')

    def encerrar_sessao(self):
        if self.sessao_service.sessao_ativa is None:
            messagebox.showwarning('Aviso', 'Não há sessão ativa.')
            return

        self.timer_rodando = False
        self.sessao_service.encerrar_sessao()
        self.timer_label.config(text='00:00:00')
        self.tempo_decorrido = 0
        self.pausar_button.config(text='Pausar sessão')

        if self.dashboard_tab is not None:
            self.dashboard_tab.atualizar_dashboard()

        messagebox.showinfo('Sucesso', 'Sessão encerrada com sucesso.')

    def atualizar_timer(self):
        if not self.timer_rodando:
            return

        if self.sessao_service.sessao_ativa is None:
            return

        self.tempo_decorrido = self.sessao_service.tempo_pausado_segundos

        if not self.sessao_service.sessao_pausada and self.sessao_service.horario_inicial is not None:
            segundos_atuais = int((datetime.now() - self.sessao_service.horario_inicial).total_seconds())
            self.tempo_decorrido += segundos_atuais

        horas = self.tempo_decorrido // 3600
        minutos = (self.tempo_decorrido % 3600) // 60
        segundos = self.tempo_decorrido % 60

        self.timer_label.config(text=f'{horas:02}:{minutos:02}:{segundos:02}')
        self.frame.after(1000, self.atualizar_timer)
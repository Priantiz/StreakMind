import tkinter as tk
from tkinter import ttk, messagebox


class ConfiguracoesTab:
    def __init__(self, parent, configuracao_service, dashboard_tab=None):
        self.parent = parent
        self.configuracao_service = configuracao_service
        self.dashboard_tab = dashboard_tab

        self.frame = ttk.Frame(self.parent)

        self.vars_dias = {}
        self.criar_widgets()
        self.carregar_valores_atuais()

    def criar_widgets(self):
        self.titulo_label = ttk.Label(
            self.frame,
            text='Configurações',
            font=('Arial', 16)
        )
        self.titulo_label.pack(pady=20)

        self.meta_frame = ttk.Frame(self.frame)
        self.meta_frame.pack(pady=10)

        self.meta_label = ttk.Label(self.meta_frame, text='Meta diária (min):')
        self.meta_label.grid(row=0, column=0, padx=5, pady=5)

        self.meta_entry = ttk.Entry(self.meta_frame, width=10)
        self.meta_entry.grid(row=0, column=1, padx=5, pady=5)

        self.dias_label = ttk.Label(self.frame, text='Dias obrigatórios:')
        self.dias_label.pack(pady=(20, 10))

        self.dias_frame = ttk.Frame(self.frame)
        self.dias_frame.pack(pady=5)

        nomes_dias = [
            ('Seg', 0),
            ('Ter', 1),
            ('Qua', 2),
            ('Qui', 3),
            ('Sex', 4),
            ('Sáb', 5),
            ('Dom', 6)
        ]

        for indice, (nome, valor) in enumerate(nomes_dias):
            var = tk.BooleanVar()
            self.vars_dias[valor] = var

            if indice < 4:
                linha = 0
                coluna = indice
            else:
                linha = 1
                coluna = indice - 4

            check = ttk.Checkbutton(
                self.dias_frame,
                text=nome,
                variable=var
            )
            check.grid(row=linha, column=coluna, padx=5, pady=5, sticky='w')

        self.salvar_button = ttk.Button(
            self.frame,
            text='Salvar configurações',
            command=self.salvar_configuracoes
        )
        self.salvar_button.pack(pady=20)

    def carregar_valores_atuais(self):
        configuracao = self.configuracao_service.configuracao

        self.meta_entry.delete(0, tk.END)
        self.meta_entry.insert(0, str(configuracao.meta_diaria))

        for dia, var in self.vars_dias.items():
            var.set(dia in configuracao.dias_obrigatorios)

    def salvar_configuracoes(self):
        try:
            nova_meta = int(self.meta_entry.get().strip())

            dias_obrigatorios = [
                dia for dia, var in self.vars_dias.items()
                if var.get()
            ]

            self.configuracao_service.definir_meta_diaria(nova_meta)
            self.configuracao_service.definir_dias_obrigatorios(dias_obrigatorios)

            if self.dashboard_tab is not None:
                self.dashboard_tab.atualizar_dashboard()

            messagebox.showinfo('Sucesso', 'Configurações salvas com sucesso.')

        except Exception as erro:
            messagebox.showerror('Erro', str(erro))
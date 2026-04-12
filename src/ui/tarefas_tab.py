import tkinter as tk
from tkinter import ttk, messagebox


class TarefasTab:
    def __init__(self, parent, tarefa_service, sessao_tab=None):
        self.parent = parent
        self.tarefa_service = tarefa_service
        self.sessao_tab = sessao_tab

        self.frame = ttk.Frame(self.parent)

        self.criar_widgets()
        self.atualizar_lista_tarefas()
        
    def criar_widgets(self):

        self.input_frame = ttk.Frame(self.frame)
        self.input_frame.pack(pady=15)

        self.nome_label = ttk.Label(self.input_frame, text='Nome da tarefa:')
        self.nome_label.grid(row=0, column=0, padx=5, pady=5)

        self.nome_entry = ttk.Entry(self.input_frame, width=30)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        self.botoes_frame = ttk.Frame(self.frame)
        self.botoes_frame.pack(pady=8)

        self.adicionar_button = ttk.Button(
            self.botoes_frame,
            text='Adicionar',
            command=self.adicionar_tarefa,
            width=20
        )
        self.adicionar_button.pack(pady=4)

        self.remover_button = ttk.Button(
            self.botoes_frame,
            text='Remover selecionada',
            command=self.remover_tarefa,
            width=20
        )
        self.remover_button.pack(pady=4)

        self.lista_label = ttk.Label(self.frame, text='Tarefas cadastradas:')
        self.lista_label.pack(pady=(10, 3))

        self.lista_tarefas = tk.Listbox(self.frame, width=40, height=10)
        self.lista_tarefas.pack(pady=2)

    def atualizar_lista_tarefas(self):
        self.lista_tarefas.delete(0, tk.END)

        for tarefa in self.tarefa_service.listar_tarefas():
            self.lista_tarefas.insert(tk.END, tarefa.nome)

    def adicionar_tarefa(self):
        nome_tarefa = self.nome_entry.get().strip()

        try:
            self.tarefa_service.adicionar_tarefa(nome_tarefa)
            self.atualizar_lista_tarefas()
            self.nome_entry.delete(0, tk.END)
            if self.sessao_tab is not None:
                self.sessao_tab.atualizar_lista_tarefas()
        except Exception as erro:
            messagebox.showerror('Erro', str(erro))

    def remover_tarefa(self):
        selecao = self.lista_tarefas.curselection()

        if not selecao:
            messagebox.showwarning('Aviso', 'Selecione uma tarefa para remover.')
            return

        nome_tarefa = self.lista_tarefas.get(selecao[0])

        removida = self.tarefa_service.remover_tarefa(nome_tarefa)

        if removida:
            self.atualizar_lista_tarefas()
            if self.sessao_tab is not None:
                self.sessao_tab.atualizar_lista_tarefas()
        else:
            messagebox.showerror('Erro', 'Não foi possível remover a tarefa.')
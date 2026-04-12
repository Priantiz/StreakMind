import json
import os

from models.tarefa import Tarefa
from models.sessao import Sessao
from models.configuracao import Configuracao


class JsonRepository:
    def __init__(self, caminho_arquivo='dados.json'):
        self.caminho_arquivo = caminho_arquivo

    def criar_arquivo_se_nao_existir(self):
        if not os.path.exists(self.caminho_arquivo):
            dados_iniciais = {
                'tarefas': [],
                'sessoes': [],
                'configuracao': {},
                'streak': {}
            }

            with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados_iniciais, arquivo, ensure_ascii=False, indent=4)

    def salvar(self, tarefa_service, sessao_service, configuracao, streak_service):
        self.criar_arquivo_se_nao_existir()

        dados = {
            'tarefas': [
                tarefa.retornar_como_dicionario()
                for tarefa in tarefa_service.lista_tarefas
            ],
            'sessoes': [
                sessao.retornar_como_dicionario()
                for sessao in sessao_service.lista_sessoes
            ],
            'configuracao': configuracao.retornar_como_dicionario(),
            'streak': streak_service.retornar_como_dicionario()
        }

        with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar(self):
        self.criar_arquivo_se_nao_existir()

        with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        tarefas = [
            Tarefa.dicionario_para_objeto(tarefa)
            for tarefa in dados.get('tarefas', [])
        ]

        sessoes = [
            Sessao.dicionario_para_objeto(sessao)
            for sessao in dados.get('sessoes', [])
        ]

        configuracao_dict = dados.get('configuracao', {})
        if configuracao_dict:
            configuracao = Configuracao.dicionario_para_objeto(configuracao_dict)
        else:
            configuracao = Configuracao()

        streak = dados.get('streak', {})

        return {
            'tarefas': tarefas,
            'sessoes': sessoes,
            'configuracao': configuracao,
            'streak': streak
        }
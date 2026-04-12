import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.services.TarefaService import TarefaService

def test_adicionar_tarefa_valida():
    tarefa_service = TarefaService()

    nova_tarefa = tarefa_service.adicionar_tarefa('Python')

    assert nova_tarefa.nome == 'Python'
    assert len(tarefa_service.lista_tarefas) == 1
    assert tarefa_service.lista_tarefas[0].nome == 'Python'


def test_adicionar_tarefa_duplicada():
    tarefa_service = TarefaService()
    tarefa_service.adicionar_tarefa('Python')

    with pytest.raises(ValueError):
        tarefa_service.adicionar_tarefa('Python')


def test_remover_tarefa_existente():
    tarefa_service = TarefaService()
    tarefa_service.adicionar_tarefa('Python')

    resultado = tarefa_service.remover_tarefa('Python')

    assert resultado is True
    assert len(tarefa_service.lista_tarefas) == 0


def test_remover_tarefa_inexistente():
    tarefa_service = TarefaService()

    resultado = tarefa_service.remover_tarefa('Java')

    assert resultado is False
    assert len(tarefa_service.lista_tarefas) == 0


def test_adicionar_tarefa_com_nome_invalido():
    tarefa_service = TarefaService()

    with pytest.raises(TypeError):
        tarefa_service.adicionar_tarefa(123)
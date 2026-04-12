# StreakMind

Versão: 1.0.0

## Descrição

O StreakMind é uma aplicação desktop em Python com interface gráfica que ajuda estudantes a manterem consistência nos estudos por meio de registro de sessões, acompanhamento do tempo estudado no dia e sistema de streak baseado em metas mínimas.

O sistema foi criado para ajudar estudantes que têm dificuldade em manter rotina, não sabem quanto realmente estudam e perdem consistência com facilidade.

## Problema real

Muitos estudantes têm dificuldade em criar e manter uma rotina de estudos. Em vários casos, a pessoa até sente que estudou bastante, mas não possui um registro claro do tempo investido, nem um acompanhamento objetivo da própria constância.

Isso gera problemas como:

- falta de disciplina
- sensação de progresso sem medição real
- perda de consistência
- dificuldade em manter hábitos de estudo

## Proposta da solução

O StreakMind resolve esse problema registrando sessões de estudo em tempo real e comparando o total estudado no dia com uma meta mínima definida pelo usuário.

Além disso, o sistema utiliza um mecanismo de streak para incentivar constância, considerando os dias obrigatórios da semana configurados pelo próprio usuário.

## Público-alvo

Estudantes que desejam:

- melhorar a disciplina nos estudos
- medir com clareza o tempo estudado
- acompanhar constância ao longo dos dias
- organizar sessões de estudo por tarefa ou de forma livre

## Funcionalidades principais

- dashboard com resumo do dia
- exibição da streak atual
- exibição da meta diária
- cálculo do tempo total estudado no dia
- resumo por tarefa do dia
- criação e remoção de tarefas
- sessão com tarefa
- sessão livre
- pausa e retomada de sessão
- configuração de meta diária
- configuração de dias obrigatórios
- persistência de dados em JSON

## Regras principais do sistema

- a streak só conta em dias obrigatórios (definidos pelo usuário)
- o usuário deve definir pelo menos 1 dia obrigatório por semana
- a meta diária deve ser de pelo menos 20 minutos
- a streak só aumenta quando o tempo total do dia atinge a meta diária
- dias não obrigatórios não quebram a streak
- apenas uma sessão pode ficar ativa por vez
- tarefas são opcionais
- sessões livres são permitidas

## Tecnologias utilizadas

- Python 3
- Tkinter
- JSON
- Pytest
- Ruff
- GitHub Actions

## Instruções de instalação

```bat
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Instrução de execução

```bat
python src/main.py
```

## Instruções para rodar os testes
```bat
python -m pytest tests
```

## Instrução para rodar o lint
```bat
python -m ruff check src tests
```

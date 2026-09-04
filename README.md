# StreakMind

**Versão:** 1.2.0

**Autor:** Lucas Porcedda Prianti

**Repositório:** https://github.com/Priantiz/StreakMind

**Página do projeto:** https://priantiz.github.io/StreakMind/

## Descrição

O StreakMind é uma aplicação desktop open source desenvolvida em Python com interface gráfica, criada para ajudar estudantes a manterem consistência nos estudos por meio do registro de sessões, acompanhamento do tempo estudado e sistema de streak baseado em metas mínimas.

O projeto também busca demonstrar práticas de desenvolvimento de software, como organização em camadas, persistência de dados, testes automatizados, linting, integração com API externa e integração contínua com GitHub Actions.

## Download para Windows

Para utilizar o StreakMind sem instalar Python ou configurar o ambiente de desenvolvimento, baixe a versão mais recente do executável na seção de Releases:

https://github.com/Priantiz/StreakMind/releases

O executável do Windows já contém as dependências necessárias para executar a aplicação.

> Para analisar, modificar ou executar o código-fonte, consulte as instruções abaixo.

## Problema real

Muitos estudantes têm dificuldade em criar e manter uma rotina de estudos. Em vários casos, a pessoa até sente que estudou bastante, mas não possui um registro claro do tempo investido, nem um acompanhamento objetivo da própria constância.

Isso pode gerar problemas como:

- falta de disciplina;
- sensação de progresso sem medição real;
- perda de consistência;
- dificuldade em manter hábitos de estudo.

## Proposta da solução

O StreakMind ajuda a lidar com esse problema registrando sessões de estudo em tempo real e comparando o total estudado no dia com uma meta mínima definida pelo usuário.

Além disso, o sistema utiliza um mecanismo de streak para acompanhar a constância do usuário, considerando os dias obrigatórios da semana definidos nas configurações.

## Público-alvo

O StreakMind é destinado principalmente a estudantes que desejam:

- melhorar a disciplina nos estudos;
- medir com clareza o tempo estudado;
- acompanhar a constância ao longo dos dias;
- organizar sessões de estudo por tarefa ou de forma livre.

## Funcionalidades principais

- dashboard com resumo do dia;
- exibição da streak atual;
- exibição da meta diária;
- cálculo do tempo total estudado no dia;
- resumo do tempo estudado por tarefa;
- criação e remoção de tarefas;
- sessões de estudo associadas a tarefas;
- sessões de estudo livre;
- pausa e retomada de sessões;
- configuração da meta diária;
- configuração dos dias obrigatórios;
- persistência de dados em JSON;
- consulta de feriados nacionais;
- exibição no dashboard quando o dia atual é feriado;
- configuração para exigir ou não estudo em feriados.

## Regras principais do sistema

- a streak considera apenas os dias obrigatórios definidos pelo usuário;
- o usuário deve definir pelo menos 1 dia obrigatório por semana;
- a meta diária deve ser de pelo menos 20 minutos;
- a streak aumenta quando o tempo total estudado no dia atinge a meta diária;
- dias não obrigatórios não quebram a streak;
- apenas uma sessão pode ficar ativa por vez;
- tarefas são opcionais;
- sessões livres são permitidas;
- feriados nacionais podem ser considerados ou ignorados como dias obrigatórios;
- quando a opção **"Exigir estudo em feriados"** está desativada, feriados nacionais não quebram a streak.

## Tecnologias utilizadas

- Python 3
- Tkinter
- JSON
- Requests
- BrasilAPI
- Pytest
- Ruff
- GitHub Actions
- PyInstaller

## Integração com API pública

O StreakMind utiliza a **BrasilAPI** para consultar os feriados nacionais do Brasil.

Essa integração permite verificar se a data atual corresponde a um feriado nacional e utilizar essa informação tanto no dashboard quanto na lógica da streak.

O usuário pode configurar se deseja exigir estudo em feriados. Quando essa opção está desativada, os feriados nacionais não são considerados dias obrigatórios e não quebram a streak.

Endpoint utilizado:

```text
https://brasilapi.com.br/api/feriados/v1/{ano}
```

## Persistência de dados

Os dados do usuário são armazenados localmente em formato JSON.

No Windows, o StreakMind utiliza a pasta de dados do usuário:

```text
%APPDATA%\StreakMind\dados.json
```

O arquivo armazena informações como:

- tarefas;
- sessões de estudo;
- configurações;
- dados da streak.


## Executando pelo código-fonte

### 1. Clonar o repositório

```bat
git clone https://github.com/Priantiz/StreakMind.git
cd StreakMind
```

### 2. Criar o ambiente virtual

```bat
python -m venv venv
```

### 3. Ativar o ambiente virtual

```bat
venv\Scripts\activate
```

### 4. Instalar as dependências

```bat
python -m pip install -r requirements.txt
```

### 5. Executar a aplicação

```bat
python src/main.py
```

## Executável para Windows

O StreakMind também pode ser distribuído como um único arquivo `.exe`, criado com PyInstaller.

O executável disponível na seção de Releases permite utilizar a aplicação sem instalar Python, VS Code ou as dependências manualmente.

A separação do projeto funciona da seguinte forma:

```text
Código-fonte
    ↓
Repositório GitHub

Aplicação pronta para uso
    ↓
GitHub Releases
    ↓
StreakMind.exe
```

## Gerando o executável

Para reconstruir o executável a partir do código-fonte, instale o PyInstaller:

```bat
python -m pip install pyinstaller
```

Em seguida, execute na raiz do projeto:

```bat
pyinstaller --clean --onefile --windowed --name StreakMind --icon=assets\StreakMind.ico --paths src src\main.py
```

O executável será gerado em:

```text
dist\StreakMind.exe
```

## Testes automatizados

Para executar os testes:

```bat
python -m pytest tests
```

## Lint

Para executar a análise estática do código com Ruff:

```bat
python -m ruff check src tests
```

## Integração contínua

O projeto utiliza **GitHub Actions** para executar automaticamente verificações de qualidade do código.

A pipeline realiza:

- instalação das dependências;
- execução do Ruff;
- execução dos testes automatizados.

As verificações são executadas automaticamente a partir das alterações enviadas ao repositório.

## Estrutura geral do projeto

```text
StreakMind/
├── .github/
│   └── workflows/
├── assets/
│   └── StreakMind.ico
├── docs/
├── src/
│   ├── models/
│   ├── services/
│   ├── storage/
│   ├── ui/
│   └── main.py
├── tests/
├── .gitignore
├── README.md
├── requirements.txt
└── StreakMind.spec
```

## Versionamento

Versão atual:

```text
1.2.0
```
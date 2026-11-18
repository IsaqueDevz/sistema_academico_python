# Sistema Acadêmico

> Sistema acadêmico em Python para cadastro de estudantes, disciplinas e notas, com emissão de ficha acadêmica. Desenvolvido para o **Técnico em Informática para Internet (TIPI)** do **Instituto Federal do Espírito Santo, Campus Colatina** por Isaque Neves Marriel.

O sistema tem duas formas de uso: um **menu no terminal** e uma **interface web** feita com Flask.

---

## Funcionalidades

- Cadastro de estudante com nome, matrícula, curso, turma e CPF
- Validação de CPF, matrícula, curso e turma
- Cadastro de disciplinas do curso escolhido
- Registro da nota final de cada disciplina (0 a 10)
- Situação por disciplina:

| Nota final | Situação |
|:---:|---|
| 10 | Aprovado com distinção |
| 6 a menos de 10 | Aprovado |
| Abaixo de 6 | Reprovado |

- Situação final do estudante, pela quantidade de reprovações:

| Disciplinas reprovadas | Situação final |
|:---:|---|
| Nenhuma | Passou de ano direto |
| Uma ou duas | Passou de ano com dependência |
| Mais de duas | Retido |

- Ficha acadêmica completa

---

## Tecnologias

| Tecnologia | Uso |
|---|---|
| ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white) | Linguagem principal |
| ![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white) | Interface web |
| ![validate-docbr](https://img.shields.io/badge/validate--docbr-validação_de_CPF-1e7b34) | Validação de CPF |

---

## Estrutura do projeto

```
sistema/
├── main.py              # Menu no terminal
├── app.py               # Interface web (Flask)
├── lib/
│   ├── arquivo/
│   │   └── __init__.py  # Cadastros, notas e ficha
│   └── interface/
│       └── __init__.py  # Menu do terminal
├── static/
│   └── ifes.png         # Logo
└── templates/
    └── index.html       # Página da interface web
```

---

## Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- pip

---

## Instalação

**1. Clone o repositório e entre na pasta:**

```bash
git clone https://github.com/seu-usuario/sistema-academico.git
cd sistema-academico
```

**2. Crie e ative um ambiente virtual (recomendado):**

```bash
python -m venv venv
```

No **Windows**:

```bash
venv\Scripts\activate
```

No **Linux** ou **macOS**:

```bash
source venv/bin/activate
```

**3. Instale as bibliotecas necessárias:**

```bash
pip install flask validate-docbr
```

Ou, usando o `requirements.txt`:

```txt
flask
validate-docbr
```

```bash
pip install -r requirements.txt
```

---

## Como usar

### Terminal

```bash
python main.py
```

### Interface web

```bash
python app.py
```

Depois acesse **http://127.0.0.1:5000** no navegador.

---

## Observações

- O sistema trabalha com **um estudante por vez**. Os dados ficam em memória e são perdidos ao encerrar o programa.
- O limite de **5 disciplinas** é controlado pela interface web. No terminal, ainda não há esse limite.
- Use **dados fictícios** nos testes.

---

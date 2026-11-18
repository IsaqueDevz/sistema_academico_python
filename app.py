import builtins
import io
from contextlib import redirect_stdout

from flask import Flask, render_template, request, flash, redirect, url_for

import lib.arquivo as arq

app = Flask(__name__)
app.secret_key = "troque-esta-chave"

LIMITE_DISCIPLINAS = 5
ROTULOS_ESTUDANTE = ["Nome", "Matrícula", "Curso", "Turma", "CPF"]


class SemResposta(Exception):
    pass


def executar(funcao, *respostas):
    fila = list(respostas)

    def input_falso(prompt=""):
        if not fila:
            raise SemResposta()
        return fila.pop(0)

    saida = io.StringIO()
    input_original = builtins.input
    builtins.input = input_falso

    try:
        with redirect_stdout(saida):
            funcao()
        return True, ""
    except SemResposta:
        linhas = [l.strip() for l in saida.getvalue().splitlines() if l.strip()]
        return False, (linhas[-1] if linhas else "Valor inválido.")
    finally:
        builtins.input = input_original


def limpar():
    arq.estudante.clear()
    arq.disciplinas.clear()
    arq.notas.clear()
    arq.situacaodisciplina.clear()


@app.route("/")
def index():
    tem_estudante = len(arq.estudante) >= 5
    notas_lancadas = len(arq.estudante) > 5

    dados = list(zip(ROTULOS_ESTUDANTE, arq.estudante[:5])) if tem_estudante else []

    linhas = []
    situacao_final = None
    if notas_lancadas:
        linhas = [(d, arq.notas[d], arq.situacaodisciplina[d]) for d in arq.disciplinas]
        situacao_final = arq.situacao_estudante()

    return render_template(
        "index.html",
        tem_estudante=tem_estudante,
        dados=dados,
        disciplinas=arq.disciplinas,
        limite=LIMITE_DISCIPLINAS,
        notas_lancadas=notas_lancadas,
        linhas=linhas,
        situacao_final=situacao_final,
    )


@app.post("/estudante")
def post_estudante():
    if arq.estudante:
        flash("Já existe um estudante. Use 'Novo estudante' para recomeçar.", "erro")
        return redirect(url_for("index"))

    f = request.form
    etapas = [
        ("Nome", arq.cadnome, f.get("nome", "")),
        ("Matrícula", arq.cadmatricula, f.get("matricula", "")),
        ("Curso", arq.cadcurso, f.get("curso", "")),
        ("Turma", arq.cadturma, f.get("turma", "")),
        ("CPF", arq.cadcpf, f.get("cpf", "")),
    ]

    for rotulo, funcao, valor in etapas:
        ok, msg = executar(funcao, valor)
        if not ok:
            limpar()
            flash(f"{rotulo}: {msg}", "erro")
            return redirect(url_for("index"))

    flash("Estudante cadastrado!", "ok")
    return redirect(url_for("index"))


@app.post("/disciplina")
def post_disciplina():
    nome = request.form.get("disciplina", "").strip().upper()

    if not arq.estudante:
        flash("Cadastre um estudante antes de adicionar disciplinas.", "erro")
    elif len(arq.estudante) > 5:
        flash("As notas já foram lançadas.", "erro")
    elif len(arq.disciplinas) >= LIMITE_DISCIPLINAS:
        flash(f"O limite é de {LIMITE_DISCIPLINAS} disciplinas.", "erro")
    elif nome in arq.disciplinas:
        flash("Essa disciplina já foi cadastrada.", "erro")
    else:
        ok, msg = executar(arq.cadastrar_disciplina, nome)
        if ok:
            flash("Disciplina cadastrada!", "ok")
        else:
            flash(msg, "erro")

    return redirect(url_for("index"))


@app.post("/notas")
def post_notas():
    if not arq.estudante:
        flash("Cadastre um estudante antes de lançar notas.", "erro")
        return redirect(url_for("index"))

    if len(arq.estudante) > 5:
        flash("As notas já foram lançadas.", "erro")
        return redirect(url_for("index"))

    if len(arq.disciplinas) != LIMITE_DISCIPLINAS:
        flash(f"Cadastre as {LIMITE_DISCIPLINAS} disciplinas antes de lançar as notas.", "erro")
        return redirect(url_for("index"))

    valores = []
    for idx, disciplina in enumerate(arq.disciplinas):
        bruto = request.form.get(f"nota_{idx}", "").strip().replace(",", ".")
        try:
            nota = float(bruto)
        except ValueError:
            flash(f"Nota de {disciplina} inválida: digite um número.", "erro")
            return redirect(url_for("index"))

        if not 0 <= nota <= 10:
            flash(f"A nota de {disciplina} deve estar entre 0 e 10.", "erro")
            return redirect(url_for("index"))

        valores.append(str(nota))

    ok, msg = executar(arq.cadastrar_notas, *valores)
    if ok:
        flash("Notas cadastradas!", "ok")
    else:
        flash(msg, "erro")

    return redirect(url_for("index"))


@app.post("/novo")
def novo():
    limpar()
    flash("Pronto para cadastrar um novo estudante.", "ok")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
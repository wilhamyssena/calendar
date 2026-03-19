from flask import Flask, render_template, request, redirect
from database import criar_tabela
from models import inserir_pessoa, buscar_por_mes
import calendar

app = Flask(__name__)

criar_tabela()


@app.route("/")
def home():

    mes_atual = 12 #temporario

    pessoas = buscar_por_mes(mes_atual)

    return render_template("lista_mes.html", pessoas=pessoas, mes=mes_atual)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form["nome"]
        dia = request.form["dia"]
        mes = request.form["mes"]
        whatsapp = request.form["whatsapp"]
        instagram = request.form["instagram"]

        inserir_pessoa(nome, dia, whatsapp, instagram)

        return redirect("/")
    
    return render_template("cadastro.html")


@app.route("/calendario/<int:mes>")
def calendario(mes):

    ano = 2026

    cal = calendar.monthcalendar(ano, mes)

    pessoas = buscar_por_mes(mes)

    # Organizar pessoas por dia
    pessoas_por_dia = {}

    for nome, dia in pessoas:
        if dia not in pessoas_por_dia:
            pessoas_por_dia[dia] = []
        pessoas_por_dia[dia].append(nome)

    return render_template(
        "calendario_mes.html",
        calendario=cal,
        pessoas_por_dia=pessoas_por_dia,
        mes=mes
    )

if __name__ == "__main__":
    app.run(debug=True)
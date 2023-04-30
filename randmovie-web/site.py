from flask import Flask, render_template, request, \
    redirect, session, flash, url_for
from randmovie_main import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gerar_aleatorio', methods=['GET', ])
def gerar():
    lista_filmes = listar_filmes()
    lista_aleatoria = lista_aleatoria_func(lista_filmes)
    print('rodando agr...')
    saida = rodar(lista_aleatoria)
    return saida


@app.route('/gerar_rate', methods=['POST', ])
def gerar_rate():
    return "OK, gerar rate"


@app.route('/gerar_genero', methods=['POST', ])
def gerar_genero():
    return "OK, gerar genero"


@app.route('/gerar_rate_aleatorio', methods=['POST', ])
def gerar_rate_aleatorio():
    return "OK, gerar rate genero"


app.run(debug=True, port=80)

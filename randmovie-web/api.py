import json

from flask import Flask, render_template, request, make_response
from randmovie_main import *
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def renderizar_filme(filme_saida):
    if filme_saida:
        titulo = filme_saida['original_title']
        sinopse_ingles_from_dict = filme_saida['overview']
        if not sinopse_ingles_from_dict:
            sinopse_ingles_from_dict = "Não encontrado"
        rate = filme_saida['vote_average']
        genero = get_genero_filme(filme_saida)['name']
        jpg = filme_saida['poster_path']
        return render_template('filme.html', titulo=titulo, sinopse=sinopse_ingles_from_dict,
                               rate=rate, genero=genero, jpg=jpg)
    if not filme_saida:
        return render_template('filme.html', titulo="titulo_teste", sinopse="sinopse_teste", rate="9.985",
                               genero="Muita comedia",
                               jpg="https://image.tmdb.org/t/p/w600_and_h900_bestv2//9MHZ2sALxREoLFVjGh7ueaSIVoJ.jpg")


@app.route('/gerar_aleatorio', methods=['GET', ])
def gerar_api():
    lista_filmes = listar_filmes()
    lista_aleatoria = lista_aleatoria_func(lista_filmes)
    saida = rodar(lista_aleatoria, server_mode=True)
    return saida


@app.route('/opcoes_genero', methods=['GET', ])
def opcoes_genero():
    list_genero = []
    for i in get_genre():
        list_genero.append(i)
    return list_genero


@app.route('/gerar_aleatorio_rate_genero', methods=['POST', ])
def gerar_aleatorio_rate_genero():
    try:
        body = request.get_data()
        body_json = json.loads(body)
        rate = body_json.get('rate')
        genero = body_json.get('genero')
        if not rate and rate != 0:
            if not genero:
                return make_response({'result': 'rate invalido disgraaaaaça'}, 400)
        if not rate and rate != 0:
            lista_filmes = listar_filmes_genero(genero)
            lista_aleatoria = lista_aleatoria_func(lista_filmes)
            saida = rodar(lista_aleatoria, server_mode=True)
            return saida
        if not genero:
            if 0 <= rate <= 10:
                lista_filmes = listar_filmes_rate(int(rate))
                lista_aleatoria = lista_aleatoria_func(lista_filmes)
                saida = rodar(lista_aleatoria, server_mode=True)
                return saida
            else:
                return make_response({'result': 'rate invalido disgraaaaaça'}, 400)
        if rate and genero:
            if 1 <= rate <= 10:
                genero = genero.lower()
                lista_filmes = listar_filmes_rate_genero(rate, genero)
                lista_aleatoria = lista_aleatoria_func(lista_filmes)
                saida = rodar(lista_aleatoria, server_mode=True)
                return saida
            else:
                return make_response({'result': 'rate invalido disgraaaaaça'}, 400)
        else:
            return make_response({'result': 'json incorreto'}, 400)
    except Exception as E:
        return make_response({'result': 'json incorreto', "error": E}, 400)


app.run(host='0.0.0.0', port=80)

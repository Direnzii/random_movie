import json

from flask import Flask, render_template, request, make_response
from randmovie_main import *

app = Flask(__name__)


def renderizar_filme(filme_saida, just_api=False):
    if filme_saida:
        titulo = filme_saida['original_title']
        sinopse_ingles_from_dict = filme_saida['overview']
        if not sinopse_ingles_from_dict:
            sinopse_ingles_from_dict = "Não encontrado"
        rate = filme_saida['vote_average']
        genero = get_genero_filme(filme_saida)['name']
        jpg = filme_saida['poster_path']
        if just_api:
            saida = [titulo, sinopse_ingles_from_dict, rate, genero,
                     f"https://image.tmdb.org/t/p/w600_and_h900_bestv2/{jpg}"]
            return saida
        if not just_api:
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
    return renderizar_filme(saida, just_api=True)


@app.route('/opcoes_genero', methods=['GET', ])
def opcoes_genero():
    return get_genre()


@app.route('/gerar_aleatorio_rate_genero', methods=['POST', ])
def gerar_aleatorio_rate_genero():
    try:
        body = request.get_data()
        body_json = json.loads(body)
        rate = body_json.get('rate')
        genero = body_json.get('genero')
        if not rate:
            if not genero:
                return make_response({'result': 'rate invalido disgraaaaaça'}, 400)
        if not rate:
            lista_filmes = listar_filmes_genero(genero)
            lista_aleatoria = lista_aleatoria_func(lista_filmes)
            saida = rodar(lista_aleatoria, server_mode=True)
            return renderizar_filme(saida, just_api=True)
        if not genero:
            if 1 <= rate <= 10:
                lista_filmes = listar_filmes_rate(rate)
                lista_aleatoria = lista_aleatoria_func(lista_filmes)
                saida = rodar(lista_aleatoria, server_mode=True)
                return renderizar_filme(saida, just_api=True)
            else:
                return make_response({'result': 'rate invalido disgraaaaaça'}, 400)
        if rate and genero:
            if 1 <= rate <= 10:
                genero = genero.lower()
                lista_filmes = listar_filmes_rate_genero(rate, genero)
                lista_aleatoria = lista_aleatoria_func(lista_filmes)
                saida = rodar(lista_aleatoria, server_mode=True)
                return renderizar_filme(saida, just_api=True)
            else:
                return make_response({'result': 'rate invalido disgraaaaaça'}, 400)
        else:
            return make_response({'result': 'json incorreto'}, 400)
    except:
        return make_response({'result': 'json incorreto'}, 400)


app.run(host='0.0.0.0', port=80)
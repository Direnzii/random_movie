from flask import Flask, render_template, request, \
    redirect, session, flash, url_for
from randmovie_main import *

app = Flask(__name__)

sinopse_teste = """Mauris ullamcorper turpis varius, porta justo vel, suscipit mauris. Maecenas dictum elit leo, 
a eleifend justo pellentesque sit amet. Nullam pharetra auctor nibh. Praesent placerat aliquet metus, vel auctor 
nisi sollicitudin ac. Integer dignissim magna risus, nec dignissim purus elementum. """

titulo_teste = """Donec tempus cursus tristique. Nullam pulvinar auctor nibh sit amet."""


def renderizar_filme(filme_saida):  # filme_saida
    titulo = filme_saida['original_title']
    sinopse_ingles_from_dict = filme_saida['overview']
    if not sinopse_ingles_from_dict:
        sinopse_ingles_from_dict = "Não encontrado"
    rate = filme_saida['vote_average']
    genero = get_genero_filme(filme_saida)['name']
    jpg = filme_saida['poster_path']
    return render_template('filme.html', titulo=titulo, sinopse=sinopse_ingles_from_dict, rate=rate, genero=genero, jpg=jpg)
    # return render_template('filme.html', titulo=titulo_teste, sinopse=sinopse_teste, rate="9.985",
    #                        genero="Muita comedia",
    #                        jpg="https://image.tmdb.org/t/p/w600_and_h900_bestv2//9MHZ2sALxREoLFVjGh7ueaSIVoJ.jpg")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gerar_aleatorio', methods=['GET', ])
def gerar():
    lista_filmes = listar_filmes()
    lista_aleatoria = lista_aleatoria_func(lista_filmes)
    render_template('index.html', loading=True)
    saida = rodar(lista_aleatoria, server_mode=True)
    return renderizar_filme(saida)
    # return renderizar_filme()


@app.route('/gerar_rate', methods=['GET', ])
def gerar_rate():
    return """OK, gerar rate EM MANUTENÇÃO...<br><button onclick="window.location.href='/'">Back</button>"""


@app.route('/gerar_genero', methods=['GET', ])
def gerar_genero():
    return """OK, gerar genero EM MANUTENÇÃO...<br><button onclick="window.location.href='/'">Back</button>"""


@app.route('/gerar_rate_aleatorio', methods=['GET', ])
def gerar_rate_aleatorio():
    return """OK, gerar rate genero EM MANUTENÇÃO...<br><button onclick="window.location.href='/'">Back</button>"""


app.run(host='0.0.0.0', port=80)

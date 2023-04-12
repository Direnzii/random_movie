from flask import Flask, render_template, request, \
    redirect, session, flash, url_for

# class Jogo:
#     def __init__(self, nome, categoria, console):
#         self.nome=nome
#         self.categoria=categoria
#         self.console=console
#
# jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
# jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
# jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
# lista = [jogo1, jogo2, jogo3]
#
# class Usuario:
#     def __init__(self, nome, nickname, senha):
#         self.nome = nome
#         self.nickname = nickname
#         self.senha = senha

# usuario1 = Usuario("Bruno Divino", "BD", "alohomora")
# usuario2 = Usuario("Camila Ferreira", "Mila", "paozinho")
# usuario3 = Usuario("Guilherme Louro", "Cake", "python_eh_vida")
#
# usuarios = { usuario1.nickname : usuario1,
#              usuario2.nickname : usuario2,
#              usuario3.nickname : usuario3 }

app = Flask(__name__)
# app.secret_key = 'alura'

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/novo')
# def novo():
#     if 'usuario_logado' not in session or session['usuario_logado'] == None:
#         return redirect(url_for('login', proxima=url_for('novo')))
#     return render_template('novo.html', titulo='Novo Jogo')

@app.route('/gerar-aleatorio', methods=['POST',])
def gerar():
    # nome = request.form['nome']
    # categoria = request.form['categoria']
    # console = request.form['console']
    # jogo = Jogo(nome, categoria, console)
    # lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/gerar-rate', methods=['POST',])
def gerar_rate():
    # nome = request.form['nome']
    # categoria = request.form['categoria']
    # console = request.form['console']
    # jogo = Jogo(nome, categoria, console)
    # lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/gerar-genero', methods=['POST',])
def gerar_genero():
    # nome = request.form['nome']
    # categoria = request.form['categoria']
    # console = request.form['console']
    # jogo = Jogo(nome, categoria, console)
    # lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/gerar-full', methods=['POST',])
def gerar_full():
    # nome = request.form['nome']
    # categoria = request.form['categoria']
    # console = request.form['console']
    # jogo = Jogo(nome, categoria, console)
    # lista.append(jogo)
    return redirect(url_for('sla'))

@app.route('/sla')
def sla ():
    return 'botão clicado'
# @app.route('/login')
# def login():
#     proxima = request.args.get('proxima')
#     return render_template('login.html', proxima=proxima)
#
# @app.route('/autenticar', methods=['POST',])
# def autenticar():
#     if request.form['usuario'] in usuarios:
#         usuario = usuarios[request.form['usuario']]
#         if request.form['senha'] == usuario.senha:
#             session['usuario_logado'] = usuario.nickname
#             flash(usuario.nickname + ' logado com sucesso!')
#             proxima_pagina = request.form['proxima']
#             return redirect(proxima_pagina)
#     else:
#         flash('Usuário não logado.')
#         return redirect(url_for('login'))
#
# @app.route('/logout')
# def logout():
#     session['usuario_logado'] = None
#     flash('Logout efetuado com sucesso!')
#     return redirect(url_for('index'))
#
app.run(debug=True, port=80)
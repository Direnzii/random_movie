import requests
import random
import os

token = os.getenv(key="CHAVE_API_FILME")
filme = {}


def get_genero_filme(filme_gen):
    genero = filme_gen['genres'][0]
    if not genero:
        sem_genero = 'Não localizado'
        return sem_genero
    else:
        return genero


def printar_generos():
    saida = ''
    dict_gen = get_genre_name()
    for name in dict_gen:
        saida += name + ", "
    n = 2
    final_str = ""
    for i in range(len(saida) - n):
        final_str = final_str + saida[i]
    print(final_str)


def get_genre_name():
    list_gen = []
    dict_name_gen = get_genre()
    for i in dict_name_gen:
        list_gen.append(i)
    return list_gen


def get_genre():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={token}"
    full = requests.get(url).json()['genres']
    dict_genero = {}
    genero_string = ''
    list_id = []
    for genre in full:
        genero = genre["name"]
        id_gen: int = genre["id"]
        dict_genero.update({genero.lower(): id_gen})
        genero_string += genero + ','
        list_id.append(id_gen)
    return dict_genero


def numero_aleatorio():
    numero_aleatorio_full = random.randrange(1, 501)
    return numero_aleatorio_full


def chunks(lista):
    for i in range(0, len(lista), 4):
        yield lista[i:i + 4]


def lista_aleatoria_func(lista):
    lista = list(chunks(lista))
    count_list = len(lista)
    numero = random.randrange(0, count_list)
    list_aleatoria = lista[numero]
    return list_aleatoria


def requisicao(url):
    requisicao_url = requests.get(url)
    json = requisicao_url.json()
    return json


def listar_filmes_rate_genero(rate, genero):
    while True:
        lista_filmes = []
        genero_id = get_genre()
        genero_id = genero_id[f'{genero}']
        url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                    f"api_key={token}&" \
                    "include_adult=false&" \
                    "include_video=false&" \
                    f"page={numero_aleatorio()}&" \
                    f"vote_average.gte={rate}&" \
                    f"with_genres={genero_id}"
        filmes = requisicao(url_geral)
        filmes = filmes['results']
        if not filmes:
            continue
        else:
            for movie in filmes:
                id_movie_1 = movie['id']
                lista_filmes.append(id_movie_1)
            return lista_filmes


def listar_filmes_genero(genero):
    while True:
        lista_filmes = []
        genero_id = get_genre()
        genero_id = genero_id[f'{genero}']
        url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                    f"api_key={token}&" \
                    "include_adult=false&" \
                    "include_video=false&" \
                    f"page={numero_aleatorio()}&" \
                    f"with_genres={genero_id}"
        filmes = requisicao(url_geral)
        filmes = filmes['results']
        if not filmes:
            continue
        else:
            for movie in filmes:
                id_movie_2 = movie['id']
                lista_filmes.append(id_movie_2)
            return lista_filmes


def listar_filmes_rate(rate):
    while True:
        lista_filmes = []
        url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                    f"api_key={token}&" \
                    "include_adult=false&" \
                    "include_video=false&" \
                    f"page={numero_aleatorio()}&" \
                    f"vote_average.gte={rate}"
        filmes = requisicao(url_geral)
        filmes = filmes['results']
        if not filmes:
            continue
        else:
            for movie in filmes:
                id_movie_3 = movie['id']
                lista_filmes.append(id_movie_3)
            return lista_filmes


def listar_filmes():
    while True:
        lista_filmes = []
        url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                    f"api_key={token}&" \
                    "include_adult=false&" \
                    "include_video=false&" \
                    f"page={numero_aleatorio()}"
        filmes = requisicao(url_geral)
        filmes = filmes['results']
        if not filmes:
            continue
        else:
            for movie in filmes:
                id_movie_4 = movie['id']
                lista_filmes.append(id_movie_4)
            return lista_filmes


def rodar(lista_filmes, server_mode=False):
    i = True
    while i:
        try:
            count_movies = len(lista_filmes)
            random_id = random.randrange(0, count_movies)
            id_filme = lista_filmes[random_id]

            url_filme = f"https://api.themoviedb.org/3/movie/{id_filme}?" \
                        f"api_key={token}"
            filme_requi = requisicao(url_filme)

            nome = filme_requi['original_title']
            sinopse_ingles_from_dict = filme_requi['overview']
            genero = get_genero_filme(filme_requi)
            imagem = filme_requi['poster_path']
            requisicao_imagem = f"https://image.tmdb.org/t/p/w600_and_h900_bestv2{imagem}"
            if not sinopse_ingles_from_dict:
                sinopse_ingles_from_dict = "Não encontrado"
            votos = filme_requi['vote_average']
            print("*******************\n*** SEU FILME É ***")
            print('Nome: ', nome, '\nSinopse: ', sinopse_ingles_from_dict, '\nGenero: ', genero, '\nMédia de votos: ', votos)
            print(requisicao_imagem)
            # input("Pressione enter para uma nova busca ...")
            saida = ''
            saida += "*******************\n*** SEU FILME É ***<br>"
            saida += f"\n'Nome: ', {nome}, '\nSinopse: ', {sinopse_ingles_from_dict}, '\n" \
                     f"Genero: ', {genero}, '\nMédia de votos: ', {votos}<br>"
            saida += requisicao_imagem
            os.system('cls' if os.name == 'nt' else 'clear')
            i = False
            if server_mode:
                return filme_requi
            return saida  # saida
        except ValueError:
            continue


def error():
    a = 0 / 0
    return a


def banner():
    print("▛▀▘▗▜            ▜       ▐        ▗       ▌    ▀▛▘▌  ▗\n"
          "▙▄ ▄▐ ▛▚▀▖▞▀▖ ▝▀▖▐ ▞▀▖▝▀▖▜▀ ▞▀▖▙▀▖▄ ▞▀▖ ▞▀▌▞▀▖  ▌ ▛▀▖▄ ▝▀▖▞▀▌▞▀▖\n"
          "▌  ▐▐ ▌▐ ▌▛▀  ▞▀▌▐ ▛▀ ▞▀▌▐ ▖▌ ▌▌  ▐ ▌ ▌ ▌ ▌▌ ▌  ▌ ▌ ▌▐ ▞▀▌▚▄▌▌ ▌\n"
          "▘  ▀▘▘▘▝ ▘▝▀▘ ▝▀▘ ▘▝▀▘▝▀▘ ▀ ▝▀ ▘  ▀▘▝▀  ▝▀▘▝▀   ▘ ▘ ▘▀▘▝▀▘▗▄▘▝▀")


def main():
    banner()
    while True:
        print(
            "**********************\n***DIGITE UMA OPÇÃO***\n(1) - Aleatório\n(2) - Por rate\n"
            "(3) - Por gênero\n(4) - Por rate e gênero")
        try:
            opcao = int(input('Insira aqui: '))
            if opcao == 1:
                lista_filmes = listar_filmes()
                lista_aleatoria = lista_aleatoria_func(lista_filmes)
                rodar(lista_aleatoria)
            elif opcao == 2:
                rate = int(input("Insira um rate minimo para a busca, de 1 a 10: "))
                if 1 <= rate <= 10:
                    lista_filmes = listar_filmes_rate(rate)
                    lista_aleatoria = lista_aleatoria_func(lista_filmes)
                    rodar(lista_aleatoria)
                else:
                    print("Rate inválido, fechando !!")
            elif opcao == 3:
                print("*************************\n***Generos disponiveis***")
                printar_generos()
                genero = input("Insira um gênero valido: ")
                genero = genero.lower()
                lista_filmes = listar_filmes_genero(genero)
                lista_aleatoria = lista_aleatoria_func(lista_filmes)
                rodar(lista_aleatoria)
            elif opcao == 4:
                rate = int(input("Insira um rate minimo para a busca, de 1 a 10: "))
                if 1 <= rate <= 10:
                    print("*************************\n***Generos disponiveis***")
                    printar_generos()
                    genero = input("Insira um gênero valido: ")
                    genero = genero.lower()
                    print("Esta é uma busca específica, pode demorar alguns segundos...")
                    lista_filmes = listar_filmes_rate_genero(rate, genero)
                    lista_aleatoria = lista_aleatoria_func(lista_filmes)
                    rodar(lista_aleatoria)
                else:
                    print("rate inválido, insira um numero de 1 a 10 !!")
            else:
                error()
        except ValueError:
            print("Não existe essa opção !!")


if __name__ == '__main__':
    main()

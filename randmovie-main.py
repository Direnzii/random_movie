import requests
import random
import os
class AssistirFilme():
    token = os.getenv(key="CHAVE_API_FILME")
    filme = {}
    def get_genero_filme(self):
        genero = self.filme['genres'][0]
        if not genero:
            sem_genero = 'Não localizado'
            return sem_genero
        else:
            return genero['name']
    def printar_generos(self):
        saida = ''
        dict = self.get_genre_name()
        for name in dict:
            saida += name + ", "
        n = 2
        final_str = ""
        for i in range(len(saida) - n):
            final_str = final_str + saida[i]
        print(final_str)
    def get_genre_name(self):
        list = []
        dict = self.get_genre()
        for i in dict:
            list.append(i)
        return list
    def get_genre(self):
        url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.token}"
        full = requests.get(url).json()['genres']
        dict_genero = {}
        for genre in full:
            genero = genre["name"]
            id: int = genre["id"]
            dict_genero.update({genero.lower(): id})
        return dict_genero
    def numero_aleatorio(self):
        numero_aleatorio = random.randrange(1, 501)
        return numero_aleatorio
    def chunks(self, lista):
        for i in range(0, len(lista), 4):
            yield lista[i:i + 4]
    def lista_aleatoria(self, lista):
        lista = list(self.chunks(lista))
        count_list = len(lista)
        numero = random.randrange(0, count_list)
        list_aleatoria = lista[numero]
        return list_aleatoria
    def requisicao(self, url):
        requisicao = requests.get(url)
        json = requisicao.json()
        return json
    def listar_filmes_rate_genero(self, rate, genero):
        while True:
            lista_filmes = []
            genero_id = self.get_genre()
            genero_id = genero_id[f'{genero}']
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}&" \
                        f"vote_average.gte={rate}&" \
                        f"with_genres={genero_id}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes
    def listar_filmes_genero(self, genero):
        while True:
            lista_filmes = []
            genero_id = self.get_genre()
            genero_id = genero_id[f'{genero}']
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}&" \
                        f"with_genres={genero_id}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes
    def listar_filmes_rate(self, rate):
        while True:
            lista_filmes = []
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}&" \
                        f"vote_average.gte={rate}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes
    def listar_filmes(self):
        while True:
            lista_filmes = []
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes
    def rodar(self, lista_filmes):
        i = True
        while i:
            try:
                count_movies = len(lista_filmes)
                random_id = random.randrange(0, count_movies)
                id_filme = lista_filmes[random_id]

                url_filme = f"https://api.themoviedb.org/3/movie/{id_filme}?" \
                            f"api_key={self.token}"
                self.filme = self.requisicao(url_filme)

                nome = self.filme['original_title']
                sinopse = self.filme['overview']
                genero = self.get_genero_filme()
                imagem = self.filme['poster_path']
                requisicao_imagem = f"https://image.tmdb.org/t/p/w600_and_h900_bestv2{imagem}"
                if not sinopse:
                    sinopse = "Não encontrado"
                votos = self.filme['vote_average']
                print("*******************\n*** SEU FILME É ***")
                print('Nome: ', nome, '\nSinopse: ', sinopse, '\nGenero: ', genero, '\nMédia de votos: ', votos)
                input("Pressione enter para uma nova busca ...")
                os.system('cls' if os.name == 'nt' else 'clear')
                i = False
            except Exception as e:
                continue
    def error(self):
        a = 0 / 0
        return a
    def banner(self):
        print("▛▀▘▗▜            ▜       ▐        ▗       ▌    ▀▛▘▌  ▗\n"
              "▙▄ ▄▐ ▛▚▀▖▞▀▖ ▝▀▖▐ ▞▀▖▝▀▖▜▀ ▞▀▖▙▀▖▄ ▞▀▖ ▞▀▌▞▀▖  ▌ ▛▀▖▄ ▝▀▖▞▀▌▞▀▖\n"
              "▌  ▐▐ ▌▐ ▌▛▀  ▞▀▌▐ ▛▀ ▞▀▌▐ ▖▌ ▌▌  ▐ ▌ ▌ ▌ ▌▌ ▌  ▌ ▌ ▌▐ ▞▀▌▚▄▌▌ ▌\n"
              "▘  ▀▘▘▘▝ ▘▝▀▘ ▝▀▘ ▘▝▀▘▝▀▘ ▀ ▝▀ ▘  ▀▘▝▀  ▝▀▘▝▀   ▘ ▘ ▘▀▘▝▀▘▗▄▘▝▀")


def main():
    aleatorio = AssistirFilme()
    aleatorio.banner()
    while True:
        print("**********************\n***DIGITE UMA OPÇÃO***\n(1) - Aleatório\n(2) - Por rate\n(3) - Por gênero\n(4) - Por rate e gênero")
        try:
            opcao = int(input('Insira aqui: '))
            if opcao == 1:
                lista_filmes = aleatorio.listar_filmes()
                lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
                aleatorio.rodar(lista_aleatoria)
            elif opcao == 2:
                rate = int(input("Insira um rate minimo para a busca, de 1 a 10: "))
                if rate >= 1 and rate <=10:
                    lista_filmes = aleatorio.listar_filmes_rate(rate)
                    lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
                    aleatorio.rodar(lista_aleatoria)
                else:
                    print("Rate inválido, fechando !!")
            elif opcao == 3:
                print("*************************\n***Generos disponiveis***")
                aleatorio.printar_generos()
                genero = input("Insira um gênero valido: ")
                genero = genero.lower()
                lista_filmes = aleatorio.listar_filmes_genero(genero)
                lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
                aleatorio.rodar(lista_aleatoria)
            elif opcao == 4:
                rate = int(input("Insira um rate minimo para a busca, de 1 a 10: "))
                if rate >= 1 and rate <=10:
                    print("*************************\n***Generos disponiveis***")
                    aleatorio.printar_generos()
                    genero = input("Insira um gênero valido: ")
                    genero = genero.lower()
                    print("Esta é uma busca específica, pode demorar alguns segundos...")
                    lista_filmes = aleatorio.listar_filmes_rate_genero(rate, genero)
                    lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
                    aleatorio.rodar(lista_aleatoria)
                    i = False
                else:
                    print("rate inválido, insira um numero de 1 a 10 !!")
            else:
                aleatorio.error()
        except Exception as e:
            print("Não existe essa opção !!")
        #input("Pressione enter para uma nova busca ...")
if __name__ == '__main__':
    main()
# aleatorio = AssistirFilme()
# a = aleatorio.printar_generos()  #PARA TESTES
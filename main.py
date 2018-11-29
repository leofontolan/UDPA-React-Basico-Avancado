# -*- coding: utf-8 -*-
from movie import Movie
from tvshow import TvShow
import fresh_tomatoes

#Instances of Movies and TVShow with data
movie_1 = Movie("Homem de Ferro",
                "2h 6m",
                "https://upload.wikimedia.org/wikipedia/pt/thumb/0/00/Iron_Man_poster.jpg/250px-Iron_Man_poster.jpg",
                "https://www.youtube.com/watch?v=rFKv3WRgSUs",
                "Um industrial bilionário e inventor brilhante que realiza testes bélicos no exterior",
                "2008")

movie_2 = Movie("À Procura da Felicidade ",
                "1h 57m",
                "https://upload.wikimedia.org/wikipedia/pt/thumb/1/1e/The_Pursuit_of_Happyness.jpg/200px-The_Pursuit_of_Happyness.jpg",
                "https://www.youtube.com/watch?v=6yc069E1gfc",
                "Chris Gardner enfrenta uma vida difícil. Despejado de seu apartamento. Ele vai em busca de seu sonho.",
                "2006")

movie_3 = Movie("Bohemian Rhapsody",
                "2h 13m",
                "https://upload.wikimedia.org/wikipedia/pt/thumb/2/2e/Bohemian_Rhapsody_poster.png/200px-Bohemian_Rhapsody_poster.png",
                "https://www.youtube.com/watch?v=GryRsVhOvxo",
                "Freddie Mercury, Brian May, Roger Taylor e John Deacon formam a banda de rock Queen em 1970.",
                "2018")


serie_1 = TvShow("Marseille",
                 "52 mim",
                 "http://br.web.img3.acsta.net/c_216_288/pictures/16/05/05/23/38/313077.jpg",
                 "https://www.youtube.com/watch?v=8WvqgV7-kSc",
                 "Robert Taro é o prefeito da cidade por 25 anos, e está prestes a enfrentar o homem que escolheu para ser seu herdeiro, nas próximas eleições.",
                 "1 Temporada",
                 "1 Episódio",
                 "Canal")

serie_2 = TvShow("Flash",
                 "42 mim",
                 "http://br.web.img2.acsta.net/c_216_288/pictures/17/09/29/21/15/4233147.jpg",
                 "https://www.youtube.com/watch?v=Yj0l7iGKh8g",
                 "Barry Allen (Grant Gustin) era um funcionário da Polícia Científica que, ao sofrer um acidente, foi banhado por produtos químicos em seu laboratório e, em seguida, atingido por um raio.",
                 "1 Temporada",
                 "1 Episódio",
                 "Canal")

serie_3 = TvShow("The Walking Dead",
                 "44 mim",
                 "http://br.web.img2.acsta.net/c_216_288/pictures/18/10/12/01/14/0550773.jpg",
                 "https://www.youtube.com/watch?v=R1v0uFms68U",
                 "Um apocalipse provoca uma infestação de zumbis na cidade de Cynthiana, em Kentucky, nos Estados Unidos, e o oficial de polícia Rick Grimes (Andrew Lincoln) descobre que os mortos-vivos estão se propagando progressivamente. ",
                 "1 Temporada",
                 "1 Episódio",
                 "Canal")

#Array with all movies
movies = [movie_1, movie_2, movie_3, serie_1, serie_2, serie_3]

#Call Fresh Tomatoes to genarate HTML file
fresh_tomatoes.open_movies_page(movies)

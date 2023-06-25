from modelo import *
import json 
import requests
from modelo import *
from ventana import *
class Manejador():
    def __init__(self):
        url = "https://api.themoviedb.org/3/discover/movie?api_key=1826cb1a64536061a0f390599631dc52"
        response = requests.get(url)
        data = response.json()
        self.__pelis = data["results"]
        self.__manejador=[]
    def carga_peliculas(self):
        for peli in self.__pelis:
            unapelicula=Pelicula(peli["title"],peli["overview"],peli["original_language"],peli["release_date"])
            for idGen in peli["genre_ids"]:
                unapelicula.carga_genero(idGen)
            self.__manejador.append(unapelicula)
    def Busca_Generos(self,ids):
        data = {
            "genres": [
            {"id": 28, "name": "Action"},
            {"id": 12, "name": "Adventure"},
            {"id": 16, "name": "Animation"},
            {"id": 35, "name": "Comedy"},
            {"id": 80, "name": "Crime"},
            {"id": 99, "name": "Documentary"},
            {"id": 18, "name": "Drama"},
            {"id": 10751, "name": "Family"},
            {"id": 14, "name": "Fantasy"},
            {"id": 36, "name": "History"},
            {"id": 27, "name": "Horror"},
            {"id": 10402, "name": "Music"},
            {"id": 9648, "name": "Mystery"},
            {"id": 10749, "name": "Romance"},
            {"id": 878, "name": "Science Fiction"},
            {"id": 10770, "name": "TV Movie"},
            {"id": 53, "name": "Thriller"},
            {"id": 10752, "name": "War"},
            {"id": 37, "name": "Western"}
            ]
        }
        lista=[]
        for genre in data["genres"]:
            genre_id = genre["id"]
            for i in range(len(ids)):
                if ids[i] == genre_id:
                    lista.append(genre["name"])

        return lista
    def getLista(self):
        return self.__manejador

if __name__ == '__main__':
    manejador = Manejador()
    manejador.carga_peliculas()
    app = Ventana(manejador)
    app.Ejecutar()
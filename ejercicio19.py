class Pelicula:
    def __init__(self, titulo, estudio, estreno):
        self.titulo = titulo
        self.estudio = estudio
        self.estreno = estreno


class PilaPeliculas:
    def __init__(self):
        self.pila = []

    def agregar_pelicula(self, pelicula):
        self.pila.append(pelicula)

    def peliculas_estrenadas_en_2014(self):
        print("Peliculas estrenadas en 2014:")
        for pelicula in self.pila:
            if pelicula.estreno == 2014:
                print(pelicula.titulo)

    def cantidad_peliculas_estrenadas_en_2018(self):
        contador = 0
        for pelicula in self.pila:
            if pelicula.estreno == 2018:
                contador += 1
        print("Cantidad de películas estrenadas en 2018:", contador)

    def peliculas_marvel_estrenadas_en_2016(self):
        print("Películas de Marvel Studios estrenadas en 2016:")
        for pelicula in self.pila:
            if pelicula.estreno == 2016 and pelicula.estudio == "Marvel Studios":
                print(pelicula.titulo)


# Ejemplo de uso
pila_peliculas = PilaPeliculas()

# Agregar peliculas a la pila
pelicula1 = Pelicula("Avengers: Age of Ultron", "Marvel Studios", 2015)
pelicula2 = Pelicula("Guardianes de la Galaxia", "Marvel Studios", 2014)
pelicula3 = Pelicula("Deadpool", "20th Century Fox", 2016)
pelicula4 = Pelicula("Captain America: Civil War", "Marvel Studios", 2016)
pelicula5 = Pelicula("Black Panther", "Marvel Studios", 2018)
pelicula6 = Pelicula("Thor: Ragnarok", "Marvel Studios", 2017)

pila_peliculas.agregar_pelicula(pelicula1)
pila_peliculas.agregar_pelicula(pelicula2)
pila_peliculas.agregar_pelicula(pelicula3)
pila_peliculas.agregar_pelicula(pelicula4)
pila_peliculas.agregar_pelicula(pelicula5)
pila_peliculas.agregar_pelicula(pelicula6)

# Mostrar peliculas estrenadas en 2014
pila_peliculas.peliculas_estrenadas_en_2014()

# Indicar cantidad de peliculas estrenadas en 2018
pila_peliculas.cantidad_peliculas_estrenadas_en_2018()

# Mostrar peliculas de Marvel Studios estrenadas en 2016
pila_peliculas.peliculas_marvel_estrenadas_en_2016()

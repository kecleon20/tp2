class PersonajeMCU:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas


class PilaPersonajesMCU:
    def __init__(self):
        self.pila = []

    def agregar_personaje(self, personaje):
        self.pila.append(personaje)

    def posicion_rocket_groot(self):
        posicion_rocket = None
        posicion_groot = None
        pila_auxiliar = []
        while not posicion_rocket or not posicion_groot:
            personaje = self.pila.pop()
            pila_auxiliar.append(personaje)
            if personaje.nombre == "Rocket Raccoon":
                posicion_rocket = len(self.pila) + 1
            elif personaje.nombre == "Groot":
                posicion_groot = len(self.pila) + 1
        while pila_auxiliar:
            personaje = pila_auxiliar.pop()
            self.pila.append(personaje)
        print("Posicion de Rocket Raccoon:", posicion_rocket)
        print("Posicion de Groot:", posicion_groot)

    def personajes_mas_de_5_peliculas(self):
        print("Personajes que participaron en mas de 5 peliculas:")
        for personaje in self.pila:
            if personaje.peliculas > 5:
                print(personaje.nombre, "- Peliculas:", personaje.peliculas)

    def participacion_black_widow(self):
        contador = 0
        for personaje in self.pila:
            if personaje.nombre == "Viuda Negra":
                contador += personaje.peliculas
        print("Viuda Negra participo en", contador, "peliculas")

    def mostrar_personajes_cdg(self):
        print("Personajes cuyos nombres empiezan con C, D y G:")
        for personaje in self.pila:
            if personaje.nombre[0] in ["C", "D", "G"]:
                print(personaje.nombre)


# Ejemplo de uso
pila_personajes = PilaPersonajesMCU()

# Agregar personajes a la pila
personaje1 = PersonajeMCU("Iron Man", 10)
personaje2 = PersonajeMCU("Captain America", 8)
personaje3 = PersonajeMCU("Thor", 7)
personaje4 = PersonajeMCU("Rocket Raccoon", 5)
personaje5 = PersonajeMCU("Groot", 6)
personaje6 = PersonajeMCU("Black Widow", 9)

pila_personajes.agregar_personaje(personaje1)
pila_personajes.agregar_personaje(personaje2)
pila_personajes.agregar_personaje(personaje3)
pila_personajes.agregar_personaje(personaje4)
pila_personajes.agregar_personaje(personaje5)
pila_personajes.agregar_personaje(personaje6)

# Determinar posicion de Rocket Raccoon y Groot
pila_personajes.posicion_rocket_groot()

# Determinar personajes que participaron en mas de 5 peliculas
pila_personajes.personajes_mas_de_5_peliculas()

# Determinar participacion de la Viuda Negra
pila_personajes.participacion_black_widow()

# Mostrar personajes cuyos nombres empiezan con C, D y G
pila_personajes.mostrar_personajes_cdg()

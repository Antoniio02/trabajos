# 1) Escribir una clase llamada Rectángulo que contenga una base y una altura,
#  y que contenga un método que devuelva el área del rectángulo.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

rectangulo = Rectangulo(5, 3)
print("El área del rectángulo es:", rectangulo.area())

# 2)Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina.
#  La clase debe contener como miembros:
# o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
# o Un atributo para el estado (lleno o vacío).
# o Un atributo n, que indica la cantidad máxima de cebadas.
# o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
# excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
# o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
# debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
# o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
# de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
# “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

class Mate:
    def __init__(self, cantidad_maxima):
        self.cantidad_cebadas = cantidad_maxima
        self.estado = "vacío"
        self.n = cantidad_maxima

    def cebar(self):
        if self.estado == "lleno":
            print("¡Cuidado! ¡Te quemaste!")
        elif self.cantidad_cebadas > 0:
            self.estado = "lleno"
            print("Mate cebado.")
        else:
            print("Advertencia: el mate está lavado.")
            self.estado = "lleno"

    def beber(self):
        if self.estado == "vacío":
            print("¡El mate está vacío!")
        elif self.cantidad_cebadas > 0:
            self.cantidad_cebadas -= 1
            self.estado = "vacío"
            print(f"Se bebió el mate. Quedan {self.cantidad_cebadas} cebadas.")
        else:
            print("Advertencia: el mate está lavado.")
            self.estado = "vacío"


mate = Mate(3)

mate.cebar()
mate.beber()
mate.cebar()
mate.beber()
mate.cebar()
mate.beber()

mate.cebar()
mate.beber()

# 3) Botella y Sacacorchos
#  Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
#  Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
# destapada.
#  Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
# una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
# sacacorchos ya contiene un corcho.
#  Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
# un corcho.
class Corcho:
    def __init__(self, bodega):
        self.bodega = bodega


class Botella:
    def __init__(self, corcho):
        self.corcho = corcho

    def destapada(self):
        return self.corcho is None


class Sacacorchos:
    def __init__(self):
        self.corcho = None

    def destapar(self, botella):
        if botella.destapada():
            print("La botella ya está destapada.")
        elif self.corcho is not None:
            print("El sacacorchos ya contiene un corcho.")
        else:
            self.corcho = botella.corcho
            botella.corcho = None
            print(f"Botella destapada, corcho extraído de la bodega {self.corcho.bodega}.")

    def limpiar(self):
        if self.corcho is None:
            print("No hay un corcho en el sacacorchos.")
        else:
            print(f"Corcho de la bodega {self.corcho.bodega} retirado del sacacorchos.")
            self.corcho = None


corcho1 = Corcho("Bodega La Rioja")
botella1 = Botella(corcho1)
sacacorchos = Sacacorchos()

sacacorchos.destapar(botella1)
sacacorchos.limpiar()
sacacorchos.destapar(botella1)

# 4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
# restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
# método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
# Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
# sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
# al método

class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Restaurante: {self.restaurante_nombre}")
        print(f"Tipo de comida: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.restaurante_nombre} ahora está abierto.")


class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print(f"Sabores disponibles en {self.restaurante_nombre}:")
        for sabor in self.sabores:
            print(f"- {sabor}")


heladeria = Heladeria("La Dolce Vita", "Helados", ["Chocolate", "Vainilla", "Fresa", "Menta"])

heladeria.describir_restaurante()
heladeria.abrir_restaurante()
heladeria.mostrar_sabores()


# 5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
# reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
# que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
#  Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
# personaje, al que le debe hacer el daño indicado por el atributo ataque.
#  Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
# devuelva la cantidad cosechada

class Personaje:
    def __init__(self, vida, posicion, velocidad):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad

    def recibir_ataque(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            print("¡El personaje ha muerto!")
            raise Exception("Vida menor o igual a cero")

    def mover(self, direccion):
        self.posicion += self.velocidad * direccion
        print(f"Personaje se ha movido a la posición {self.posicion}")


class Soldado(Personaje):
    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque = ataque

    def atacar(self, otro_personaje):
        print(f"Soldado ataca a personaje con {self.ataque} de daño.")
        otro_personaje.recibir_ataque(self.ataque)


class Campesino(Personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha = cosecha

    def cosechar(self):
        print(f"Campesino ha cosechado {self.cosecha} unidades.")
        return self.cosecha


soldado = Soldado(100, 0, 5, 20)
campesino = Campesino(80, 10, 3, 50)

soldado.mover(1)
soldado.atacar(campesino)
campesino.cosechar()


# 6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
# se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
# usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
# Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.

class Usuario:
    def __init__(self, nombre, apellido, edad, correo, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.direccion = direccion

    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo}")
        print(f"Dirección: {self.direccion}")

    def saludar_usuario(self):
        print(f"¡Hola, {self.nombre} {self.apellido}! Bienvenido a tu perfil.")


usuario1 = Usuario("Pedro", "Rodriguez", 28, "pedro.rodriguez@gmail.com", "Av. Belgrano 183")
usuario2 = Usuario("Joaquin", "Saravia", 25, "joacosarv@gmail.com", "Av. San Martin")
usuario3 = Usuario("Antonio", "Dominguez", 23, "axe.8202@gmail.com", "Alejandro gauffin")

usuario1.describir_usuario()
usuario1.saludar_usuario()

usuario2.describir_usuario()
usuario2.saludar_usuario()

usuario3.describir_usuario()
usuario3.saludar_usuario()


# 7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
# Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
# postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
# muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

class Admin(Usuario):
    def __init__(self, nombre, apellido, edad, correo, direccion, privilegios):
        super().__init__(nombre, apellido, edad, correo, direccion)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(f"Privilegios de {self.nombre} {self.apellido}:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")


admin1 = Admin("Alen", "Alfaro", 30, "alenalf@Gmail.com", "Buenos Aires", 
    ["puede postear en el foro",
    "puede borrar un post",
    "puede banear usuario",
    "puede ver estadísticas avanzadas"])

admin1.describir_usuario()
admin1.saludar_usuario()
admin1.mostrar_privilegios()

# 8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
# con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
# clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
# el método para mostrar privilegios.

class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print("Privilegios:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")
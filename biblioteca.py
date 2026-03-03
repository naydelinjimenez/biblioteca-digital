# Clase que representa un libro
class Libro:

    # Constructor de la clase
    def __init__(self, titulo, autor, categoria, isbn):
        
        # Usamos una tupla para guardar título y autor (no cambiarán)
        self.info = (titulo, autor)

        # Categoría del libro
        self.categoria = categoria

        # Código único del libro
        self.isbn = isbn

# Método para mostrar la información del libro
    def mostrar_info(self):
        print("Título:", self.info[0])
        print("Autor:", self.info[1])
        print("Categoría:", self.categoria)
        print("ISBN:", self.isbn)

# Clase que representa a un usuario de la biblioteca
class Usuario:

    # Constructor de la clase
    def __init__(self, nombre, id_usuario):

        # Nombre del usuario
        self.nombre = nombre

        # ID único del usuario
        self.id_usuario = id_usuario

        # Lista de libros prestados
        self.libros_prestados = []

# Clase que gestiona toda la biblioteca
class Biblioteca:

    # Constructor de la biblioteca
    def __init__(self):

        # Diccionario para guardar los libros (ISBN : objeto Libro)
        self.libros = {}

        # Diccionario para guardar los usuarios (ID : objeto Usuario)
        self.usuarios = {}

        # Conjunto para asegurar IDs únicos
        self.ids_usuarios = set()

# Método para añadir un libro
    def añadir_libro(self, libro):

        # Verifica si el ISBN ya existe
        if libro.isbn in self.libros:
            print("El libro ya existe en la biblioteca")

        else:
            # Se agrega el libro al diccionario
            self.libros[libro.isbn] = libro
            print("Libro añadido correctamente")

# Método para quitar un libro de la biblioteca
    def quitar_libro(self, isbn):

        # Verifica si el libro existe
        if isbn in self.libros:

            # Elimina el libro del diccionario
            del self.libros[isbn]
            print("Libro eliminado correctamente")

        else:
            print("El libro no existe en la biblioteca")

# Método para registrar un usuario
    def registrar_usuario(self, usuario):

        # Verifica si el ID ya está registrado
        if usuario.id_usuario in self.ids_usuarios:
            print("El ID de usuario ya existe")

        else:
            # Se agrega el ID al conjunto
            self.ids_usuarios.add(usuario.id_usuario)

            # Se guarda el usuario en el diccionario
            self.usuarios[usuario.id_usuario] = usuario

            print("Usuario registrado correctamente")

# Método para dar de baja un usuario
    def eliminar_usuario(self, id_usuario):

        # Verifica si el usuario existe
        if id_usuario in self.usuarios:

            # Elimina el usuario del diccionario
            del self.usuarios[id_usuario]

            # También elimina el ID del conjunto
            self.ids_usuarios.remove(id_usuario)

            print("Usuario eliminado correctamente")

        else:
            print("El usuario no existe")

# Método para prestar un libro a un usuario
    def prestar_libro(self, id_usuario, isbn):

        # Verificar si el usuario existe
        if id_usuario not in self.usuarios:
            print("El usuario no existe")
            return

        # Verificar si el libro existe
        if isbn not in self.libros:
            print("El libro no está disponible")
            return

        # Obtener el usuario y el libro
        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]

        # Agregar el libro a la lista de libros prestados del usuario
        usuario.libros_prestados.append(libro)

        # Eliminar el libro de la biblioteca
        del self.libros[isbn]

        print("Libro prestado correctamente")

# Método para devolver un libro
    def devolver_libro(self, id_usuario, isbn):

        # Verificar si el usuario existe
        if id_usuario not in self.usuarios:
            print("El usuario no existe")
            return

        usuario = self.usuarios[id_usuario]

        # Buscar el libro en los libros prestados del usuario
        for libro in usuario.libros_prestados:

            if libro.isbn == isbn:

                # Quitar el libro de la lista del usuario
                usuario.libros_prestados.remove(libro)

                # Volver a añadir el libro a la biblioteca
                self.libros[isbn] = libro

                print("Libro devuelto correctamente")
                return

        print("El usuario no tiene ese libro prestado")

# Método para buscar libros
    def buscar_libro(self, tipo, valor):

        encontrado = False

        # Revisar todos los libros de la biblioteca
        for libro in self.libros.values():

            if tipo == "titulo" and libro.info[0] == valor:
                libro.mostrar_info()
                encontrado = True

            elif tipo == "autor" and libro.info[1] == valor:
                libro.mostrar_info()
                encontrado = True

            elif tipo == "categoria" and libro.categoria == valor:
                libro.mostrar_info()
                encontrado = True

        if not encontrado:
            print("No se encontraron libros")

# Crear la biblioteca
biblioteca = Biblioteca()

# Crear algunos libros
libro1 = Libro("El principito", "Antoine de Saint-Exupery", "Ficcion", "111")
libro2 = Libro("Don Quijote", "Miguel de Cervantes", "Clasico", "222")
libro3 = Libro("1984", "George Orwell", "Distopia", "333")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Juan", 1)
usuario2 = Usuario("Maria", 2)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar un libro
biblioteca.prestar_libro(1, "111")

# Mostrar libros prestados del usuario
print("\nLibros prestados a Juan:")
for libro in usuario1.libros_prestados:
    libro.mostrar_info()

# Devolver el libro
biblioteca.devolver_libro(1, "111")

# Buscar libro por titulo
print("\nBusqueda por titulo:")
biblioteca.buscar_libro("titulo", "1984")
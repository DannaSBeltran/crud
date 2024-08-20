def crear(self, nombre, edad):
    nuevo_usuario = Usuario(self.id_counter, nombre, edad)
    self.usuarios.append(nuevo_usuario)
    self.id_counter += 1
    print(f"Usuario creado: {nuevo_usuario.id}, {nuevo_usuario.nombre}, {nuevo_usuario.edad}")

def leer(self):
    for usuario in self.usuarios:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Edad: {usuario.edad}")

def actualizar(self, id, nombre, edad):
    for usuario in self.usuarios:
        if usuario.id == id:
            usuario.nombre = nombre
            usuario.edad = edad
            print(f"Usuario actualizado: {usuario.id}, {usuario.nombre}, {usuario.edad}")
            return
    print("Usuario no encontrado.")

def eliminar(self, id):
    for usuario in self.usuarios:
        if usuario.id == id:
            self.usuarios.remove(usuario)
            print(f"Usuario eliminado: {usuario.id}, {usuario.nombre}")
            return
    print("Usuario no encontrado.")

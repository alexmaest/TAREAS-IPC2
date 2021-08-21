class estudiante:
  def __init__(self, carne, nombre, edad, direccion, telefono, email, carrera, puesto):
    self.carne = carne
    self.nombre = nombre 
    self.edad = edad
    self.direccion = direccion
    self.telefono = telefono
    self.email = email
    self.carrera = carrera
    self.puesto = puesto

class nodo:
  def __init__(self, estudiante=None, siguiente=None, anterior=None):
    self.estudiante = estudiante
    self.siguiente = siguiente
    self.anterior = anterior

class lista_doble:
  def __init__(self):
    self.primero = None
  
  def insertar(self, estudiante):
    if self.primero is None:
      self.primero = nodo(estudiante=estudiante)
    else:
      actual =nodo(estudiante=estudiante, siguiente=self.primero)
      self.primero.anterior = actual
      self.primero = actual
  
  def recorrer(self):
    if self.primero is None:
      return
    actual = self.primero
    print("carne:", actual.estudiante.carne, "nombre:", actual.estudiante.nombre, "email:", actual.estudiante.email, "->")
    while actual.siguiente:
        actual = actual.siguiente
        print("carne: ", actual.estudiante.carne, "nombre: ", actual.estudiante.nombre, "email: ", actual.estudiante.email, "->")

  def eliminar(self, carne):
    actual = self.primero
    while actual:
      if actual.estudiante.carne == carne:
        if actual.anterior:
          if actual.siguiente:
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
          else:
            actual.anterior.siguiente = None
            actual.anterior = None
        else:
          if actual.siguiente:
            self.primero = actual.siguiente
            actual.siguiente.anterior = None
          else:
            self.primero = None
        return True
      else:
        actual = actual.siguiente
    return False

  def buscar(self, carne):
    actual = self.primero
    while actual != None:
      if carne == actual.estudiante.carne:
        print("Estudiante encontrado")
        print("carne:", actual.estudiante.carne, "nombre:", actual.estudiante.nombre, "email:", actual.estudiante.email, "->")
        break
      else:
        actual = actual.siguiente
    if actual == None:
      print("Estudiante no encontrado")

e1 = estudiante(201915859, "Gerson Ortiz", 20, "9 calle 10-02 zona 1", 24483922, "gerson.ortiz@gmail.com", "Ingenieria en Sistemas", "Programador Jr")
e2 = estudiante(201953234, "Karen Hurarte", 21, "7 calle 10-02 zona 1", 24465436, "karenhurarte@gmail.com", "Ingenieria en Sistemas", "Programador Jr")
e3 = estudiante(201963423, "Luis Mendez", 22, "8 calle 10-02 zona 1", 28644444, "luismendez@gmail.com", "Ingenieria en Sistemas", "Programador Jr")

lista_d = lista_doble()
lista_d.insertar(e1)
lista_d.insertar(e2)
lista_d.insertar(e3)

lista_d.recorrer()

lista_d.eliminar(201953234)

lista_d.buscar(201963423)
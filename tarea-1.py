class estudiante:
  def __init__(self, carne, nombre, edad, direccion, telefono, email, carrera, puesto):
    self.carne = carne
    self.nombre = nombre 
    self. edad = edad
    self.direccion = direccion
    self.telefono = telefono
    self.email = email
    self.carrera = carrera
    self.puesto = puesto

class nodo:
  def __init__(self, estudiante = None, siguiente = None):
    self.estudiante = estudiante
    self.siguiente = siguiente

class lista_enlazada:
  def __init__(self):
    self.primero = None #Se inicializa la lista 
  
  def insertar(self, estudiante):
    if self.primero is None: #Si primero esta vacia.
      self.primero = nodo(estudiante = estudiante) 
      return
    actual = self.primero 
    while actual.siguiente: 
      actual = actual.siguiente 
    actual.siguiente = nodo(estudiante=estudiante)

  def recorrer(self):
    actual = self.primero
    while actual != None:
      print("carne:", actual.estudiante.carne, "nombre:", actual.estudiante.nombre, "email:", actual.estudiante.email, "->")
      actual = actual.siguiente
  
  def eliminar(self,carne):
    actual = self.primero
    anterior = None

    while actual and actual.estudiante.carne != carne:
      anterior = actual
      actual = actual.siguiente

    if anterior is None:
      self.primero = actual.siguiente
      actual.siguiente = None

    elif actual:
      anterior.siguiente = actual.siguiente
      actual.siguiente = None

    # De otra manera
    while actual and actual.estudiante.carne == carne:
      anterior = actual
      actual = actual.siguiente
        
      if anterior is None:
        self.primero = actual.siguiente
        actual.siguiente = None
      elif actual:
        actual = actual.siguiente
        actual.siguiente = None

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

lista_e = lista_enlazada()
lista_e.insertar(e1)
lista_e.insertar(e2)
lista_e.insertar(e3)

lista_e.recorrer()

lista_e.buscar(201953234)
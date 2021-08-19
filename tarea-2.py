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

class lista_circular:
  def __init__(self):
    self.primero = None
  
  def insertar(self, estudiante):
    if self.primero is None:
      self.primero = nodo(estudiante = estudiante)
      self.primero.siguiente = self.primero
    else:
      actual = nodo(estudiante = estudiante, siguiente = self.primero.siguiente)
      self.primero.siguiente = actual

  def recorrer(self):
    if self.primero is None:
      return
    actual = self.primero
    print("carne:", actual.estudiante.carne, "nombre", actual.estudiante.nombre, "email", actual.estudiante.email, "->")
    while actual.siguiente != self.primero:
      actual = actual.siguiente
      print("carne:", actual.estudiante.carne, "nombre", actual.estudiante.nombre, "email", actual.estudiante.email, "->")
  
  def eliminar(self, carne):
    actual = self.primero
    anterior = None
    no_encontrado = False

    while actual and actual.estudiante.carne != carne:
      anterior = actual
      actual = actual.siguiente
      if actual == self.primero:
        no_encontrado = True
        break
    if not no_encontrado:
      if anterior is not None:
        anterior.siguiente = actual.siguiente
      else:
        while actual.siguiente != self.primero: 
          actual = actual.siguiente
        actual.siguiente = self.primero.siguiente
        self.primero = self.primero.siguiente
  
  def buscar(self, carne):
    if self.primero != None:
      actual = self.primero
      Encontrado =  False
     
      while actual != None:
        if actual.estudiante.carne == carne:
          Encontrado =  True
          break      
        elif actual.siguiente == self.primero:
          break
        else:
          actual = actual.siguiente
          Encontrado =  False

      if Encontrado == True:
        print("Estudiante encontrado")
        print("carne:", actual.estudiante.carne, "nombre", actual.estudiante.nombre, "email", actual.estudiante.email, "->")
      else:
        print("Estudiante no encontrado")
    else:
      print("Lista vacia")

e1 = estudiante(201915859, "Gerson Ortiz", 20, "9 calle 10-02 zona 1", 24483922, "gerson.ortiz@gmail.com", "Ingenieria en Sistemas", "Programador Jr")
e2 = estudiante(201953234, "Karen Hurarte", 21, "7 calle 10-02 zona 1", 24465436, "karenhurarte@gmail.com", "Ingenieria en Sistemas", "Programador Jr")
e3 = estudiante(201963423, "Luis Mendez", 22, "8 calle 10-02 zona 1", 28644444, "luismendez@gmail.com", "Ingenieria en Sistemas", "Programador Jr")

lista_c = lista_circular()
lista_c.insertar(e1)
lista_c.insertar(e2)
lista_c.insertar(e3)

lista_c.recorrer()
lista_c.buscar(201963423)
lista_c.eliminar(201915859)
lista_c.recorrer()
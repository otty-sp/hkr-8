#realizamos el constructor donde definiremos los TDA que queremos que realice

class Empleados:


	def movimiento(codigoEmpleado,canttarea,tareas):
		self.CodigoEmpleado = codigo
		self.Canttarea= canttarea
        self.tareas = None

        global id
        id += 1
        self.id = id
        
        
    def Gettareas(self):
        return self.tareas

    def GetCanttarea(self):
        return self.Canttarea

    def GetCodigodeEmpleado(self):
        return self.id
        
#en las Tareas, se declarara la area y la descripcion del empleado        
        
class Tareas:

    def __init__(self,descripcion,Area):
        self.Descripcion=descripcion
        self.AreaSolicitante = Area
        self.listareas = Stack()
        

    def GetDescripcion(self)
        return self.Descripcion
        

    def GetAreaSolicitante(self):
        return self.AreaSolicitante
        

    def AgregarTarea(self,descripcion,Area):
        self.listareas.push(Tarea(descripcion,Area))
        

class Empleado:

    def __init__(self):
    
        self.newTarea = Stack()
        self.Busca = []
        
    def AgregarEmpleado(self,cantidadtareas,tareas):
        self.newTarea.push(Empleado(cantidadtareas,tareas))

    def BuscarEmpleado(self,inicio,fin):
    
        for i in range(self.newTarea.size()):
            Emple = self.Registro.pop()
            if Emple.id >= inicio and Emple.id <= fin:
                self.newTarea.push(Emple)
                self.Busca.append(Emple)
            else:
                self.newTarea.push(Emple)
    def Busqueda(self):
        print self.Busca

    def AsignarTarea(self):
        emplea = None
        for i in range(self.newTarea.size()):
            emplea = self.newTarea.pop()
            if emplea.Cantidad == emplea.tareas:
                self.newTarea.push(Emplea)
            else:
                emplea.tareas = []
                while is not self.listareas.isEmpty() and emplea.Cantidad =! len(emplea.tareas):
                    tare = self.listareas.pop()
                    emplea.tareas.append(tare)
self.newTarea.push(emplea) 

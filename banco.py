from movimiento import movimiento
from stack import Stack
class banco:
#constructor, definimos lo deseado en e banco
    def __init__(self):

        self.banco=Stack()
        self.id = None
        self.depo = Stack()
        self.extra = Stack()
        self.cuen = Stack()

    def entrada(self,fecha,noCu,monto,tipo):
        self.banco.push(movimiento(fecha,noCu,monto,tipo))
         

    def arreglo(self):
        while not self.banco.isEmpety():
            tipo = self.banco.pop()
            if tipo.tipo == 0:
                depo.push(self.banco.pop)
            else:
                extra.push(self.banco.pop)
       

#calcula el deposito total

    def totaldepo(self, day):
        depo = self.id
        suma= none
        suma2 = none
        fech = self.temp.pop()
        while fech.fecha <= day and not self.id.isEmpety():
            suma = self.id.pop()
            suma.monto = suma2
            suma2 += suma2
        return suma2

        # regresa el numero de depositos realizados

    def nodepo(self, day):
        self.id = depo.pop()
        tool = Stack()
        while self.temp.fecha <= day and not self.temp.isEmpety():
            tool.push(depo.pop)
        tool.size()
        return tool

        # separa los movimientos echos en una cuenta

    def cuenta(self,n):
        while not self.banco.isEmpety():
            cu = self.banco.pop()
            if cu.nocuenta == n:
                cuen.push(sefl.banco.pop)
            else:
                none

        #total de deposito de una cuenta

    def saldocuenta(self):
        while not cuen.isEmpety()
            op = cuen.pop()
            if op.tipo == 0:
                depocuen = op.monto
                totaldepocuen += depocuen
            else:
                reticuen = op.monto
                totalreticuen += reticuen

        return totaldepocuen
p.banco
for i in 5:
    (i,i,i,0)

# -*- coding: iso-8859-15 -*-

#Datos de los autores:

#Nombres de los estudiantes:Ian Andrés Rubio Cabrera.
#Grupo: 467
#Programa: 213023
#Codigo Fuente: autoria propia

#---------------------------------------------------------------------------------------------------------------------------------
#

#librerias:
from abc import abstractmethod
from abc import ABCMeta
from abc import ABC


#classes abstractas:

class entidad_g_del_s(metaclass= ABCMeta):
    pass
    

class servicios(entidad_g_del_s):
    # datos utiles:
    text_1 = "Por favor ingrese un número entero"
    
    def __init__(self):
        self._nombre = "servicio"
        self._costo = 0
        self._costo = 0
    def calcular_costos():
        pass
    def describir_servicios():
        pass
    def validar_parametros():
        pass
    def asignar_a_cliente(self,lista):
        print("nombre   |  nu. identificacion:")
        for a in lista:
            print("("+str(a._nombre),"|"+str(a._identificacion)+")")
        while True:
            b = input("escriba el número de indentificación del cliente para seleccionarlo")  
            if b == int():
                lista[b]._servicios.append(self)

            else:
                print(self.text_1)

#classes

    #clase cliente:
class cliente(entidad_g_del_s):
   
    def __init__(self):
        self._nombre = "Usuario_0"
        self._identificacion = "0"
        self._servicios = []
        self._deudas = "0"
    def registro(self, lista,operacion):
            if operacion == 1:
        
                print("Registro de clientes.")
                while True:
                    a = input("ingrese el nombre del cliente o ingrese 0 para cancelar\n")
                    if a == "0":
                        print("cancelado")
                        break
                
                    else:
                        self._nombre = str(a)
                        self._identificacion = len(lista)
                        lista.append(self)
                        break
            elif operacion == 2:
                
                print("Eliminación de clientes.")
                print("lista de clientes:")
                print("nombre   |  nu. identificacion:")
                for a in lista:
                    print("("+str(a._nombre),"|"+str(a._identificacion)+")")
                    while True:
                        b = int(input("Escriba el número de indentificación del cliente para seleccionarlo"+
                                  " o escriba 'cancelar' para cancelar.\n"))
                        if type(b) == int:
                            b2 = input("digite 1 para confirmar la eliminacion del usuario o "+
                                "cualquier otra tecla para cancelar\n")
                            if b2 == "1":
                                del lista[b]
                                print("cliente eliminado con exito")
                                break
                            else:
                                 print("cancelado")
                                 break
                        elif a == "cancelar":
                            print("cancelado")
                            break
                        
                        else:
                            print("fallo")
                
                
                    
            
            
            

    #3 clases que hereden de la clase servicios:
    # los tiempos son en horas:
class reservas_de_salas(servicios):
    nombre = "reserva de sala"
    def __init__(self):
        self._nombre = "reserva de sala"
        self._tiempo = 0
        self._costo = 0

    def calcular_costos(self):
        self._costo = int(self.tiempo) * 10000
        
        print(self._costo)
        
    def describir_servicios(self):
        print("Renta de salas por horas a costo fijo de 10000 por hora")
        
    def validar_parametros(self):
        while True:
            self.describir_servicios()
            print("ingrese el tiempo de reserva de sala")
            a = input()
            if a == int():
                self._tiempo = a
                self.calcular_costos()
                break
            else:
                print(self.text_1)
                
          
        

class alquiler_de_equipos(servicios):
    nombre = "alquiler de equipos"
    def __init__(self):
        self._nombre = "alquiler de equipos"
        self._tiempo = 0
        self._costo = 0
        
    def calcular_costos(tiempo):
        total = tiempo * 50000
        print(total)
        return total
    def describir_servicios():
        print("alquiler de equipos informaticos por costo de 50000 por hora")
    def validar_parametros(self):
        while True:
            self.describir_servicios()
            print("ingrese el tiempo del alquiler")
            a = input()
            if a == int():
                self._tiempo = a
                self.calcular_costos()
                break
            else:
                print(self.text_1)

class asesorias_especializadas(servicios):
    nombre = "asesorias especializadas"
    def __init__(self):
        self._nombre = "asesorias especializadas"
        self._tipo = 1
        self._tiempo = 0
        self._costos_adicionales = 0
        self._costo = 0

    def calcular_costos(self):
        total1 = (self._tipo * self._duracion)+self._costos_adicionales
        if self._duracion > 48:
            descuento = 0,85
        else:
            descuento = 1
        total = total1 * descuento
        self._costo = total
        print(total)
        return total
    def describir_servicios(self):
        print("Asesorias especializadas de software y hardware varian en coste por tipo(harware(50000$)"+
        ", sofware(100000$)), duracion y costos adicionales")
        
    def validar_parametros(self):
        con1 = True
        while con1:
            self.describir_servicios()
            print("ingrese el tipo(harware(50000$)"+", sofware(100000$)"+
                  "\n con (1)harware(50000$) \n(2)sofware(100000$)")
            
            a = input()
            if a == 1 or 2:
                self._tipo = a
                while con1:
                    print("ingrese la duracion de la asesorias especializadas")
                    a = input()
                    if a == int():
                        self._tiempo = a
                        while con1:
                            print("ingrese los costos adicionales")
                            a = input()
                            if a == int():
                                self._costos_adicionales = a
                                self.calcular_costos()
                                con1 = False
                                
                            else:
                                print(self.text_1)
                    
                    else:
                        print(self.text_1)
                
            else:
                print("porfavor ingrese 1 o 2")
                
# Una clase Reserva que integre cliente(al que esta asignada la reserva), servicio(que se reserva), duración 
#y estado(cancelada, activa,(pagada)),
#e implemente confirmación, cancelación y procesamiento con
#manejo de excepciones.
class Reserva(entidad_g_del_s):
    def __init__(self):
        self._cliente = "desconocido"
        self._servicio = "0"
        self._duración = "0" 
        self._estado = "0"
    def confirmación(self):
        self._estado = "confirmada"
    def cancelación(self):
        del self
    def procesamiento(self,a,b,c,d):
        self._cliente = a
        self._servicio = b
        self._duración = c
        self._estado = d
    
        
    

#Sistema de reservas de salas

#Sistema de alquiler de equipos 

#Sistema de asesorías especializadas


#inicio de programa:
class menu(entidad_g_del_s):
    control = -1
    # def __init__(self):
    #     pass
    control2 = True
    clientes_l = []
    #datos de texto utilies:
    text1_1 = "digite el número correspondiente a la opcion para seleccionarla:"
    
    def menu_ini(self):
        while self.control2:
            print("Menú de Software FJ para gestion de clientes, servicios y reservas.")
            print(self.text1_1)
            print("(1)clientes")
            print("(2)servicios")
            print("(3)reservas")
            print("(0)cerrar")
            self.menu_control()

    def menu_clientes(self):
        global clientes_l 
        a2 = len(self.clientes_l)
        print("número de clientes:"+str(a2))
        print("lista de clientes:")
        
        for a in self.clientes_l:
            #print(a)
            if a2 == 0:
                pass
            else:
                print(a._nombre, end= ", ")
        print()
        print("precione '1' para añadir un cliente")
        print("precione '2' para eliminar un cliente")
        print("precione '0' para cancelar")
        b1 = int(input())
        if b1 == 1 or 2:
            b2 = cliente()
            b2.registro(self.clientes_l,b1)
            inicio.menu_ini()
        elif b1 == 0:
            inicio.menu_ini()
        
    def menu_servicios(self):
        print(self.text1_1)
        print("(1)Para asignar un servicio a un cliente")
        print("(2)Para eliminar un servicio a un cliente")
        print("(3)Para cancelar")
        a = input()
        if a == "1":
            print("lista de servicios:")
            l1 = []
            for a1 in servicios.__subclasses__():
                l1.append(a1.nombre)
            print(l1)
            print("Digite el número de dentificación del servicio para selecciónarlo.")
            print("nombre   |  nu. identificacion:")
            for b, a1 in enumerate(servicios.__subclasses__()):
                print(str(a1.nombre),str(b))

    def menu_reservas(self):
        print("lista de reservas:")
        self.menu_control()
        
    def menu_control(self):
        entrada = int(input())
        self.control = entrada
        if self.control == 1:
            self.menu_clientes()
            self.control = -1
        if self.control == 2:
            self.menu_servicios()
            self.control = -1
        if self.control == 3:
            self.menu_reservas()
            self.control = -1
        if self.control == 0:
            print("adios")
            self.control2 = False
            self.control = -1
    

inicio = menu()

inicio.menu_ini()
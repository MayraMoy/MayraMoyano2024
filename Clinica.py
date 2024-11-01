from datetime import date
from typing import List, Optional

class Consulta:
    def __init__(self, en_linea_o_cita: str, fecha_solicitud: date, cadena_sintomas: str, estado_solicitud: str):
        self.en_linea_o_cita = en_linea_o_cita
        self.fecha_solicitud = fecha_solicitud
        self.cadena_sintomas = cadena_sintomas
        self.estado_solicitud = estado_solicitud
        self.doctor = None  # Relación con Doctor (uno a muchos)
        self.paciente = None  # Relación con Paciente (uno a muchos)


class Pacientes:
    def __init__(self, id: str, nombre: str, edad: int, genero: str, email: str, telefono: str, direccion: str):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.consultas: List[Consulta] = []  # Relación con Consulta (uno a muchos)
        
    def crear_perfil_de_paciente(self):
        pass
    
    def editar_perfil_de_paciente(self):
        pass
    
    def eliminar_perfil_de_paciente(self):
        pass
    
    def solicitud_de_consulta(self):
        pass


class Preinscripcion:
    def __init__(self, id_de_prescripcion: int, diagnostico: str, nombre_de_medicina: str, potencia_medicamento: int, 
                 frecuencia_medicamento: int, observaciones: str, prueba_laboratorio: str, laboratorio_de_instrucciones: str, 
                 preinscripcion_entregar: str, solicitudes_de_laboratorio_realizadas: str, monto_de_la_factura: float):
        self.id_de_prescripcion = id_de_prescripcion
        self.diagnostico = diagnostico
        self.nombre_de_medicina = nombre_de_medicina
        self.potencia_medicamento = potencia_medicamento
        self.frecuencia_medicamento = frecuencia_medicamento
        self.observaciones = observaciones
        self.prueba_laboratorio = prueba_laboratorio
        self.laboratorio_de_instrucciones = laboratorio_de_instrucciones
        self.preinscripcion_entregar = preinscripcion_entregar
        self.solicitudes_de_l


from ..extensions import db, ma
from .midle_tables import *

class Profesor(db.Model):
    cedula = db.Column(db.Integer, primary_key = True)
    nacionalidad = db.Column( db.String(50) )
    genero = db.Column( db.String(255) )
    dedicacion = db.Column( db.String(255) )
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    nombre_banner = db.Column(db.String(255))
    fecha_vinculacion =db.Column(db.DateTime)
    correo = db.Column(db.String(255))
    maximo_nivel_academico = db.Column(db.String(255))
    validado_por = db.Column(db.String(255))
    validado_en = db.Column(db.DateTime)
    articulos = db.relationship("Articulo", secondary=autor_articulo_profesor) 
    
class ProfesorSchema(ma.Schema):
    class Meta:
        fields = ("cedula", "nacionalidad", "genero","dedicacion","nombre","apellido","nombre_banner","fecha_vinculacion",\
            "correo","maximo_nivel_academico","validado_por","validado_en")
    
profesor_schema = ProfesorSchema()
profesores_schema = ProfesorSchema(many = True)

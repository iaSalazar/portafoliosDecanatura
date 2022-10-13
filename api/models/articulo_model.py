
from ..extensions import db, ma


# #midle table
# autor_articulo_profesor = db.Table('autor_articulo_profesor',
#                     db.Column('articulo_id', db.Integer, db.ForeignKey('articulo.id')),
#                     db.Column('profesor_cedula', db.Integer, db.ForeignKey('profesor.cedula'))
#                     )


class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column( db.String(250) )
    ano = db.Column(db.Integer)
    tipo = db.Column(db.String(250))
    referencia = db.Column(db.String(250))
    fecha_ultima_modificación = db.Column(db.DateTime)
    nombre_revista = db.Column(db.String(250))
    doi = db.Column(db.String(250))
    issn = db.Column(db.String(250))
    volumen = db.Column(db.String(250))
    numero = db.Column(db.Integer)
    pagina_inicial = db.Column(db.String(250))
    calificacion = db.Column(db.String(250)) 
    citaciones = db.Column(db.Integer)
    validado_por = db.Column(db.String(250))
    validado_en = db.Column(db.DateTime)

    
class Articulo_Schema(ma.Schema):
    class Meta:
        fields = ("id", "titulo", "ano", "tipo", "referencia","fecha_ultima_modificación","nombre_revista", "doi", "issn", "volumen",\
           "numero", "pagina_inicial","calificacion","citaciones","validado_por","validado_en" )
    
articulo_schema = Articulo_Schema()
articulos_schema = Articulo_Schema(many = True)



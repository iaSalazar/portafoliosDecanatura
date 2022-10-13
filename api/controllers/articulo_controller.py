from flask import request
from flask_restful import Resource
from ..models.articulo_model import articulo_schema, articulos_schema, Articulo
from ..models.profesor_model import Profesor
from ..extensions import db,api


class RecursoListarArticulos(Resource):
    def get(self):
        articulos = Articulo.query.all()
        return articulos_schema.dump(articulos)
    
    def post(self):
            articulo_nuevo = Articulo(
                titulo = request.json['titulo'],
                tipo =request.json['tipo']
            )
            #simulates the profesor who is inserting data about the article.
            profesor = Profesor.query.get_or_404(1234)
            profesor.articulos.append(articulo_nuevo)
            db.session.add(profesor)
            #db.session.add(articulo_nuevo)
            db.session.commit()
            return articulo_schema.dump(articulo_nuevo)
     
class RecursoUnArticulo(Resource):
    def get(self, id_articulo):
        articulo = Articulo.query.get_or_404(id_articulo)
        return articulo_schema.dump(articulo)
    
    def put(self, id_articulo):
        articulo = Articulo.query.get_or_404(id_articulo)

        if 'titulo' in request.json:
            articulo.titulo = request.json['titulo']
        if 'tipo' in request.json:
            articulo.contenido = request.json['tipo']

        db.session.commit()
        return articulo_schema.dump(articulo)

    def delete(self, id_articulo):
        articulo = Articulo.query.get_or_404(id_articulo)
        db.session.delete(articulo)
        db.session.commit()
        return '', 204

api.add_resource(RecursoListarArticulos, '/articulos')     
api.add_resource(RecursoUnArticulo, '/articulos/<int:id_publicacion>')
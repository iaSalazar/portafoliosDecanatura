from flask import request
from flask_restful import Resource
from ..models.profesor_model import profesor_schema, profesores_schema, Profesor
from ..extensions import db,api


class RecursoListarProfesores(Resource):
    def get(self):
        profesor = Profesor.query.all()
        return profesores_schema.dump(profesor)
    
    def post(self):
            nuevo_profesor = Profesor(
                cedula = request.json['cedula'],
                nombre=request.json['nombre']
            )
            db.session.add(nuevo_profesor)
            db.session.commit()
            return profesor_schema.dump(nuevo_profesor)
     
class RecursoUnProfesor(Resource):
    def get(self, id_profesor):
        profesor = Profesor.query.get_or_404(id_profesor)
        return profesor_schema.dump(profesor)
    
    def put(self, id_profesor):
        profesor = Profesor.query.get_or_404(id_profesor)

        if 'cedula' in request.json:
            profesor.titulo = request.json['cedula']
        if 'nombre' in request.json:
            profesor.contenido = request.json['nombre']

        db.session.commit()
        return profesor_schema.dump(profesor)

    def delete(self, id_profesor):
        profesor = Profesor.query.get_or_404(id_profesor)
        db.session.delete(profesor)
        db.session.commit()
        return '', 204

api.add_resource(RecursoListarProfesores, '/api/profesores')     
api.add_resource(RecursoUnProfesor, '/api/profesores/<int:id_profesor>')
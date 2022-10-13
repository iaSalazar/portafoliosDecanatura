from ..extensions import db, ma

#midle table
autor_articulo_profesor = db.Table('autor_articulo_profesor',
                    db.Column('profesor_cedula', db.Integer, db.ForeignKey('profesor.cedula')),
                    db.Column('articulo_id', db.Integer, db.ForeignKey('articulo.id'))
                                        )
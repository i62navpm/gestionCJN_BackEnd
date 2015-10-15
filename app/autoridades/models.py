from mongoengine import *
from app.cofrades.models import Cofrade


class Direccion(EmbeddedDocument):
    calle = StringField(required=True)
    municipio = StringField(required=True)
    provincia = StringField(required=True)
    cp = IntField(required=True)
    numero = IntField(required=True)
    planta = StringField()
    piso = StringField()


class Autoridad(Document):
    entidad = StringField(required=True)
    posicion = StringField()
    direccion = EmbeddedDocumentField(Direccion)
    telefono = StringField(regex=r'(\d{9})', max_length=9)
    email = EmailField()
    nota = StringField()
    meta = {'collection': 'Autoridad'}

    class Meta:
        ordering = ['entidad']
        verbose_name_plural = 'Autoridades'

    def __str__(self):
        return '%s %s' % (self.entidad.encode('iso8859_15'),
                          self.posicion.encode('iso8859_15') if self.posicion else '')
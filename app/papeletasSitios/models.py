from mongoengine import *
from app.cofrades.models import Cofrade


class Papeleta(EmbeddedDocument):
    fecha = StringField(required=True)
    cofrade = ReferenceField(Cofrade)


class PapeletaSitio(Document):
    anio = IntField(required=True, unique=True)
    papeletas = ListField(EmbeddedDocumentField(Papeleta))
    meta = {'collection': 'PapeletaSitio'}

    class Meta:
        ordering = ['anio']
        verbose_name_plural = 'PapeletasSitio'

    def __str__(self):
        return '%s %s' % (str(self.anio), len(self.papeletas))
from mongoengine import *
import datetime
from app.cofrades.models import Cofrade


class Costalero(Document):
    cofrade = ReferenceField(Cofrade)
    sitio = StringField(required=True, unique=True)
    fecha = StringField()
    talla = FloatField()
    meta = {'collection': 'Costalero'}

    class Meta:
        ordering = ['sitio']
        verbose_name_plural = 'Costaleros'

    def __str__(self):
        return '%s %s %s' % (str(self.sitio), str(self.cofrade.numeroOrden), str(self.cofrade))
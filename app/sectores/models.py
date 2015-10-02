from mongoengine import *
from app.cofrades.models import Cofrade


class Sector(Document):
    numeroSector = IntField(required=True, unique=True)
    cofrade = ReferenceField(Cofrade, dbref=False)
    calles = ListField(StringField())
    meta = {'collection': 'Sector'}

    class Meta:
        ordering = ['numeroSector']
        verbose_name_plural = 'Sectores'

    def __str__(self):
        return '%s %s %s' % (str(self.numeroSector), str(self.cofrade.numeroOrden), str(self.cofrade))
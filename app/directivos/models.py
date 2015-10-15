from mongoengine import *
from app.cofrades.models import Cofrade


class Directivo(Document):
    cofrade = ReferenceField(Cofrade)
    posicion = StringField(required=True)
    meta = {'collection': 'Directivo'}

    class Meta:
        ordering = ['posicion']
        verbose_name_plural = 'Directivos'

    def __str__(self):
        return '%s %s %s' % (str(self.posicion), str(self.cofrade.numeroOrden), str(self.cofrade))
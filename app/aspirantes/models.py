from mongoengine import *
from app.cofrades.models import Cofrade

class Aspirante(Document):
    cofrade = ReferenceField(Cofrade)
    fecha = StringField()
    meta = {'collection': 'Aspirante'}

    class Meta:
        ordering = ['fecha']
        verbose_name_plural = 'Aspirantes'

    def __str__(self):
        return '%s %s %s' % (str(self.fecha), str(self.cofrade.numeroOrden), str(self.cofrade))
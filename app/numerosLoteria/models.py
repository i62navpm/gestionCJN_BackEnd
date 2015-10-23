from mongoengine import *


class DatosLoteria(EmbeddedDocument):
    numero = IntField(required=True)
    precio = FloatField(required=True)

class NumerosLoteria(Document):
    navidad1 = EmbeddedDocumentField(DatosLoteria)
    navidad2 = EmbeddedDocumentField(DatosLoteria)
    ninio1 = EmbeddedDocumentField(DatosLoteria)
    ninio2 = EmbeddedDocumentField(DatosLoteria)
    meta = {'collection': 'NumerosLoteria'}

    class Meta:
        verbose_name_plural = 'numerosLoteria'

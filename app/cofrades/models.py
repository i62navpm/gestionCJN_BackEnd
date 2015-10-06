from mongoengine import *
import datetime


class Direccion(EmbeddedDocument):
    calle = StringField(required=True)
    municipio = StringField(required=True)
    provincia = StringField(required=True)
    cp = IntField(required=True)
    numero = IntField(required=True)
    planta = StringField()
    piso = StringField()


class DatosPersonales(EmbeddedDocument):
    nombre = StringField(required=True)
    apellido1 = StringField(required=True)
    apellido2 = StringField(required=True)
    dni = StringField(regex=r'(\d{8})([a-zA-Z]{1})', max_length=9)
    sexo = StringField(required=True, choices=('Hombre', 'Mujer'))
    direccion = EmbeddedDocumentField(Direccion)
    fechaNacimiento = StringField()
    fechaInscripcion = StringField()
    telefono = StringField(regex=r'(\d{9})', max_length=9)
    email = EmailField()
    nota = StringField()


class Cuenta(EmbeddedDocument):
    iban = StringField(regex=r'([A-Z]{2})(\d{22})', max_length=24)
    cc = StringField(regex=r'(\d{20})', max_length=20)


class DatosFinancieros(EmbeddedDocument):
    cuenta = EmbeddedDocumentField(Cuenta)
    banco = StringField()
    direccionBanco = StringField()
    domiciliarPagos = BooleanField()
    domiciliarLoteria = BooleanField()
    deuda = ListField(IntField())


class DatosLoteria(EmbeddedDocument):
    numeroNavidad1 = IntField()
    numeroNavidad2 = IntField()
    numeroNinio1 = IntField()
    numeroNinio2 = IntField()
    participacionNavidad = BooleanField()
    participacionNinio = BooleanField()


class Baja(EmbeddedDocument):
    fechaBaja = StringField(default=datetime.datetime.now)
    motivo = StringField(choices=('Voluntaria',
                                  'Fallecimiento',
                                  'Duplicidad',
                                  'Falta pago de 2 a\\u00f1os'))


class Cofrade(Document):
    numeroOrden = IntField(required=True, unique=True)
    numeroCofrade = IntField()
    datosPersonales = EmbeddedDocumentField(DatosPersonales)
    datosFinancieros = EmbeddedDocumentField(DatosFinancieros)
    datosLoteria = EmbeddedDocumentField(DatosLoteria)
    baja = EmbeddedDocumentField(Baja)
    meta = {'collection': 'Cofrade'}

    class Meta:
        ordering = ['numeroOrden', 'numeroCofrade']
        verbose_name_plural = 'Cofrades'

    def __str__(self):
        return '%s %s %s' % (self.datosPersonales['nombre'].encode('utf-8'),
                             self.datosPersonales['apellido1'].encode('utf-8'),
                             self.datosPersonales['apellido2'].encode('utf-8'))


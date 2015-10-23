from mongoengine import *
from app.cofrades.models import Cofrade

class GastoBancario(Document):
    gastoDomiciliacion = FloatField(min_value=0.0, required=True)
    gastoEnvioPostal = FloatField(min_value=0.0, required=True)
    meta = {'collection': 'GastoBancario'}

    class Meta:
        verbose_name_plural = 'GastosBancarios'

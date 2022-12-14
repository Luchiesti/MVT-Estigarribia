from AppFamiliares.models import Familiar
from django.http import HttpResponse
from django.template import loader, Template


"""
TODO 'Crear una web que permite ver los datos de algunos de tus familiares, guardados en una BD'

    1. Deberá tener un template, una vista y un modelo (cómo mínimo, pueden ser más)
    2. La clase del modelo, deberá guardar mínimo un número, una cadena y una fecha (puede guardar más cosas)
    3. Se deberá crear como mínimo 3 familiares
    4. Los familiares se deben ver desde la web
"""

def crear_familiares(request):
    familiar1 = Familiar(relacion='Madre', nombre='Emilia', apellido='Watson', fecha_nacimiento='1970-01-22', cedula=21575125)
    familiar2 = Familiar(relacion='Padre', nombre='Roberto', apellido='Estigarribia', fecha_nacimiento='1969-06-19', cedula=21859278)
    familiar3 = Familiar(relacion='Hermana', nombre='Emilia', apellido='Estigarribia', fecha_nacimiento= '1994-06-14', cedula=38942718)
    familiar1.save()
    familiar2.save()
    familiar3.save()

    contexto = {
        'informacion': {
            'Madre': familiar1,
            'Padre': familiar2,
            'Hermana': familiar3
        }
    }
    plantilla = loader.get_template('template1.html')
    documento_texto = plantilla.render(contexto)

    return HttpResponse(documento_texto)

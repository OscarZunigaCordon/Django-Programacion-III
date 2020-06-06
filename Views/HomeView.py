from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():

    def home(self):
        plantilla = get_template('Index.html')
        return HttpResponse(plantilla.render())

    def pagina1(self):
        return HttpResponse('Hola desde una nueva ruta')

    def pagina2(self, parametro1):
        return HttpResponse('Hola desde otra ruta con parametro ' + str(parametro1))

    def pagina3(self, parametro1, parametro2):
        return HttpResponse('Hola desde otra ruta con 2 parametro2 ' + str(parametro1)+ "-" + str(parametro2))

    def login(self):
        plantilla = get_template('login.html')
        return HttpResponse(plantilla.render())

    def gesAlumnos(self):
        plantilla = get_template('gesAlumnos.html')
        return HttpResponse(plantilla.render())

    def gesMaestros(self):
        plantilla = get_template('gesMaestros.html')
        return HttpResponse(plantilla.render())

    def gesClases(self):
        plantilla = get_template('gesClases.html')
        return HttpResponse(plantilla.render())

    def gesAsignacion(self):
        plantilla = get_template('gesAsignacion.html')
        return HttpResponse(plantilla.render())
from os import access
import requests
import json
import datetime
import gi
gi.require_version("Gtk", "3.0")
from typing import Protocol, Union

from gi.repository import Gtk

class Model: 
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.listaDatosPersonales = None
        self.pagInstalaciones = 0
        self.listaInstalaciones = None
        self.pagAlertas = 0
        self.tam_listaInstalaciones = 0
        self.dataAlertas = []
        self.listaIdInstalaciones = []
        self.formato_valido = 1
        self.listaDatosUser = []
        self.listaSitiosVisitados = []
        self.lista_radar = []
        self.i = 0
        self.j = 0

    def comprobar_servidor(self):
        try:
            r = requests.get("http://localhost:8080/api/rest/")
            return r.status_code != 200 
        except Exception:
            pass

        
    def info_persona(self, nombreapellido):

        list_NA = nombreapellido.split()
        if len(list_NA)==2:
            self.nombre = list_NA[0]
            self.apellido = list_NA[1]
        else:
            self.formato_valido = 0

        self.pagInstalaciones = 0

        #petición get datos personales
 
        r = requests.get("http://localhost:8080/api/rest/user?name="+self.nombre+"&surname="+self.apellido,
        headers={"x-hasura-admin-secret":"myadminsecretkey"})
        data = r.json() #data es dict
        self.listaDatosPersonales = data.get('users') #lista es list
        

    def info_instalaciones(self, limit = "&limit=5"): #limit es opcional
        #peticion get instalaciones con y sin limit dependiendo para que se vaya a usar
        r = requests.get("http://localhost:8080/api/rest/user_access_log/"+self.listaDatosPersonales[0].get('uuid')+"?offset="+str(self.pagInstalaciones)+limit,
        headers={"x-hasura-admin-secret":"myadminsecretkey"})

        #if para no sobreescribir los datos guardados para las alertas y para las instalciones de usuario
        if(limit == "&limit=5"):
            dataInstalaciones = r.json()
            self.listaInstalaciones = dataInstalaciones.get('access_log') #lista es list
            self.tam_listaInstalaciones = len(self.listaInstalaciones)
        else:
            dataInstalaciones = r.json()
            self.listaInstalacionesAlertas = dataInstalaciones.get('access_log') #lista es list
            


    def info_alertas(self, fechaI, fechaF):
        self.lista_personas_en_edificios = []
        lista_horas = []
        aux = []
        self.lista_radar = []

        r = requests.get(
        "http://localhost:8080/api/rest/user_access_log/"+self.listaDatosPersonales[0].get('uuid')+"/daterange",
        headers={"x-hasura-admin-secret": "myadminsecretkey"},
        json={"startdate": fechaI, "enddate": fechaF})
        data = r.json()
        data_horas = data.get('access_log')

        for i in range(len(data_horas)):
            lista_horas.append([data_horas[i].get('facility').get('id'),data_horas[i].get('timestamp')])


        # obtengo una lista {id, fechaInicio, fechaFin}
        for i in range(0, int((len(lista_horas) / 2))):
            id = lista_horas[i][0]
            for j in range(i + 1, len(lista_horas)):
                if id == lista_horas[j][0]:
                    lista_horas[i].append(lista_horas[j][1])
                    if (lista_horas[i][1] > lista_horas[i][2]):
                        aux = lista_horas[i][1]
                        lista_horas[i][1] = lista_horas[i][2]
                        lista_horas[i][2] = aux
                    lista_horas.pop(j)
                    break


        for i in range(len(lista_horas)):

            r = requests.get(
            f"http://localhost:8080/api/rest/facility_access_log/{lista_horas[i][0]}/daterange",
            headers={"x-hasura-admin-secret": "myadminsecretkey"},
            json={"startdate": lista_horas[i][1], "enddate": lista_horas[i][2]})

            data = r.json()

          
            self.lista_personas_en_edificios.append(data)

        for i in range(len(self.lista_personas_en_edificios)):
           for j in range(len(self.lista_personas_en_edificios[i].get('access_log'))):
               aux.append([self.lista_personas_en_edificios[i].get('access_log')[j].get('user').get('name'),
                                  self.lista_personas_en_edificios[i].get('access_log')[j].get('user').get('surname'),
                                  self.lista_personas_en_edificios[i].get('access_log')[j].get('user').get('phone'),
                                  self.lista_personas_en_edificios[i].get('access_log')[j].get('user').get('is_vaccinated')])


        for i in range(len(aux)):
            if aux[i] not in self.lista_radar:
                self.lista_radar.append(aux[i])




    def eliminar_usuario_repetidos(self):
        lista = self.lista_personas_en_edificios

        for i in range(len(lista) - 1):
            user = lista[i].get('access_log')[0].get('user').get('uuid')
            for j in range(i + 1, len(lista)):
                if (user == lista[i].get('access_log').get('user').get('uuid')):
                    lista.pop(i)
                # Nos eliminamos a nosotros mismos
                if (lista[i].get("acces_log").get('uuid') == lista[i].get('user').get('uuid')):
                    lista.pop(i)


    


                
    
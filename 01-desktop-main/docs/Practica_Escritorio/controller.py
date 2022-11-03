import model
import view
import datetime
from dateutil.parser import *

import threading
from gi.repository import GLib

class Controller:

    def __init__(self):
        #el controller se encarga de crear
        self.model = model.Model() #creamos modelo
        self.view = view.View() #creamos view y le pasamos el estado actual
        self.view.connect_buscar_clicked(self.on_buscar_clicked) #usamos el metodo connect para decirle a la vista que cuando pulse el boton ejecute self.on_buscar_clicked
        
        self.view.connect_retroceder_instalaciones(self.on_retroceder_instalaciones_clicked)
        self.view.connect_avanzar_instalaciones(self.on_avanzar_instalaciones_clicked)

        #self.view.connect_buscar_alertas_clicked(self.on_buscar_alertas_clicked)
        #self.view.connect_retroceder_alertas(self.on_retroceder_alertas_clicked)
        #self.view.connect_avanzar_alertas(self.on_avanzar_alertas_clicked)

    def on_buscar_clicked(self, button):
        text = self.view.entry.get_text()
        if(text != ""):
            #Comprobamos que es server esta activo
            if(self.model.comprobar_servidor()):

                threading.Thread(target= self.model.info_persona(text), name="Server petition Thread", daemon= True).start()
        
                #self.model.info_persona(text)
                self.resultado = self.model.listaDatosPersonales    
                self.on_formato_valido()

                self.view.connect_buscar_alertas_clicked(self.on_buscar_alertas_clicked)
                self.view.connect_retroceder_alertas(self.on_retroceder_alertas_clicked)
                self.view.connect_avanzar_alertas(self.on_avanzar_alertas_clicked)

                GLib.idle_add(lambda: self.view.update_view_Instalaciones(self.model.listaInstalaciones, self.model.pagInstalaciones, self.model.tam_listaInstalaciones))
            else:
                self.view.error_server()
        else: 
            self.view.formato_invalido()

#############################INSTALACIONES################################

    def on_retroceder_instalaciones_clicked(self, button):
        
        #Comprobamos que el server esta activo
        if(self.model.comprobar_servidor()):
            threading.Thread(target= self.model.info_instalaciones(), name="Server petition Thread", daemon= True).start()
            self.model.pagInstalaciones = self.model.pagInstalaciones -5
            self.model.info_instalaciones()
            # Volvemos al thread principal
            GLib.idle_add(lambda: self.view.update_view_Instalaciones(self.model.listaInstalaciones, self.model.pagInstalaciones, self.model.tam_listaInstalaciones))
        else: 
            self.view.error_server()

    def on_avanzar_instalaciones_clicked(self, button):
        
        #Comprobamos que el server esta activo
        if(self.model.comprobar_servidor()):
            threading.Thread(target= self.model.info_instalaciones(), name="Server petition Thread", daemon= True).start()
            self.model.pagInstalaciones = self.model.pagInstalaciones + self.model.tam_listaInstalaciones
            self.model.info_instalaciones()
            #self.view.update_view_Instalaciones(self.model.listaInstalaciones, self.model.pagInstalaciones, self.model.tam_listaInstalaciones )
            # Volvemos al thread principal
            GLib.idle_add(lambda: self.view.update_view_Instalaciones(self.model.listaInstalaciones, self.model.pagInstalaciones, self.model.tam_listaInstalaciones))
        else:
            self.view.error_server()


#######################ALERTAS##############################

    def comprobar_fechas(self, fecha):
        try:
            #retorna true si la fecha es valida
            parse(fecha)
            return True
            
        except Exception:
            return False

    def on_buscar_alertas_clicked(self, button):
        
        fi = self.view.entryfi.get_text()
        ff = self.view.entryff.get_text()

        fihora = fi+"T00:00:00+00:000"
        ffhora = ff+"T00:00:00+00:000"

        if(self.comprobar_fechas(fi) and self.comprobar_fechas(ff)):
        
            if(fi <= ff) :
                
                #self.model.info_alertas(fihora, ffhora)
                if(self.model.comprobar_servidor()):
                    threading.Thread(target= self.model.info_alertas(fihora, ffhora), name="Server petition Thread", daemon= True).start()

                    #self.view.update_view_Alertas(self.model.lista_radar, self.model.pagAlertas)
                    # Volvemos al thread principal
                    GLib.idle_add(lambda: self.view.update_view_Alertas(self.model.lista_radar, self.model.pagAlertas))
                else:
                    self.view.error_server()
            else :
                self.view.fechas_invalidas()
        else:
            self.view.fechas_correctas()

    def on_retroceder_alertas_clicked(self, button):
        aux = []
        cont = 0
        

        self.model.pagAlertas = self.model.pagAlertas - 5

        for i in range(len(self.model.lista_radar)):
            if(i>=self.model.pagAlertas and cont<5):
                aux.append(self.model.lista_radar[i])
                cont = cont + 1
        
        self.view.update_view_Alertas(aux, self.model.pagAlertas)

    def on_avanzar_alertas_clicked(self, button):
        aux = []
        cont = 0

        self.model.pagAlertas = self.model.pagAlertas + 5

        for i in range(len(self.model.lista_radar)):
            if(i>=self.model.pagAlertas and cont<5):
                aux.append(self.model.lista_radar[i])
                cont = cont + 1

        self.view.update_view_Alertas(aux, self.model.pagAlertas)

    #######################COMPROBACIONES##############################

    def on_formato_valido(self):
        if(self.model.formato_valido == 1):
            #GLib.idle_add(lambda: self.on_existe_usuario())
            self.on_existe_usuario()
        else:
            #GLib.idle_add(lambda: self.view.formato_invalido)
            self.view.formato_invalido()

    def on_existe_usuario(self):
        if(self.model.listaDatosPersonales):
            
            self.model.info_instalaciones()
            #GLib.idle_add(lambda: self.view.update_view_infoPersona(self.resultado))
            self.view.update_view_infoPersona(self.model.listaDatosPersonales)
            self.view.update_view_Instalaciones(self.model.listaInstalaciones, self.model.pagInstalaciones, self.model.tam_listaInstalaciones)
        else:
            #GLib.idle_add(lambda: self.view.no_existe_usuario())
            
            self.view.no_existe_usuario()

    def start(self):
        view.start()

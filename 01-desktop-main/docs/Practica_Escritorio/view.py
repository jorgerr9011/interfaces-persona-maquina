import gi
import qrcode

import locale
import gettext
_ = gettext.gettext
N_ = gettext.ngettext

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Atk

class View(Gtk.Window):

    def __init__(self):  # cuando se inicializa/crea se le pasa el estado en este caso count

        w = Gtk.Window(title="PyCalc1.0")
        w.connect('destroy', Gtk.main_quit)

        #w.set_default_size(1000, 1000)
        #w.Gtk_Maximize()

        vbox = Gtk.VBox(spacing=8, margin=12)
        w.add(vbox)

        hbox = Gtk.HBox(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        self.entry = Gtk.SearchEntry()
        entry_accessible = self.entry.get_accessible()
        entry_accessible.set_name("Introducir_nombre")
        self.entry.set_text("")

        hbox.pack_start(self.entry, False, False, 0)

        self.button = Gtk.Button.new_with_label("Buscar")
        button_accessible = self.button.get_accessible()
        button_accessible.set_name('Boton_buscar_persona')
        hbox.pack_start(self.button, False, False, 0)

        #########################################################################

        vbox1 = Gtk.VBox(spacing=6)

        self.labelVacio = Gtk.Label(label=' ')
        self.labelDatos = Gtk.Label(label='DATOS DEL USUARIO')

        self.liststore = Gtk.ListStore(str, str, str, str, str, str, str)

        self.liststore.append([" ", " ", " ", " ", " ", " ", " "])


        treeview = Gtk.TreeView(model=self.liststore)
        treeview_accessible = treeview.get_accessible()
        treeview_accessible.set_name("Info_usuario")
        renderer_txt = Gtk.CellRendererText()
        column_txt = Gtk.TreeViewColumn("uuid", renderer_txt, text=0)


        treeview.append_column(column_txt)

        renderer_txt1 = Gtk.CellRendererText()
        column_txt1 = Gtk.TreeViewColumn("Username", renderer_txt1, text=1)
        treeview.append_column(column_txt1)

        renderer_txt2 = Gtk.CellRendererText()
        column_txt2 = Gtk.TreeViewColumn("Name", renderer_txt2, text=2)
        treeview.append_column(column_txt2)

        renderer_txt3 = Gtk.CellRendererText()
        column_txt3 = Gtk.TreeViewColumn("Surname", renderer_txt3, text=3)
        treeview.append_column(column_txt3)

        renderer_txt4 = Gtk.CellRendererText()
        column_txt4 = Gtk.TreeViewColumn("Email", renderer_txt4, text=4)
        treeview.append_column(column_txt4)

        renderer_txt5 = Gtk.CellRendererText()
        column_txt5 = Gtk.TreeViewColumn("Phone", renderer_txt5, text=5)
        treeview.append_column(column_txt5)

        renderer_txt6 = Gtk.CellRendererText()
        column_txt6 = Gtk.TreeViewColumn("is_vaccinated", renderer_txt6, text=6)
        treeview.append_column(column_txt6)

        self.image = Gtk.Image()

        vbox1.pack_start(self.labelVacio, True, True, 0)
        vbox1.pack_start(self.labelDatos, True, True, 0)
        vbox1.pack_start(treeview, True, True, 0)
        vbox1.pack_start(self.image, False, False, 0)
        vbox.pack_start(vbox1, True, True, 0)

        ###########################################################################################

        vbox2 = Gtk.VBox(spacing=6)

        self.labelVacio = Gtk.Label(label=' ')
        self.labelInstalaciones = Gtk.Label(label='INSTALACIONES VISITADAS')

        self.liststore1 = Gtk.ListStore(str, str, str, str, str, str)
        self.liststore1.append([" ", " ", " ", " ", " ", " "])
        self.liststore1.append([" ", " ", " ", " ", " ", " "])
        self.liststore1.append([" ", " ", " ", " ", " ", " "])
        self.liststore1.append([" ", " ", " ", " ", " ", " "])
        self.liststore1.append([" ", " ", " ", " ", " ", " "])

        treeview1 = Gtk.TreeView(model=self.liststore1)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Instalación", renderer_text, text=0)
        treeview1.append_column(column_text)

        renderer_text1 = Gtk.CellRendererText()
        column_text1 = Gtk.TreeViewColumn("Calle", renderer_text1, text=1)
        treeview1.append_column(column_text1)

        renderer_text2 = Gtk.CellRendererText()
        column_text2 = Gtk.TreeViewColumn("Id", renderer_text2, text=2)
        treeview1.append_column(column_text2)

        renderer_text3 = Gtk.CellRendererText()
        column_text3 = Gtk.TreeViewColumn("Temperatura", renderer_text3, text=3)
        treeview1.append_column(column_text3)

        renderer_text4 = Gtk.CellRendererText()
        column_text4 = Gtk.TreeViewColumn("Timestamp", renderer_text4, text=4)
        treeview1.append_column(column_text4)

        renderer_text5 = Gtk.CellRendererText()
        column_text5 = Gtk.TreeViewColumn("Type", renderer_text5, text=5)
        treeview1.append_column(column_text5)

        ####BOTONES AVANZAR Y RETROCEDER EN INSTALACIONES####

        hboxButtonsLR = Gtk.HBox(spacing=6)

        self.buttonL = Gtk.Button.new_with_label("<")
        hboxButtonsLR.pack_start(self.buttonL, False, False, 0)
        self.buttonL.set_sensitive(False)

        self.buttonR = Gtk.Button.new_with_label(">")
        hboxButtonsLR.pack_start(self.buttonR, False, False, 0)
        self.buttonR.set_sensitive(False)

        vbox2.pack_start(self.labelVacio, True, True, 0)
        vbox2.pack_start(self.labelInstalaciones, True, True, 0)
        vbox2.pack_start(treeview1, True, True, 0)
        vbox2.pack_start(hboxButtonsLR, False, False, 0)
        vbox.pack_start(vbox2, True, True, 0)

        ###############################################################################

        vbox3 = Gtk.VBox(spacing=6)
        hbox1 = Gtk.HBox(spacing=6)

        self.labelVacio = Gtk.Label(label=' ')
        self.labelAlertas = Gtk.Label('RASTREAR ALERTAS COVID-19')

        
        self.entryfi = Gtk.Entry()
        self.entryfi.set_text("") #YYYY-MM-DD
        self.entryfi.set_placeholder_text("YYYY-MM-DD")
        fi_accessible = self.entryfi.get_accessible()
        fi_accessible.set_name('Fecha_inicial')
        hbox1.pack_start(self.entryfi, False, False, 0)

        self.entryff = Gtk.Entry()
        self.entryff.set_text("") #YYYY-MM-DD
        self.entryff.set_placeholder_text("YYYY-MM-DD")
        ff_accessible = self.entryff.get_accessible()
        ff_accessible.set_name('Fecha_final')
        hbox1.pack_start(self.entryff, False, False, 0)
        
        self.buttonBuscarAlertas = Gtk.Button.new_with_label("Buscar")
        buttonAlertas_accessible = self.buttonBuscarAlertas.get_accessible()
        buttonAlertas_accessible.set_name('Boton_Alertas_Covid')
        hbox1.pack_start(self.buttonBuscarAlertas, False, False, 0)
        
        vbox3.pack_start(self.labelVacio, True, True, 0)
        vbox3.pack_start(self.labelAlertas, True, True, 0)
        vbox3.pack_start(hbox1, True, True, 0)

        self.liststore2 = Gtk.ListStore(str, str, str, str)
        self.liststore2.append([" ", " ", " "," "])
        self.liststore2.append([" ", " ", " "," "])
        self.liststore2.append([" ", " ", " "," "])
        self.liststore2.append([" ", " ", " "," "])
        self.liststore2.append([" ", " ", " "," "])

        treeview2 = Gtk.TreeView(model=self.liststore2)

        renderer_textt = Gtk.CellRendererText()
        column_textt = Gtk.TreeViewColumn("Nombre", renderer_textt, text=0)
        treeview2.append_column(column_textt)

        renderer_textt1 = Gtk.CellRendererText()
        column_textt1 = Gtk.TreeViewColumn("Apellido", renderer_textt1, text=1)
        treeview2.append_column(column_textt1)

        renderer_textt2 = Gtk.CellRendererText()
        column_textt2 = Gtk.TreeViewColumn("phone", renderer_textt2, text=2)
        treeview2.append_column(column_textt2)

        renderer_textt3 = Gtk.CellRendererText()
        column_textt3 = Gtk.TreeViewColumn("is_vaccinated", renderer_textt3, text=3)
        treeview2.append_column(column_textt3)

        vbox3.pack_start(treeview2, True, True, 0)

        hboxButtonsLR1 = Gtk.HBox(spacing=6)

        self.buttonL1 = Gtk.Button.new_with_label("<")
        hboxButtonsLR1.pack_start(self.buttonL1, False, False, 0)
        self.buttonL1.set_sensitive(False)

        self.buttonR1 = Gtk.Button.new_with_label(">")
        buttonR1_accessible = self.buttonR1.get_accessible()
        buttonR1_accessible.set_name('Avanzar_alertas_covid')
        hboxButtonsLR1.pack_start(self.buttonR1, False, False, 0)
        self.buttonR1.set_sensitive(False)

        vbox3.pack_start(hboxButtonsLR1, False, False, 0)

        vbox.pack_start(vbox3, True, True, 0)

        self.w = w
        #s = Gtk.Screen.get_default()
        self.w.set_default_size(1, 1)
        #w.set_default_size(1000, 1000)
        self.w.show_all()

    # conectar el metodo clicked con el controlador

    #######################PERSONAS&INSTALACIONES############################
    def connect_buscar_clicked(self, handler):
        self.button.connect('clicked', handler)

    def connect_retroceder_instalaciones(self, handler):
        self.buttonL.connect('clicked', handler)

    def connect_avanzar_instalaciones(self, handler):
        self.buttonR.connect('clicked', handler)

    ################################ALERTAS##################################33
    def connect_buscar_alertas_clicked(self, handler):
        self.buttonBuscarAlertas.connect('clicked', handler)

    def connect_retroceder_alertas(self, handler):
        self.buttonL1.connect('clicked', handler)

    def connect_avanzar_alertas(self, handler):
        self.buttonR1.connect('clicked', handler)

    def update_view_infoPersona(self, lista):
        self.liststore[0][0] = lista[0].get('uuid')
        self.liststore[0][1] = lista[0].get('username')
        self.liststore[0][2] = lista[0].get('name')
        self.liststore[0][3] = lista[0].get('surname')
        self.liststore[0][4] = lista[0].get('email')
        self.liststore[0][5] = lista[0].get('phone')
        aux = 'False' if lista[0].get('is_vaccinated') == False else 'True'
        self.liststore[0][6] = aux

        img = qrcode.make("{"+lista[0].get('name')+"}, {"+lista[0].get('surname')+"}, {"+lista[0].get('uuid')+"}")
        #type(img)  # qrcode.image.pil.PilImage
        img.save("some_file.png")
        self.image.set_from_file("some_file.png")

    def update_view_Instalaciones(self, lista, numero_pag, len_instalaciones):
        i = 0
        for i in range(len_instalaciones):
            self.liststore1[i][0] = lista[i].get('facility').get('name')
            self.liststore1[i][1] = lista[i].get('facility').get('address')
            self.liststore1[i][2] = str(lista[i].get('facility').get('id'))
            self.liststore1[i][3] = lista[i].get('temperature')
            timestamp = lista[i].get('timestamp')[:-22]
            self.liststore1[i][4] = timestamp
            self.liststore1[i][5] = lista[i].get('type')

        if len_instalaciones != 5:
            for j in range(len_instalaciones, 5):
                self.liststore1[j][0] = ""
                self.liststore1[j][1] = ""
                self.liststore1[j][2] = ""
                self.liststore1[j][3] = ""
                self.liststore1[j][4] = ""
                self.liststore1[j][5] = ""


        if numero_pag >= 5:
            self.buttonL.set_sensitive(True)
        else:
            self.buttonL.set_sensitive(False)
        if numero_pag >= 0:
            self.buttonR.set_sensitive(True)
        #Ojo!!!!!! mirar pq no se cumple si len_instalaciones es multiplo de 5 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!! PABLO BELLO PUÑAL !!!!!!
        if len_instalaciones != 5:
            self.buttonR.set_sensitive(False)
        #Activamos el boton de busqueda por alertas
        self.buttonBuscarAlertas.set_sensitive(True)

    def update_view_Alertas(self, lista, numero_pag):
        # Como ya hemos realizado la busqueda, lo desactivamos
        self.buttonBuscarAlertas.set_sensitive(False)
        self.buttonR1.set_sensitive(True)

        cont = 0

        for i in range(len(lista)):
            self.liststore2[i][0] = lista[i][0]
            self.liststore2[i][1] = lista[i][1]
            self.liststore2[i][2] = lista[i][2]
            aux = 'False' if lista[i][3] == False else 'True'
            self.liststore2[i][3] = aux
            cont = cont + 1


        if len(lista) != 5:
            for j in range(len(lista), 5):
                self.liststore2[j][0] = ""
                self.liststore2[j][1] = ""
                self.liststore2[j][2] = ""
                self.liststore2[j][3] = ""


        if numero_pag >= 5:
            self.buttonL1.set_sensitive(True)
        else:
            self.buttonL1.set_sensitive(False) 

        
        #Ojo!!!!!! mirar pq no se cumple si len_instalaciones es multiplo de 5 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!! PABLO BELLO PUÑAL !!!!!!
        if cont != 5:
            self.buttonR1.set_sensitive(False)
        

    ################################ERRORES####################################
    def no_existe_usuario(self):
        dialog = Gtk.MessageDialog(parent = self.w, 
                                    message_type = Gtk.MessageType.ERROR,
                                    buttons = Gtk.ButtonsType.CLOSE,
                                    text = "NO EXISTE USUARIOS CON ESE NOMBRE")
        
        dialog.run()
        dialog.destroy()
        

    def formato_invalido(self):
        dialog = Gtk.MessageDialog(parent = self.w, 
                                    message_type = Gtk.MessageType.ERROR,
                                    buttons = Gtk.ButtonsType.CLOSE,
                                    text = "ASEGURESE DE PONER NOMBRE Y APELLIDO")
        
        dialog.run()
        dialog.destroy()

    def fechas_invalidas(self):
        dialog = Gtk.MessageDialog(parent = self.w, 
                                    message_type = Gtk.MessageType.ERROR,
                                    buttons = Gtk.ButtonsType.CLOSE,
                                    text = "Fecha inicial menor que fecha final")
        
        dialog.run()
        dialog.destroy()

    def error_server(self):
        dialog = Gtk.MessageDialog(parent = self.w, 
                                    message_type = Gtk.MessageType.ERROR,
                                    buttons = Gtk.ButtonsType.CLOSE,
                                    text = "IMPOSIBLE CONECTAR CON BD")
        
        dialog.run()
        dialog.destroy()

    def fechas_correctas(self):
        dialog = Gtk.MessageDialog(parent = self.w, 
                                    message_type = Gtk.MessageType.ERROR,
                                    buttons = Gtk.ButtonsType.CLOSE,
                                    text = "ASEGURESE DE PONER LAS DOS FECHAS CORRECTAMENTE")
        
        dialog.run()
        dialog.destroy()

def start():
    Gtk.main()


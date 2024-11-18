#!/usr/bin/python3

# Front-End Gtk para módulo enrut

# Importo clase Enrut para representar mapa de noticias
from enrut import Enrut
# Importo toolkit grafico Gtk mediante GObject para tener una interfaz grafica compatible con varias distros Linux
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
# Definoo interfaz
class PanelDividido(Gtk.Window):

    def __init__(self, titulo = 'Ventana Nueva', ancho = 100, alto = 100):
        # Defino titulo
        super().__init__(title = titulo)
        # Defino tamaño de ventana
        self.set_size_request(ancho, alto)
        # Agrego los widgets como atributos ya que es el formato de Gtk, dos contenerdores, dos botones, un formulario y vista de arbol
        self.primer_contenedor = Gtk.VBox(spacing = 20)
        self.segundo_contenedor = Gtk.VBox(spacing = 30)
        self.gran_contenedor = Gtk.HBox(spacing = 35)
        # Decripcion del software
        self.descripcion = Gtk.Label(label = '[ Traza fuentes y destinos de una noticia ]')
        # Boton para agregar archivo
        self.archivo = Gtk.Button(label = 'archivo CSV de noticias')
        self.archivo.connect('clicked', self.elegir_archivo)
        self.archivo.set_border_width(5)
        # Formulario de noticias
        self.nombrar = Gtk.Entry(placeholder_text = 'Noticia')
        self.fechar = Gtk.Entry(placeholder_text = 'Fecha dd/mm/aaaa')
        self.describir = Gtk.Entry(placeholder_text = 'Modificaciones a la original')
        # Boton para representar mapa con archivo y/o datos de formulario (si los hay)
        self.trazar = Gtk.Button(label = 't\nr\na\nz\na\nr\n')
        self.trazar.connect('clicked', self.trazado)
        self.set_border_width(5)
        # Agrego widgets
        self.arbol = Gtk.Label()
        self.primer_contenedor.add(self.arbol)
        for widget in [self.descripcion, self.archivo, Gtk.Label(label = '( Noticia )'), self.nombrar, Gtk.Label(label = '( Fecha dd/mm/aaaa )'), self.fechar, Gtk.Label(label = '( Modificaciones a la original )'), self.describir]:
            self.segundo_contenedor.add(widget)
        # Agrego contenerdor a la ventana sino no se veran los widgets
        self.gran_contenedor.add(self.primer_contenedor)
        self.gran_contenedor.add(self.segundo_contenedor)
        self.gran_contenedor.add(self.trazar)
        self.add(self.gran_contenedor)
    # Defino eventos de botones
    def trazado(self, trazar):
        # Creo objeto mapa de noticias
        mapa = Enrut()
        # Lo inicializo
        mapa.noticia = self.nombrar.get_text()
        mapa.fecha = self.fechar.get_text()
        mapa.modificaciones = self.describir.get_text()
        self.arbol.set_text(self.arbol.get_text() + f'\n* {mapa.noticia}: {mapa.modificaciones} el {mapa.fecha}\n')
        # Actualizo con los nuevos datos en el archivo principal del software
        mapa.actualizar('Traza-Noticias.csv')

    def elegir_archivo(self, archivo):
        selector = Gtk.FileChooserDialog(title = 'Elegir archivo CSV de forma "Noticia, Modificaciones, Fecha"', parent = self, action = Gtk.FileChooserAction.OPEN)
        # Agrego botones para que sea mas facil de manejar
        selector.add_buttons(Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
        # Agrego filtro para archivos CSV
        filtro = Gtk.FileFilter()
        filtro.set_name('Archivo CSV: Noticia, Modificaciones, Fecha')
        filtro.add_mime_type('text/csv')
        selector.add_filter(filtro)
        # Inicio ventana emergente
        selector.run()
        # Altero todo segun archivo seleccionado
        mapa = Enrut()
        mapa.analizar(selector.get_filename())
        mapa.ligar(mapa)
        # Actualizo vista de arbol
        for original in mapa.fuentes:
            self.arbol.set_text(self.arbol.get_text() + f'\n* {original.noticia}: {original.modificaciones} el {original.fecha}\n')
        # Cierro ventana emergente
        selector.destroy()

# Creo interfaz
if (__name__ == '__main__'):
    # Creo objeto ventana con todos sus widgets
    ventana = PanelDividido('Ruta de noticias', 500, 500)
    # Cuidadosamente la muestro
    try:
        ventana.show_all()
        Gtk.main()
    except:
        ventana.close()
        print('\nFIN DE VENTANA\n')

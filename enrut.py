class Enrut():

    '''
        © 2024 <nicolaspauer20@gmail.com>

        Crea una abstraccion para representar contenido
        de una noticia, fecha y su recorrido para ver su
        evolución a lo largo del tiempo.

        Propiedades:

            - noticia, texto con nombre y detalles de la noticia

            - modificaciones, texto con modificaciones que hizo destino a la fuente

            - fecha, texto con fecha de la noticia en formato DD/MM/AAAA (2 digitos de dia, 2 digitos de mes y 4 digitos de año)

            - fuentes, lista de objetos de esta clase con noticias fuente

            - destinos, lista de objetos de esta clase con noticias de destino

        Métodos:

            - ligar(noticia), relaciona a otra noticia (objeto Enrut)

            - desligar(noticia), elimina relacion (objeto Enrut)

            - analizar(archivo), carga datos de CSV al objeto de esta clase que lo use

            - actualizar(archivo), copia datos a CSV al objeto de esta clase que lo use
    '''
    def __init__(self):

        self.noticia:str = ''

        self.modificaciones:str = ''

        self.fecha:str = ''

        self.fuentes:list = []

        self.destinos:list = []

    def ligar(self, noticia):
        '''
            Relaciona la noticia a otra, si la noticia a ligar es de fecha anterior o igual
            va a fuentes sino va a destinos(mediante objetos de esta clase).
        '''

        fecha_objeto = self.fecha.split('/')

        fecha_noticia = noticia.fecha.split('/')
        # Todo anterior, mismo año y mes anterior, año anterior o mismo año y mes pero de dia anterior
        anterior = (((int(fecha_noticia[0]) <= int(fecha_objeto[0])) and (int(fecha_noticia[1]) <= int(fecha_objeto[1])) and (int(fecha_noticia[2]) <= int(fecha_objeto[2]))) or ((int(fecha_noticia[2]) == fecha_objeto[2]) and (int(fecha_noticia[1]) <= int(fecha_objeto[1]))) or (int(fecha_noticia[2]) <= int(fecha_objeto[2]))) or ((int(fecha_noticia[2]) == fecha_objeto[2])) and (int(fecha_noticia[1]) == fecha_objeto[1]) and ((int(fecha_noticia[0]) <= int(fecha_objeto[0])))

        if (anterior and (not self.fuentes.__contains__(noticia))):

            self.fuentes.append(noticia)

        elif (not self.destinos.__contains__(noticia)):

            self.destinos.append(noticia)

    def desligar(self, noticia):
        '''
            Deja de relacionar una noticia si es erronea
        '''
        if self.fuentes.__contains__(noticia):

            self.fuentes.remove(noticia)

        elif self.destinos.__contains__(noticia):

            self.destinos.remove(noticia)

    def analizar(self, archivo:str):
        '''
            Copia al objeto datos de un archivo CSV (Noticia, Modificaciones, Fecha) en
            sus respectivas propiedades de texto.
        '''
        arch = open(str(archivo).replace(' ', '-'), 'r')
        # Copio datos de linea siguiente a cabecera
        linea = arch.readlines()
        # Copio primera linea al objeto y el resto a fuentes o destinos
        self.noticia = linea[1].split(',')[0]

        self.modificaciones = linea[1].split(',')[1]

        self.fecha = linea[1].replace(' ', '').replace('\n', '').split(',')[2]
        # Copio el resto desde la segunda linea
        lineas = 2

        while (lineas < linea.__len__()):
            # Creo copia del objeto
            copia = Enrut()
            # Copio datos al objeto copia
            copia.noticia = linea[lineas].split(',')[0]

            copia.modificaciones = linea[lineas].split(',')[1]

            copia.fecha = linea[lineas].replace(' ', '').replace('\n', '').split(',')[2]
            # Uso metodo ligar para enlazar objeto copia que automaticamente lleva a fuentes o destinos
            self.ligar(copia)
            # Incremento lineas para evitar bucle infinito
            lineas += 1
        # Cierro archivo porque lo deje de usar
        arch.close()

    def actualizar(self, archivo:str):
        '''
            Copia a ultima fila de archivo CSV (Noticia, Modificaciones, Fecha)
            valores de las respectivas propiedades de texto.
        '''
        arch = open(str(archivo).replace(' ', '-'), 'a')
        arch.write(f'{str(self.noticia)}, {str(self.modificaciones)}, {str(self.fecha)}\n')
        arch.close()

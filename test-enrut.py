#!/usr/bin/python3

# Importo clase como objeto enrutador
from enrut import Enrut
# Inicializo objeto sino no anda
enrutador = Enrut()
# Ligo noticias
enrutador.analizar('Traza-Noticias.csv')
enrutador.ligar(enrutador)
# Muestro contenido de enrutador
def mostrar(objeto):
    print(f"\t{objeto.fecha} '{objeto.modificaciones}' es una fuente: [{objeto.noticia.upper()}]\n\n")
# Cito fuentes
print('Fuentes:\n')
# Muestro fuentes y destinos
for fuente in enrutador.fuentes:
    mostrar(fuente)
# Muestro lugares de destinos
print('\nDestinos:\n')
for destino in enrutador.destinos:
    mostrar(destino)

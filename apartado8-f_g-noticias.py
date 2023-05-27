import fasttext
import json

global escritor
escritor = open("datos_adicionales/apartado8/comparacion-clasificador-manual.txt", "w", encoding='utf-8')

lista = list()


def escribeLinea(texto=""):
    escritor.write(texto + "\n")


# Cargando el archivo ndjson

# Abrimos el archivo especificando que tiene formato utf-8
with open('datos_adicionales/apartado8/lista-labels.noticias.ndjson',
          encoding='utf-8') as archivo:
    lineas = archivo.readlines()

textos = list()
for linea in lineas:
    try:
        data = json.loads(linea)
        textos.append(data)
    except:
        pass

labels = ["calentamiento_global", "emisiones_gas", "incendios_forestales",
          "ola_calor", "subida_nivel_mar", "escasez_agua", "off_topic"]

# Seleccionadas de forma aleatoria pero dejadas fija debido a que se pondrán de forma manual las etiquetas
noticias_a_escoger = [7, 50, 13, 81, 6, 35, 42, 41, 66, 21]

noticia_y_etiqueta = list()
for noticia in noticias_a_escoger:
    noticia_y_etiqueta.append(textos[noticia])

print()

list_etiqueta_manual = list()

list_etiqueta_manual.append("off_topic")
list_etiqueta_manual.append("emisiones_gas")
list_etiqueta_manual.append("off_topic")
list_etiqueta_manual.append("emisiones_gas")
list_etiqueta_manual.append("emisiones_gas")
list_etiqueta_manual.append("off_topic")
list_etiqueta_manual.append("off_topic")
list_etiqueta_manual.append("off_topic")
list_etiqueta_manual.append("incendios_forestales")
list_etiqueta_manual.append("off_topic")

# Aquí comienzo un procesamiento muy largo para ir obteniendo las apariciones de cada etiqueta tanto de forma manual
# como según el clasificador, contando los aciertos y aparciones para luego ir poco a poco añadiéndolo en el txt de
# resultados que se encuentra en la carpeta apartado 8

list_etiqueta_clasificador = list()
for i in range(len(list_etiqueta_manual)):
    escribeLinea("Noticia " + str(i))
    escribeLinea("\tEtiquetado manual = " + list_etiqueta_manual[i])
    clave_max = max(noticia_y_etiqueta[i]["etiquetas"], key=lambda k: noticia_y_etiqueta[i]["etiquetas"][k])
    list_etiqueta_clasificador.append(clave_max)
    escribeLinea("\tEtiquetado clasificador = " + clave_max)
    escribeLinea("\tTotal de etiquetado por el clasificador")
    for element in noticia_y_etiqueta[i]["etiquetas"].keys():
        escribeLinea("\t\tEtiqueta = " + element + " : " + str(noticia_y_etiqueta[i]["etiquetas"][element]))

elementos_unicos_manual = set(list_etiqueta_manual)
elementos_unicos_clasificador = set(list_etiqueta_clasificador)

diccionario_etiquetas_apariciones = {}

escribeLinea("Resultados: ")
escribeLinea("\tApariciones de etiquetas (de forma manual) en las " + str(len(list_etiqueta_manual)) + " noticias:")
for elemento in elementos_unicos_manual:
    escribeLinea("\t\t" + elemento + " : " + str(list_etiqueta_manual.count(elemento) / len(list_etiqueta_manual)))
escribeLinea(
    "Apariciones de etiquetas (dadas por el clasificador) en las " + str(len(list_etiqueta_manual)) + " noticias:")

for elemento in elementos_unicos_clasificador:
    apariciones = list_etiqueta_clasificador.count(elemento)
    diccionario_etiquetas_apariciones[elemento] = apariciones
    escribeLinea("\t\t" + elemento + " : " + str(apariciones / len(list_etiqueta_manual)))

escribeLinea("\tAciertos del clasificador: ")
aciertos = 0
diccionario_aciertos = {elemento: 0 for elemento in elementos_unicos_clasificador}
for i in range(len(list_etiqueta_manual)):
    if list_etiqueta_manual[i] == list_etiqueta_clasificador[i]:
        aciertos += 1
        diccionario_aciertos[list_etiqueta_clasificador[i]] = diccionario_aciertos[list_etiqueta_clasificador[i]] + 1
    else:
        diccionario_aciertos[list_etiqueta_clasificador[i]] = diccionario_aciertos[list_etiqueta_clasificador[i]] - 1

escribeLinea("\tResultados totales, porcentaje de acierto = " + str(aciertos / (len(list_etiqueta_manual))) + ", "
                                                                                                              "precisión del modelo dado utilizando el conjunto de testeo = 0.9686558167570826")
for element in elementos_unicos_clasificador:
    if diccionario_aciertos[element] <= 0:
        escribeLinea("\t\tPorcentaje de acierto de la etiqueta: " + element + " : 0")
    else:
        escribeLinea("\t\tPorcentaje de acierto de la etiqueta " + element + " : " + str(
            round(diccionario_aciertos[element] / diccionario_etiquetas_apariciones[element], 2)))

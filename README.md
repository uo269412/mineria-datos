# Ejercicio de minería de datos

<h3>Instalación para ejecutar el programa </h3>
<p>Se necesitará un intérprete de Python para poder ejecutar el programa. El utilizado ha sido Pycharm Community 2022.2.2 (aunque debería valer una versión más actual de este), descargado en el enlace oficial de descargas de Pycharm, <a href="https://www.jetbrains.com/pycharm/download/#section=windows">Enlace de descarga oficial de Pycharm</a>.</p>
<p>También necesitaremos una versión de Python. En este caso utilizaremos la versión 3.10, que se puede encontrar en <a href="https://www.python.org/downloads/release/python-3100/">Enlace de descarga oficial de Python 3.10</a>. Se recomienda descargar el Windows x86-64-web-based installer y proceder con las instrucciones para la instalación.</p>



<h3>Configuración necesaria para la ejecución del programa</h3>

<h4>Instalación de recursos</h4>
<p>Si se quiere replicar la creación del entorno de desarrollo utilizado para la ejecución de este programa, se debe tener en cuenta de que se han instalado librerías adicionales para así poder utilizarlas en el programa.</p>


<p>Si queremos replicar exactamente el mismo entorno que creé yo para la ejecución del programa, deberemos seguir estos pasos:</p>
<ol>
  <li>Crear un nuevo proyecto en Pycharm utilizando la opción New Proyect.</li>
  <li>Seleccionaremos la opción para crear un nuevo environment que utilice Virtualenv. Tendremos que asegurarnos de que el Base interpreter que utilizará sea el de la instalación de Python 3.9. Si no hemos cambiado nada de la ruta en la instalación, se encontrará en C:\Users\usuario\AppData\Local\Programs\Python\Python310</li>
  <li>Confirmaremos la creación del proyecto.</li>
  <li>Entramos en la terminal, y accederemos a la carpeta Scripts donde tendremos scripts que nos ayudarán con la instalación. La ruta debería ser nombre_proyecto/venv/Scripts.</li>
  <li>Ejecutamos los siguientes comandos:
    <ul>
      <li><i>pip install spacy</i></li>
      <li><i>pip install textacy</i></li>
      <li><i>pip install simhash</i></li>
      <li><i>python -m spacy download es_core_news_sm</i></li>
      <li><i>pip install fasttext-wheel</i></li>
    </ul>
  </li>
</ol>

<h4>Descarga de recursos</h4>
<p>En el proyecto ya se incluyen los archivos que utilizará el programa. Independientemente, aquí se muestra el enlace de los dos archivos que usará el programa. Se tendrán que descomprimir y dejar en la raíz del proyecto el archivo que incluye las noticias con las que se trabajará: </p>

<h3>Estructura del proyecto</h3>
<p>En la estructura del proyecto podremos encontrar diferentes carpetas y ejecutables</p>
<ul>
  <li><a href = "https://github.com/uo269412/mineria-datos/tree/main/datos_adicionales">Carpeta datos_adicionales</a>: Contiene datos que genera el programa y que se utilizan para procesar ciertas operaciones. Dentro de esta carpeta se puede diferenciar carpetas con archivos que se generan utilizando escritores de texto, con los datos que se guardan utilizando Pickle
  <ul>
  <li><a href = "https://github.com/uo269412/mineria-datos/tree/main/datos_adicionales/apartado4">Carpeta apartado4</a>: Contiene los ficheros que se generan en <a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado4-5.py">apartado4-5.py</a>. Estos se corresponden con dos ficheros.txt; <a href = "https://github.com/uo269412/mineria-datos/blob/main/datos_adicionales/apartado4/conjunto-entrenamiento.txt">conjunto-entrenamiento.txt</a> que será el que contendrá los segmentos etiquetas que se utilizarán para entrenar el modelo, y <a href = "https://github.com/uo269412/mineria-datos/blob/main/datos_adicionales/apartado4/conjunto-testeo.txt">conjunto-testeo.txt</a> que contendrá los segmentos etiquetados con los que se probará el modelo.</li>
  
  <li><a href = "https://github.com/uo269412/mineria-datos/tree/main/datos_adicionales/apartado8">Carpeta apartado8</a>: Contiene el fichero ndjson que se genera en <a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado8-d_e-clasificador.py">apartado8-d_e-clasificador.py</a>. Este fichero contendrá línea por línea un objeto que contendrá la noticia, junto a las etiquetas que el modelo le ha asignado y el porcentaje de segmentos que se tienen esa etiqueta en esa noticia. El archivo generado es el siguiente: <a href = "https://github.com/uo269412/mineria-datos/blob/main/datos_adicionales/apartado8/lista-labels.noticias.ndjson">lista-labels.noticias.ndjson</a>.</li>
    
  <li><a href = "https://github.com/uo269412/mineria-datos/tree/main/datos_adicionales/pickle">Carpeta pickle</a>: Aquí se contienen varias carpetas (llamadas por el nombre del .py que las genera, junto a archivos .pickle que generan estas, y así poder cargar aquellos archivos que sean necesarios en sucesivos programas. Así también, podemos guardar algunas cosas que pueden variar dependiendo de la ejecución, como por ejemplo los resultados del clustering o lo del modelo, para así poder tener fijos los datos y seguir trabajando con ellos.</li>
  </ul>  
  </li>
   
  <li>Archivos ejecutables .py llamados apartadoX: Estos archivos contienen el código para ejecutar cierta funcionalidad que se pide en el apartado del enunciado, así teniendo como nombre el apartado al que se corresponde dentro del enunciado. Esto también supone que los programas deberían ejecutarse dentro de cierto orden ya que en cada apartado se van a ir procesando ciertos datos que requerirá el siguiente programa .py. También cabe mencionar que debido a la naturaleza del ejercicio y la introducción de, por ejemplo, etiquetas manuales y componentes aleatorios, si se ejecutan algunos de estos archivos otra vez, el resultado va a cambiar. Esto ocurre a partir de la ejecución de <a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado4-5.py">apartado4-5.py</a> y en adelante. Dentro de cada archivo, se pueden observar algunos comentarios que definen un poco alguna decisión que se ha tomado a nivel de implementación, pero a grandes rasgos estos archivos buscan conseguir la siguiente funcionalidad:
    <ul>
      <li><a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado1.py">apartado1.py</a>: El objetivo de este programa es cargar las noticias no negacionistas en memoria para así eliminar los documentos cuasi-duplicados; así correspondiéndose con el punto 1. del enunciado</li>
      <li><a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado2-a_b-spacy.py">apartado2-a_b-spacy.py</a>: En este programa segmentaremos las noticias utilizando spaCy, y luego las uniremos utilizando un doble salto de línea; así correspondiéndose con los puntos 2.a. y 2.b. del enunciado.</li>      
      <li><a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado2-c-tt.py">apartado2-c-tt.py</a>: Habiendo obtenido las sentencias, se procederá a utilizar TextTiling para obtener segmentos coherentes y se añadirán a una lista única, evitando que haya segmentos repetidos; así correspondiéndose con los puntos 2.c. y 2.d. del enunciado.</li>      
      <li><a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado3.py">apartado3.py</a>: En este programa realizamos clustering de los segmentos previamente obtenidos, utilizando k-means, buscando la generación de 25 clústeres; así correspondiéndose con el punto 3. del enunciado.<br><b><ins>Si ejecutamos este programa, los resultados van a variar, ya que se seleccionarán clústeres diferentes a aquellos que escogí, por lo que hay que tenerlo en cuenta. Los clústeres que escogí y su información está guardada en un archivo .pickle, por lo que no es necesaria su ejecución.</ins></b></li>   
      <li><a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado4-5.py">apartado4-5.py</a>: Habiendo obtenido los clústeres y analizando los segmentos obtenidos, decidimos coger 10 clústeres que parecen relevantes y les asignamos de forma manual una etiqueta. Una vez hemos establecido la etiqueta que se pondrá al clúster, le ponemos a todos los segmentos de ese clúster esa etiqueta, siguiendo el formato <i>__label__etiqueta segmento</i>. Luego, cogemos de forma aleatoria el 80% de los segmentos obtenidos y los escribimos en un fichero <a href = "https://github.com/uo269412/mineria-datos/blob/main/datos_adicionales/apartado4/conjunto-entrenamiento.txt">conjunto-entrenamiento.txt</a> y el 20% restante los escribimos en <a href = "https://github.com/uo269412/mineria-datos/blob/main/datos_adicionales/apartado4/conjunto-testeo.txt">conjunto-testeo.txt</a>; así correspondiéndose con los puntos 4. y 5. del enunciado. <br> <b><ins>Si ejecutamos este programa, se seleccionarán diferentes segmentos como entrenamiento y como testeo. Aunque supone que los resultados no van a ser estrictamente un problema, la ejecución de este programa hará que los resultados difieran, ya que se generarán sets diferentes de conjunto de entrenamiento y conjunto de testeo.</ins></b></li>    
 <li><a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado6.py">apartado6.py</a>: Utilizando los conjuntos de entrenamiento y testeo, se procederá a entrenar el modelo y luego se le someterá a pruebas; así correspondiéndose con el punto 6. <br> <b><ins>Si ejecutamos este programa, se darán diferentes resultados como precisión, aunque en mi experiencia de haberlo ejecutado varias veces, suele estar entre los valores 0.89 y 0.91.</ins></b></li>    
  <li><a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado7.py">apartado7.py</a>: Habiendo entrenado el modelo con noticias no negacionistas, ahora procesaremos las noticias negacionistas. El objetivo de este programa es cargar las noticias negacionistas en memoria para así luego procesarlas; así correspondiéndose con el punto 7. del enunciado</li>
 <li><a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado8-a_b-spacy.py">apartado8-a_b-spacy.py</a>: En este programa segmentaremos las noticias negacionistas utilizando spaCy, y luego las uniremos utilizando un doble salto de línea, de manera similar a como se hizo con las noticias no negacionistas; así correspondiéndose con los puntos 8.a. y 8.b. del enunciado.</li> 
 <li><a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado8-c-tt.py">apartado8-c-tt.py</a>: Habiendo obtenido las sentencias, se procederá a utilizar TextTiling para obtener segmentos coherentes y se añadirán a una lista única, evitando que haya segmentos repetidos, de manera similar a como se hizo con las noticias no negacionistas; así correspondiéndose con el punto 8.c. del enunciado.</li>       
  <li><a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado8-d_e-clasificador.py">apartado8-d_e-clasificador.py</a>: Este programa volverá a realizar los pasos vistos en el <a href = "https://github.com/uo269412/mineria-datos/blob/main/apartado6.py">apartado6.py</a> (ya que el modelo no podía pasarse como .pickle, lo cual supone que va a dar resultados diferentes a lo visto en el programa mencionado), creando el modelo, entrenándolo con el conjunto de entrenamiento y testeándolo con el conjunto de testeo, y adicionalmente haremos que el modelo intente predecir las etiquetas que tienen los segmentos que hemos estado procesando durante el apartado 7 y el apartado 8, es decir, los negacionistas. Una vez se le asigna una etiqueta, se escribe línea por línea la noticia negacionista junto a las etiquetas que tienen sus segmentos, calculando el porcentaje de segmentos tienen dicha etiqueta y guardando todos estos resultados en <a href = "https://github.com/uo269412/mineria-datos/blob/main/datos_adicionales/apartado8/lista-labels.noticias.ndjson">lista-labels.noticias.ndjson</a>; así correspondiéndose con los puntos 8.d. y 8.e. del enunciado. <br> <b><ins>La ejecución de este programa hará que puedan cambiar las predicciones de etiquetas, lo que puede suponer cambios en el archivo ndjson que luego se analizará de forma manual.</ins></b></li> 
    </ul>
  </li>
</ul>

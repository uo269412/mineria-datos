# mineria-datos

<h1>Instalación para ejecutar el programa </h1>
<p>Se necesitará un intérprete de Python para poder ejecutar el programa. El utilizado ha sido Pycharm Community 2022.2.2 (aunque debería valer una versión más actual de este), descargado en el enlace oficial de descargas de Pycharm, <a href="https://www.jetbrains.com/pycharm/download/#section=windows">Enlace de descarga oficial de Pycharm</a>.</p>
<p>También necesitaremos una versión de Python. En este caso utilizaremos la versión 3.9, que se puede encontrar en <a href="https://www.python.org/downloads/release/python-3100/">Enlace de descarga oficial de Python 3.10</a>. Se recomienda descargar el Windows x86-64-web-based installer y proceder con las instrucciones para la instalación.</p>



<h3>Configuración necesaria para la ejecución del programa</h3>

<h4>Instalación de recursos</h4>
<p>Si se quiere replicar la creación del entorno de desarrollo utilizado para la ejecución de este programa, se debe tener en cuenta de que se han instalado librerías adicionales para así poder utilizarlas en el programa.</p>


<p>Si queremos replicar exactamente el mismo entorno que creé yo para la ejecución del programa, deberemos seguir estos pasos:</p>
<ol>
  <li>Crear un nuevo proyecto en Pycharm utilizando la opción New Proyect.</li>
  <li>Seleccionaremos la opción para crear un nuevo environment que utilice Virtualenv. Tendremos que asegurarnos de que el Base interpreter que utilizará sea el de la instalación de Python 3.9. Si no hemos cambiado nada de la ruta en la instalación, se encontrará en C:\Users\usuario\AppData\Local\Programs\Python\Python39</li>
  <li>Confirmaremos la creación del proyecto.</li>
  <li>Entramos en la terminal, y accederemos a la carpeta Scripts donde tendremos scripts que nos ayudarán con la instalación. La ruta debería ser nombre_proyecto/venv/Scripts.</li>
  <li>Ejecutamos los siguientes comandos:
    <ul>
      <li>pip install spacy</li>
      <li>pip install textacy</li>
      <li>pip install simhash</li>
      <li>python -m spacy download es_core_news_sm</li>
    </ul>
  </li>
</ol>

<h4>Descarga de recursos</h4>
<p>En el proyecto ya se incluyen los archivos que utilizará el programa. Independientemente, aquí se muestra el enlace de los dos archivos que usará el programa. Se tendrán que descomprimir y dejar en la raíz del proyecto:</p>
<ul>
  <li></li>
  <li></li>
 </ul>

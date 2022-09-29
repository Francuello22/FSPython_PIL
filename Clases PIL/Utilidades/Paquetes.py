# Podemos importar paquetes ajenos o propios con IMPORT y FROM

# Ejemplo FROM "pandas" IMOPORT "DataFrame" para solo utilizar esa funcion del paquete
# y con as lo puedo nombrar pra usarlo IMPORT "pandas" (para traer todo el paquete) AS "pd" para renombrarlo y usar pd.dataframe

# Con el comando PIP LIST en el CMD podemos ver la lista de paquetes instalados en el entorno virtual
# ahora con esta lista, podemos hacer PIP FREEZE para hace runa "captura de pantalla" y con > la metemos en un txt llamado "requirements.txt"

# Tambien puedo instalar requirements.txt de otros proyectos. Para eso creo un nuevo entorno virtual con "python venv env", luego meto en la carpeta
# del entorno el requirements.txt del proyecto nuevo y lo instalo con "PIP INSTALL -R y el \txt"

import Funciones

Funciones.prueba2(a, b, c)

# Vamos a crear ua carpeta "UTILIDADES" para guardar nuestros propios paquetes, y con el archivo "_init_.py" python lo va a identificar

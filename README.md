# Eswindows

Lo primero que debemos tener en cuenta es instalar un par de paquetes para poder inicializar la base de datos y poder realizar las migraciones para las tablas.

Lo primero seria instalar el siguiente paquete:

Instalamos los siguientes paquetes para (MAC):

 brew install mysql-connector-c
 brew install mysql
 brew unlink mysql-connector-c
 sudo pip install pymysql
 sudo pip install mysqlclient
 NOTA: Muy importante para poder tener los paquetes adecuados si se trabajara en MACos.

 o si se trabajara en WINDOWS instalar lo siguiente:
 pip install mysqlclient


Nos dirigimos a nuestra carpeta de SETTING.PY en nuestro proyecto.
e ingresamos todo los parametros para la conexion a la BD

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eswindowsbd', #Nombre de la BD por defecto
        'USER': 'root', # Usuario
        'PASSWORD': '', # Contraseña
        'HOST': '127.0.0.1', # servidor
        'PORT': 3306, # Puerto denuestra BD
    }
}

Despues ejecutamos las migraciones:

 python manage.py migrate


y para poner en marcha el servidor:

    python manage.py runserver


Dentro se encontrara un pequeño dashboard con lo requerido, Clientes y Ordenes.



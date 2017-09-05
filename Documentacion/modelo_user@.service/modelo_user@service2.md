
# El modelo _user@.service_

_Systemd_ ofrece a los usuarios la capacidad de gestionar los servicios bajo el control del usuario con una instancia _systemd_ por usuario, permitiéndoles de este modo iniciar, detener, habilitar y deshabilitar sus propias unidades, es decir, aquellas que se encuentran dentro de ciertos directorios cuando _systemd_ se ejecuta por el usuario.

Esto es conveniente para los demonios y otros servicios que normalmente se ejecutan como un usuario diferente a _root_, como por ejemplo mpd, o para realizar tareas automatizadas como la recuperación de correo.


## ¿Cómo funciona?

Según la configuración predeterminada en _/etc/pam.d/system-login_, el módulo _pam_systemd_ inicia automáticamente una instancia `systemd --user` cuando el usuario inicia sesión por primera vez. Este proceso sobrevivirá mientras exista una sesión para ese usuario, y se matará tan pronto como se cierre la última sesión para el usuario.

Por lo tanto, la instancia `systemd --user` es un proceso por usuario y no por sesión. Esto significa que todos los servicios de usuario se ejecutan fuera de una sesión y, como consecuencia, los programas que necesiten ser ejecutados dentro de una sesión probablemente se romperán en los servicios de usuario.

Es importante saber que `systemd --user` se ejecuta como un proceso separado del proceso `systemd --system`. Las unidades de usuario no pueden referirse o depender de las unidades del sistema.

Cuando se habilita (_enabled_) el inicio automático de las instancias de usuario, la instancia se inicia en el arranque y no se eliminará. La instancia de usuario _systemd_ es responsable de administrar servicios de usuario, que pueden ser utilizados para ejecutar demonios o tareas automatizadas, con todos los beneficios de _systemd_, como activación de _socket_, temporizadores o _timers_, sistema de dependencia o control estricto de procesos a través de _cgroups_.

Las unidades de usuario se encuentran en los siguientes directorios (ordenados por precedencia ascendente):

1. _/usr/lib/systemd/user/_ donde pertenecen las unidades provistas por paquetes instalados.

2. _~/.local/share/systemd/user/_ donde pertenecen las unidades de paquetes que se han instalado en el directorio _/home/_ del usuario.

3. _/etc/systemd/user/_ donde el administrador del sistema coloca las unidades de usuario de todo el sistema (_system-wide_).

4. _~/.config/systemd/user/_ donde el usuario pone sus propias unidades.




**Cuando se inicia la instancia de usuario _systemd_, se muestra el _default.target_. Otras unidades pueden ser controladas manualmente con `systemctl --user`.**


## Configuración básica

Como he mencionado anteriormente, todos los servicios del usuario se colocarán en _~/.config/systemd/user/_. Para ejecutar servicios en el primer inicio de sesión, ejecutamos `systemctl --user enable service` para cualquier servicio que queramos iniciar de forma automática.


### Variables de entorno

La instancia de usuario de _systemd_ no hereda ninguna de las variables de entorno establecidas en lugares como _.bashrc_, etc. Hay varias maneras de establecer variables de entorno para la instancia de usuario _systemd_:

1. Para usuarios con un directorio `$HOME`, utilizamos la opción _DefaultEnvironment_ en _~/.config/systemd/user.conf_. Afecta sólo a la unidad de usuario de ese usuario.

2. Con la opción _DefaultEnvironment_ en el fichero _/etc/systemd/user.conf_. Afecta a todas las unidades de usuario.




3. Agregando un fichero de configuración _drop-in_ en _/etc/systemd/system/user@.service.d/_. Afecta a todas las unidades de usuario.



4. En cualquier momento, utilizar `systemctl --user set-environment` o `systemctl --user import-environment`. Afecta a todas las unidades de usuario iniciadas después de establecer las variables de entorno, pero no las unidades que ya estaban en ejecución.

5. Usando el comando `dbus-update-activation-environment --systemd --all` proporcionado por _dbus_. Tiene el mismo efecto que `systemctl --user import-environment`, pero también afecta a la sesión _D-Bus_. 

Después de la configuración, se puede utilizar el comando `systemctl --user show-environment` para verificar que los valores son correctos.


#### Ejemplo de servicio

Creamos el directorio _/etc/systemd/system/user@.service.d/_ y en su interior generamos un fichero llamado _local.conf_:

`[Service]`
`Environment="PATH=/usr/lib/ccache/bin:/usr/local/bin:/usr/bin:/bin"`
`Environment="EDITOR=nano -c"`
`Environment="BROWSER=firefox"`
`Environment="NO_AT_BRIDGE=1"`


COMPROVAR




#### _DISPLAY_ y _XAUTHORITY_

_DISPLAY_ es utilizado por cualquier aplicación _X_ para saber qué pantalla utilizar y _XAUTHORITY_ para proporcionar una ruta al fichero _.Xauthority_ del usuario y, por tanto, la _cookie_ necesaria para acceder al servidor _X_.

Si queremos lanzar aplicaciones _X_ desde unidades _systemd_, estas variables deben establecerse. _Systemd_ proporciona un script en _/etc/X11/xinit/xinitrc.d/50-systemd-user.sh_ para importar esas variables en la sesión de usuario _systemd_ en el lanzamiento de _X_. Por lo tanto, a menos que iniciemos _X_ de un modo no estándar, los servicios de usuario deben tener en cuenta el _DISPLAY_ y _XAUTHORITY_.

`systemctl --user import-environment DISPLAY XAUTHORITY`


#### _PATH_

Si personalizamos nuestro _PATH_ y queremos lanzar aplicaciones que lo utilizan desde unidades _systemd_, deberíamos asegurarnos de que el _PATH_ modificado está configurado en el entorno _systemd_. Suponiendo que hemos establecido el _PATH_ en _.bash\_profile_, la mejor forma para que _systemd_ tenga conocimiento del _PATH_ modificado es añadiendo lo siguiente a _~/.bash\_profile_ después de que hayamos establecido la variable _PATH_:

`systemctl --user import-environment PATH`

Esto no afectará a los servicios _systemd_ iniciados antes de que se genere _~/.bash\_profile_.


### Inicio automático de instancias de usuario _systemd_

Sabemos que la instancia de usuario _systemd_ se inicia después del primer inicio de sesión de un usuario y se cancela después de que se cierre la última sesión del usuario. A veces puede sernos útil iniciarla justo después del arranque y mantenerla ejecutándose después de cerrar la última sesión, por ejemplo para que se ejecute algún proceso de usuario sin ninguna sesión abierta. Para conseguir esto usaremos el siguiente comando:

`# loginctl enable-linger username`


## _Xorg_ y _systemd_

Hay varias formas de ejecutar _xorg_ dentro de las unidades _systemd_. A continuación hay dos opciones, ya sea iniciando una nueva sesión de usuario con un proceso _xorg_, o iniciando _xorg_ desde un servicio de usuario de _systemd_.


### Inicio de sesión automático en _Xorg_ sin gestor de pantallas




### _Xorg_ como un servicio de usuario _systemd_

El hecho de que _xorg_ se pueda ejecutar desde dentro de un servicio de usuario _systemd_ permite que otras unidades relacionadas con _X_ se puedan hacer depender de _xorg_, etc. Cabe destacar que _xorg-server_ puede ejecutarse sin privilegios pero dentro de una sesión y, con el fin de evitar esto, tendrá que acabar ejecutándose con privilegios de _root_.

A continuación, explicaré cómo lanzar _xorg_ desde un servicio de usuario:

1. Hacemos que _xorg_ funcione con privilegios de _root_ y para cualquier usuario, editando _/etc/X11/Xwrapper.config_:

`allowed_users=anybody`
`needs_root_rights=yes`

2. Añadiremos las siguientes unidades a _~/.config/systemd/user_:

 1. _~/.config/systemd/user/xorg@.socket_:

`[Unit]`
`Description=Socket for xorg at display %i`

`[Socket]`
`ListenStream=/tmp/.X11-unix/X%i`

 2. _~/.config/systemd/user/xorg@.service_:

`[Unit]`
`Description=Xorg server at display %i`

`Requires=xorg@%i.socket`
`After=xorg@%i.socket`

`[Service]`
`Type=simple`
`SuccessExitStatus=0 1`

`ExecStart=/usr/bin/Xorg :%i -nolisten tcp -noreset -verbose 2 "vt${XDG_VTNR}"`

_${XDG\_VTNR}_ es la terminal virtual donde se lanzará _xorg_. Podemos codificarla en la unidad de servicio (_hard-coded_) o configurarla en el entorno _systemd_ con el comando:

`$ systemctl --user set-environment XDG_VTNR=1`

_xorg_ debe ser lanzado en la misma terminal virtual donde el usuario ha iniciado sesión. De lo contrario, _logind_ considerará la sesión inactiva.

3. Tenemos que asegurarnos de configurar la variable de entorno _DISPLAY_.

4. A continuación, para habilitar la activación de _socket_ para _xorg_ en el _display_ 0 y _tty2_ haríamos lo siguiente:

`$ systemctl --user set-environment XDG_VTNR=2`

Para que _xorg@.service_ sepa qué terminal virtual utilizar.

` systemctl --user start xorg@0.socket`

Empezar a escuchar en el _socket_ para el _display_ 0.

Ahora ejecutar cualquier aplicación _X_ lanzará _xorg_ en la _tty2_ automáticamente.





La variable de entorno XDG_VTNR se puede establecer en el entorno systemd desde .bash_profile y, a continuación, se puede iniciar cualquier aplicación X, incluido un gestor de ventanas, como una unidad systemd que dependa de xorg@0.socket.

En la actualidad, ejecutar un gestor de ventanas como un servicio de usuario significa que se ejecuta fuera de una sesión con los problemas que esto puede traer: romper la sesión.



el módulo pam_systemd.so lanza una instancia de usuario, por defecto, en el primer inicio de sesión de un usuario, iniciando user@.service

La instancia systemd --user se ejecuta fuera de cualquier sesión de usuario. Esto está bien para correr, por ejemplo mpd, pero puede ser molesto si uno trata de iniciar un gestor de ventanas desde la instancia de usuario de systemd. Entonces polkit evita montar usb, reinicar, etc., como un usuario normal, porque el gestor de ventanas se ha ejecutado fuera de la sesión activa.

Las unidades en la instancia de usuario no heredan cualquier entorno, por lo que se debe fijar manualmente.

1. Asegúrese de que la instancia de usuario de systemd se inicia correctamente. Puede comprobar esto con:
$ systemctl --user status










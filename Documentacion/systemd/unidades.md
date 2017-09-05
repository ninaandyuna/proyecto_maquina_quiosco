
# ¿Qué son las _units_ o unidades?

_systemd_ se basa en la noción de unidades, compuestas de un nombre y una extensión que indica de qué tipo de unidad se trata. Además cada unidad tiene su correspondiente archivo de configuración cuyo nombre es idéntico.
 
Un ejemplo sería el servicio _httpd.service_ cuyo archivo de configuración sería _/usr/lib/systemd/system/httpd.service_.


## Tipos de unidades

### _.service_

Describe cómo administrar un servicio o una aplicación en el servidor. Esto incluirá cómo iniciar, detener, reiniciar o recargar el servicio, en qué circunstancias debe iniciarse automáticamente, así como información de dependencia con otras unidades.


### _.socket_

Las unidades _socket_ son IPC (_sockets UNIX_), _sockets_ de red o _FIFO_. Esta unidad se utiliza para la activación basada en _socket_, es decir, cuando el socket recibe información, ejecuta un servicio. Debe haber un servicio con el mismo nombre o especificado por la directiva _Service =_.


### _.target_

Utilizada para la agrupación lógica de unidades. Hace referencia a otras unidades, que pueden ser controladas conjuntamente. También se pueden utilizar para llevar al sistema a un nuevo estado.


### _.slice_

Consiste en un conjunto jerárquico de _units_ organizadas para manejar un grupo de procesos del sistema.


### _.mount_

Contiene información sobre un punto de montaje del sistema de archivos controlado por _systemd_.


### _.automount_

Configura un punto de montaje que se montará automáticamente. Éstos deben tener el nombre del punto de montaje al que se refieren y una unidad _.mount_ correspondiente para definir las especificaciones del montaje.


### _.device_

Contiene información de una unidad de dispositivo que requiere una gestión de _systemd_. No todos los dispositivos del sistema requieren una unidad de dispositivo _systemd_, solo aquellos marcados con la etiqueta _udev systemd_.


### _.swap_

Esta unidad describe el espacio de intercambio en el sistema.


### _.path_

Define una ruta o _path_ controlada por _systemd_. De forma predeterminada, se iniciará una unidad _.service_ del mismo nombre base que la unidad _.path_ cuando el estado de ésta cambie.


### _.timer_

Sirve para definir un temporizador que será administrado por _systemd_, similar a un trabajo _cron_ para la activación retardada o programada.


### _.snapshot_

Una unidad _.snapshot_ es creada automáticamente por el comando `systemctl snapshot`. Nos permite reconstruir el estado actual del sistema después de realizar cambios. Las instantáneas no sobreviven a través de las sesiones y se utilizan para revertir los estados temporales.


### _.scope_

Son creadas automáticamente por _systemd_ y se encargan de administrar conjuntos de procesos del sistema. Su objetivo es organizar y gestionar recursos para los procesos. A diferencia de las otras unidades, no están configuradas por ficheros de unidad.


## Las unidades de plantilla (_template_)

Los archivos de unidades de plantilla permiten que _systemd_ direccione varias unidades desde un solo archivo de configuración. Es decir:

* _getty@.service_: unidad de plantilla

* _getty@tty1.service_: instancia de la unidad de plantilla

La cadena de carácteres entre el _@_ y el sufijo de la unidad recibe el nombre de identificador de instancia. Es un argumento que se le pasa a _systemd_ para usarlo en el fichero de la unidad de plantilla. Se puede utilizar para personalizar la forma en que _systemd_ trata con esa instancia específica de la unidad, de manera que pueden existir varias instancias de la misma unidad.

Se utilizan dos identificadores en el fichero de la unidad para pasar el argumento de instancia:

* _%i_ pasa el argumento, especialmente formateado (escapado).
* _%I_ pasa el argumento literalmente sin escapar.


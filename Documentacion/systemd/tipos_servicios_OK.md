
# Tipos de servicios

Existen distintos tipos de inicio a considerar cuando se escribe un archivo de servicio personalizado. Esto se configura con el parámetro _Type=_ en la sección _[Service]_:

| Tipo | Descripcion |

| --- | --- |

| _Type=simple_ (por defecto) | _systemd_ consedira que el servicio se iniciará de inmediato. El proceso iniciado con _ExecStart=_ es el proceso principal del servicio. |


## Type=simple (por defecto)

_systemd_ consedira que el servicio se iniciará de inmediato. El proceso iniciado con _ExecStart=_ es el proceso principal del servicio.


## Type=forking

El servicio se inicia una vez que el proceso se ha bifurcado (_fork_) y el proceso padre ha salido. El proceso iniciado con _ExecStart=_ genera un proceso hijo que se convierte en el proceso principal del servicio. Debemos especificar _PIDFile=_ para que _systemd_ pueda realizar un seguimiento del proceso principal.


## Type=oneshot

Este tipo es útil para _scripts_ que realizan un solo trabajo y luego salen. Podemos configurar _RemainAfterExit=yes_ para que _systemd_ todavía considere el servicio como activo después de que el proceso haya salido.


## Type=notify

Idéntico a _Type=simple_. En este caso, el _daemon_ enviará una señal a _systemd_ cuando esté listo, es decir, cuando haya terminado de iniciarse.


## Type=dbus

El servicio se considera listo cuando el _BusName=_ especificado aparece en el bus de sistema _DBus_.


## Type=idle

_systemd_ retrasará el inicio del servicio hasta que se completen todos los trabajos. Tiene un comportamiento muy parecido al de _Type=simple_.


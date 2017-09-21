
# Análisis del arranque y apagado del sistema con _systemd_

## Inicio del sistema

En el arranque del sistema intervienen varios componentes distintos. Inmediatamente después de encender el ordenador, la _BIOS_ del sistema lleva a cabo una inicialización mínima del _hardware_. A continuación, el _boot loader_ invoca el _kernel_ del S.O. desde el disco (o la red) y, este, extrae y ejecuta una imagen de disco _RAM_ inicial (_initrd_).

Después de que el sistema de ficheros raíz se encuentra y se monta, _initrd_ entrega el control a _systemd_, almacenado en la imagen del sistema operativo, y se encarga de probar todo el _hardware_ restante, montar todos los sistemas de ficheros necesarios e iniciar todos los servicios configurados.

### Funcionamiento de _systemd_ en el arranque

![arranque_sistema](Imagenes/inicio.png "_Systemd_ en el arranque del sistema")




# Uso básico del comando _systemctl_

Es la principal orden para controlar _systemd_.


## Analizar el estado del sistema

Estado del sistema:

`$ systemctl status`

Listado de unidades activas:

`$ systemctl`
`$ systemctl list-units`





The output has the following columns:

UNIT: The systemd unit name
LOAD: Whether the unit's configuration has been parsed by systemd. The configuration of loaded units is kept in memory.
ACTIVE: A summary state about whether the unit is active. This is usually a fairly basic way to tell if the unit has started successfully or not.
SUB: This is a lower-level state that indicates more detailed information about the unit. This often varies by unit type, state, and the actual method in which the unit runs.
DESCRIPTION: A short textual description of what the unit is/does.





Listado de unidades que han tenido problemas:

`$ systemctl --failed`

Listado de todas las unidades instaladas:

`$ systemctl list-unit-files`

Los archivos de las unidades disponibles se pueden ver en _/usr/lib/systemd/system/_ y _/etc/systemd/system/_ (este último tiene prioridad). 


## Usar las unidades

Activar una unidad de inmediato:

`# systemctl start _unidad_`

Desactivar una unidad de inmediato:

`# systemctl stop _unidad_`

Reiniciar la unidad:

`# systemctl restart _unidad_`

Hacer que una unidad recargue su configuración:

`# systemctl reload _unidad_`

Mostrar el estado de una unidad, incluso si se está ejecutando o no:

`$ systemctl status _unidad_`

Comprobar si la unidad ya está habilitada o no:

`$ systemctl is-enabled _unidad_`

Activar el inicio automático en el arranque:

`# systemctl enable _unidad_`

Habilitar una unidad que se iniciará en el arranque e iniciar inmediatamente:

`# systemctl enable --now _unidad_`

Enmascarar una unidad para que sea imposible iniciarla:

`# systemctl mask _unidad_`

Desenmascarar una unidad:

`# systemctl unmask _unidad_`

Desactivar el inicio automático durante el arranque:

`# systemctl disable _unidad_`

Mostrar la página del manual asociada a una unidad:

`$ systemctl help _unidad_`

Recargar _systemd_, escaneando en busca de unidades nuevas o modificadas:

`# systemctl daemon-reload`






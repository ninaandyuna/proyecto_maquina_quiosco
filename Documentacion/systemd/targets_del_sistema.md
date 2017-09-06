
# Análisis del los _targets_ del sistema y su interrelación

_systemd_ utiliza _targets_ que sirven un propósito similar a los _runlevels_ o niveles de ejecución, pero que tienen un comportamiento un poco diferente. A cada _target_ se le asigna un nombre, en lugar de numerarse, y está destinado a servir a un propósito específico con la posibilidad de realizar más de una acción al mismo tiempo. 

Algunos de ellos son activados heredando todos los servicios de otro _target_ e implementando servicios adicionales. Como hay _targets_ de _systemd_ que imitan los _runlevels_ de _SystemVinit_, es posible pasar de un _target_ a otro utilizando la orden `# telinit _RUNLEVEL_`.



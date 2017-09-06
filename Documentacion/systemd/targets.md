
# Ajuste del estado del sistema (nivel de ejecución) con unidades _.target_

_systemd_ utiliza _targets_ que sirven un propósito similar a los _runlevels_ o niveles de ejecución, pero que tienen un comportamiento un poco diferente. A cada _target_ se le asigna un nombre, en lugar de numerarse, y está destinado a servir a un propósito específico con la posibilidad de realizar más de una acción al mismo tiempo. 

Algunos de ellos son activados heredando todos los servicios de otro _target_ e implementando servicios adicionales. Como hay _targets_ de _systemd_ que imitan los _runlevels_ de _SystemVinit_, es posible pasar de un _target_ a otro utilizando la orden `# telinit _RUNLEVEL_`.


## Tabla comparativa entre los _runlevels_ de _SysV_ y los _targets_ de _systemd_

| _Runlevel_ de _SysV_ | _Target_ de _systemd_ | _Descripción_ |
| :------------------: | --------------------- | ------------- |	
| 0 | _poweroff.target_, _runlevel0.target_ | Detiene el sistema. |
| 1, s, _single_ | _rescue.target_, _runlevel1.target_ | Modo de usuario único. |
| 2, 4 | _runlevel2.target_, _runlevel4.target_, _multi-user.target_ | Definidos por el usuario. Por defecto, idéntico a _multi-user.target_. |
| 3 | _multi-user.target_, _runlevel3.target_ | Multiusuario, no gráfica. Los usuarios, por lo general, pueden acceder a través de múltiples consolas o a través de la red. |
| 5 | _graphical.target_, _runlevel5.target_ | Multiusuario, gráfica. Es decir, _multi-user.target_ + inicio de sesión gráfica. |
| 6 | _reboot.target_, _runlevel6.target_ | Reinicia el sistema. |
| _emergency_ | _emergency.target_ | Consola de emergencia. |





















# Análisis del los _targets_ del sistema y su interrelación





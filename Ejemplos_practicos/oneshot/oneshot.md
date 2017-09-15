[Unit]
Description=Servicio que envia un e-mail al apagar el sistema
#Documentation=
Requires
Before=shutdown.target
DefaultDependencies=no

[Service]
Type=oneshot
ExecStart=/usr/bin/python /bin/enviar_email.py
RemainAfterExit=yes










--------------





[Unit]
Description=Servicio que envia un e-mail al apagar el sistema
Documentation=https://github.com/mondelob
Before=shutdown.target
DefaultDependencies=no

[Service]
ExecStart=/usr/bin/python /root/enviar_email.py
Type=oneshot
RemainAfterExit=yes

[Install]
WantedBy=shutdown.target


-----------


[Unit]
Description=runs only upon shutdown
DefaultDependencies=no
Conflicts=reboot.target
Before=shutdown.target
Requires=poweroff.target

[Service]
Type=oneshot
ExecStart=/bin/true
ExecStop=/usr/local/bin/yourscript
RemainAfterExit=yes














[Unit]
Description=Crea_fichero
Documentation=man:systemd-halt.service(8)
DefaultDependencies=no
Requires=shutdown.target umount.target final.target
After=shutdown.target umount.target final.target
Before=systemd-poweroff.service

[Service]
Type=oneshot
ExecStart=/usr/bin/crea_fichero.sh




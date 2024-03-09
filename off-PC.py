import os

shutdown = input('¿Quieres apagar el ordenador? (Si / No)')

if shutdown.lower() == 'Si':
    os.system('shutdown /s /t 3')

else:
    exit()
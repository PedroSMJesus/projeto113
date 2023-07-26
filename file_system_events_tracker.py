import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/DELL"

# Classe Gerenciadora de Eventos
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created(self, event):
        print(f"Olá, {event.src_path} foi criado")

    #2_on_deleted
    def on_deleted(self, event):
        print(f"Olá, {event.src_path} foi deletado por alguem")

    #3_on_modified
    def on_modified(self, event):
        print(f"Olá, {event.src_path} foi modificada")

    #4_on_moved
    def on_moved(self, event):
        print(f"Olá, {event.src_path} foi movida para {event.dest_path}")

        


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicie o Observer
observer.start()


#5_Escreva uma exceção para keyboardInterrupt
try:
   while True:
      time.sleep(2)
      print("executando...")
except keyboardInterrupt: 
    print("interrompido!")  
    observer.stop() 







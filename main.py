from logging import root, setLoggerClass
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy_garden.mapview import MapView, MapSource
import random
import funciones
import shutil
import os


class Box(MDBoxLayout):
    #Se crean los metodos que usen los botones
    def gen_service(self):
        # Variables de los widgets
        os.mkdir("./QRTemp")
        servicio = random.randint(10000,20000)
        p1 = "Servicio #"        
        cadena =  p1 + str(servicio)
        ruta = funciones.qrspam(cadena)        
        self.ids.service_label.text = cadena
        self.ids.qr_code.source = ruta
        shutil.rmtree("./QRTemp")
    # def  markPosition(self):
    #     pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette ="Green"
        self.theme_cls.primary_hue = "700"
        return Box()


MainApp().run()
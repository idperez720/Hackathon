from inspect import isdatadescriptor
from logging import root, setLogRecordFactory, setLoggerClass
from typing import Text
from kivy.core import camera
from kivymd.app import MDApp
from kivymd.uix import dialog
from kivymd.uix import button
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy_garden.mapview import MapView, MapSource
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
import random
import funciones
import shutil
import os
from kivymd.theming import ThemeManager



class Box(MDBoxLayout):
    #Se crean los metodos que usen los botones


    def take_photo(self, *args):
        print("Take it")
        self.ids.camara.export_to_png("./scanned/selfie.png")
        p = funciones.qrdecode("./scanned/selfie.png")
        codigo = p[0].data.decode('ascii')
        print(codigo)
        self.ids.codigo_servicio.text = codigo
        self.ids.screen.current = 'Formulario'      
            
class ClienteApp(MDApp):
    def callback(self, instance):
        if  instance.icon == "qrcode":
            print("Escaneando Codigo")
            self.root.ids.screen.current = 'QR'

        elif instance.icon == "taxi":
            print("Pidiendo un taxi")

    def build(self):
        self.theme_cls.primary_palette ="Green"
        self.theme_cls.primary_hue = "700"

        return Box()


ClienteApp().run()
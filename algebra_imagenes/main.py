import kivy
kivy.require('1.9.1')
from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.floatlayout import FloatLayout
from kivy.uix.listview import ListView
from kivy.uix.screenmanager import ScreenManager,Screen
# from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
import easygui
import cv2
import proc_img
import time

Builder.load_file('main.kv')
sm = ScreenManager()

operaciones = {"CuasiSuma-RGB-Clampeada":proc_img.sumar_rgb_clam,
                "CuasiSuma-YIQ-Clampeada":proc_img.sumar_YIQ_clam,
                "CuasiSuma-RGB-Promedio":proc_img.sumar_rgb_prom,
                "CuasiSuma-YIQ-Promedio":proc_img.sumar_YIQ_prom,
                "CuasiResta-RGB-Clampeada":proc_img.restar_rgb_clam,
                "CuasiResta-YIQ-Clampeada":proc_img.restar_YIQ_clam,
                "CuasiResta-RGB-Promedio":proc_img.restar_rgb_prom,
                "CuasiResta-YIQ-Promedio":proc_img.restar_YIQ_prom
                }


class ImageIn(ButtonBehavior, Image):
    """ algo """
    def click(self, img):
        path = easygui.fileopenbox(default='*.jpg', filetypes=[["*.png", "*.jpeg", "*.jpg", "Images files"]])
        if path:
            img.source = path
            img.reload()


class ButtonIn(Button):
    def click(self,img_1,img_2,operacion,root):
        print("imagen")
        img_a = cv2.imread(img_1.source,cv2.IMREAD_COLOR)
        img_b = cv2.imread(img_2.source,cv2.IMREAD_COLOR)
        img_a, img_b = proc_img.preprocesing(img_a,img_b)
        result = operaciones[operacion.text](img_a,img_b)
        cv2.imwrite("result.jpg",result)
        img_result = sm.screens[1].ids["img_result"]
        img_result.source = "./result.jpg"
        img_result.reload()
        root.manager.transition.direction = 'left'
        root.manager.current = 'result'


# Declare both screens
class Operation_view(Screen):
    pass

class Result_view(Screen):
    pass

class MyApp(App):
    """ algo """
    def build(self):
        sm.add_widget(Operation_view(name='operation'))
        sm.add_widget(Result_view(name='result'))
        return sm
        #return ListView()
        

if __name__ == '__main__':
    MyApp().run()
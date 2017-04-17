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
# from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
import easygui
import cv2
import proc_img
import time

Builder.load_file('main.kv')

class ImageIn(ButtonBehavior, Image):
    """ algo """
    def click(self, img):
        path = easygui.fileopenbox(default='*.jpg', filetypes=[["*.png", "*.jpeg", "*.jpg", "Images files"]])
        if path:
            img.source = path
            #img_result = self.parent.parent.parent.ids["img_2"]
            #img_result.source = path
            #img.source = img_name
            img.reload()
        #print(path)
        

operaciones = {"CuasiSuma-RGB-Clampeada":proc_img.sumar_rgb_clam,
                "CuasiSuma-YIQ-Clampeada":proc_img.sumar_YIQ_clam,
                "CuasiSuma-RGB-Promedio":proc_img.sumar_rgb_prom,
                "CuasiSuma-YIQ-Promedio":proc_img.sumar_YIQ_prom,
                "CuasiResta-RGB-Clampeada":proc_img.restar_rgb_clam,
                "CuasiResta-YIQ-Clampeada":proc_img.restar_YIQ_clam,
                "CuasiResta-RGB-Promedio":proc_img.restar_rgb_prom,
                "CuasiResta-YIQ-Promedio":proc_img.restar_YIQ_prom
                }



class ButtonIn(Button):
    def click(self,img_1,img_2,operacion):
        print("imagen")
        img_a = cv2.imread(img_1.source,cv2.IMREAD_COLOR)
        #img_a = cv2.cvtColor(img_a,cv2.COLOR_BGR2RGB)
        img_b = cv2.imread(img_2.source,cv2.IMREAD_COLOR)
        #img_b = cv2.cvtColor(img_b,cv2.COLOR_BGR2RGB)
        img_a, img_b = proc_img.preprocesing(img_a,img_b)
        print(operacion.text)
        result = operaciones[operacion.text](img_a,img_b)
        cv2.imwrite("result.jpg",result)

        #proc_img.sumar_rgb_clam(img_a,img_b)
        # cv2.imwrite("pepe1.jpg",proc_img.sumar_rgb_clam(img_a,img_b))
        # cv2.imwrite("pepe2.jpg",proc_img.sumar_rgb_prom(img_a,img_b))
        # cv2.imwrite("pepe3.jpg",proc_img.sumar_YIQ_clam(img_a,img_b))
        # cv2.imwrite("pepe4.jpg",proc_img.sumar_YIQ_prom(img_a,img_b))
        # cv2.imwrite("pepe2.jpg",img_b)



class MyApp(App):
    """ algo """
    def build(self):
        #return Label(text='Hello world')
        return ListView()
        #return RelativeLayout()
        #return FloatLayout()

if __name__ == '__main__':
    MyApp().run()
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
            img_result = self.parent.parent.parent.ids["img_2"]
            img_result.source = path
            #img.source = img_name
        #print(path)

class SliderIn(Slider):
    """ algo """
    def change_value(self, img_1,img_2, alpha, beta ):
        a = cv2.imread(img_1.source,cv2.IMREAD_UNCHANGED)
        b = proc_img.change_YIQ(a,alpha,beta)
        cv2.imwrite("/tmp/pepe.png",b)
        img_2.source = "/tmp/pepe.png"
        img_2.reload()
        
class ButtonIn(Button):
    def click(self, img):
        path = easygui.fileopenbox(default='*.jpg', filetypes=[["*.png", "*.jpeg", "*.jpg", "Images files"]])
        if path:
            img.source = path
            img_result = self.parent.parent.parent.ids["img_2"]
            img_result.source = path
            #img.source = img_name
        #print(path)

    def change_value(self, img_1,img_2, alpha, beta ):
        a = cv2.imread(img_1.source,cv2.IMREAD_UNCHANGED)
        b = proc_img.change_YIQ(a,alpha,beta)
        cv2.imwrite("/tmp/pepe.png",b)
        img_2.source = "/tmp/pepe.png"
        img_2.reload()



class MyApp(App):
    """ algo """
    def build(self):
        #return Label(text='Hello world')
        return ListView()
        #return RelativeLayout()
        #return FloatLayout()

if __name__ == '__main__':
    MyApp().run()
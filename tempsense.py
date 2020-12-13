import kivy
kivy.require('1.10.0')

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
#from digitalclock import DigitalClock
from kivy.animation import Animation

import serial
#import time
#import opc


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.button import Button



import RPi.GPIO as GPIO
import board
import busio as io
import adafruit_mlx90614
import time
from time import sleep

from kivy.properties import StringProperty, NumericProperty, ObjectProperty

import cv2

import pyautogui
from datetime import datetime


i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)


#while True:

#print("Ambent Temp: ", mlx.ambient_temperature)
#print("Object Temp: ", mlx.object_temperature)

#a=mlx.ambient_temperature
#b=mlx.object_temperature



class CamApp(App):

    def build(self):
        
        superBox = BoxLayout(orientation ='vertical')  
  
        HB = BoxLayout(orientation ='horizontal') 
        self.img1=Image()
        
      
        a=mlx.ambient_temperature
        b=mlx.object_temperature
        self.btn1=Button(text ='   Object temp  : ' + str(round(b,2)) ,
                      background_color =(0, 1.28, 0, 1), 
                      font_size = 32,
                      size_hint =(0.8, 1))
        
        self.btn2=Button(text = 'Organisation name ',
                      background_color =(0, 0, 1, 1), 
                      font_size = 42,
                      #pos_hint ={'center_x':.5, 'center_y':.25},
                      size_hint =(1, 0.2))
        
        HB.add_widget(self.img1,)
        HB.add_widget(self.btn1)
        
        VB = BoxLayout(orientation ='vertical',size_hint =(1, 0.3))
        
        VB.add_widget(self.btn2)
        
        superBox.add_widget(HB)  
        superBox.add_widget(VB)  
  
                             
        
        #layout = BoxLayout()
        #layout.add_widget(self.img1)
        #layout.add_widget(self.btn1)
        #layout.add_widget(self.btn2)
        #gsl = BoxLayout(orientation ='horizontal')
        #layout.add_widget(self.gsl)
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        #cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        
        #return layout
        return superBox  
    

    def update(self, dt):
        a=mlx.ambient_temperature
        b=mlx.object_temperature
        print("ambient temperature : "+ str(a))
        print("object temperature : "+str(b))
        
        c=6
        t=b+c
        f=32+9*t/5
    
       
        
        # display image from cam in opencv window
      
        #cv2.imshow("CV2 Image", frame)
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
        #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1
        
        #filename = "%s.jpg" % time.strftime("%Y-%m-%d-%H-%M-%S")

        #myScreenshot = pyautogui.screenshot()
        #myScreenshot.save(r"/home/pi/GSL/photo/screenshot %s" % filename)
        
        if f>93 :
            self.btn1.background_color =(1, 0, 0, 1)
            f

            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r"/home/pi/GSL/photo/screenshot %s" % filename)
            
        else :
            self.btn1.background_color =(0, 1.28, 0, 1)
        
        

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()



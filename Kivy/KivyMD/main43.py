# Screen Navigation --- Using Screen Manager

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


screen_helper = '''
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
              
<MenuScreen>:
    name: 'menu'

    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}   
        on_press: root.manager.current = 'profile'               
       
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}   
        on_press: root.manager.current = 'upload'    


              
<ProfileScreen>:
    name: 'profile'

    MDLabel:
        text: 'Welcome LeeAI'
        halign: 'center'    

    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}   
        on_press: root.manager.current = 'menu'    


             
<UploadScreen>:
    name: 'upload'

    MDLabel:
        text: 'Upload Docs'
        halign: 'center'    

    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}   
        on_press: root.manager.current = 'menu'    
'''


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class LeeAIApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)

        return screen


LeeAIApp().run()

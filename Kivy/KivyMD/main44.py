# Screen Navigation --- Using Screen Manager
# use helper function to navigate code

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_nav_helper import screen_helper


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

#from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window
#from kivymd.theming import ThemeManager
from kivymd.app import MDApp

Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (360, 640)

class Container(GridLayout):
    def convert(self):
        try:
            number = int(self.text_input.text)
        except Exception:
            number = 0

        self.label_hours.text = str(number * 24)
        self.label_minutes.text = str(number * 24 * 60)
        self.label_seconds.text = str(number * 24 * 60 * 60)
        self.label_m_seconds.text = str(number * 24 * 60 * 60 * 60)
        self.label_weeks.text = str('%.2f' % round(number / 7, 2))
        

class DuckyApp(MDApp):

    def __init__(self, **kwargs):
        self.title = 'Itproger'
        #self.theme_cls.theme_style = 'Light'
        #self.theme_cls.dynamic_color = True
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Container()

if __name__ == '__main__':
    DuckyApp().run()
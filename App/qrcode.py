from kivy.app import App
from kivy.lang import Builder
# from kivy_garden.zbarcam import ZBarCam
from kivymd.uix.screen import Screen
from kivy.core.window import Window

Window.size = (400, 700)



qrzbar= """
#:import ZBarCam kivy_garden.zbarcam.ZBarCam
BoxLayout:
    orientation: 'vertical'
    ZBarCam:
        id:qrcodecam
    Label:
        size_hint: None, None
        size: self.texture_size[0], 50
        text: ' '.join([str(i) for i in qrcodecam.symbols])
"""

class QrCode(App):
    def build(self):
        screen = Screen()
        qrcode = Builder.load_string(qrzbar)
        screen.add_widget(qrcode)
        return screen


QrCode().run()

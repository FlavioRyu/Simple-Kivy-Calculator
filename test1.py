from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

# class TestButton(Button):
#     pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.text = "TestButton created"
    #     self.pos = (100,100)
    #     self.size_hint = (0.5,0.5)
class GameScreen(Widget):
    pass

class TestApp(App):

    def build(self): # override build function
        # self.load_kv("test.kv")
        # return TestButton(
        #     text="TestButton created",
        #     pos=(100, 100),
        #     size=(500, 500),
        #     size_hint=(None, None)
        # )
        return GameScreen()


if __name__ == "__main__":
    TestApp().run()
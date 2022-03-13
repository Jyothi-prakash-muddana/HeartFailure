from kivy.uix.screenmanager import FadeTransition
import windowmanager
from kivy.app import App
from kivy.lang import Builder


class HearFailure(App):
    """
    inherited all the properties of App class
    in this we will create WindowManager object
    sent that object to learn

    """
    def build(self):
        """
        :return:WindowManager object
        """
        return windowmanager.WindowManager(transition=FadeTransition(duration=.5))

if __name__ == '__main__':
    """
     main namespace to star execution
     1. crating HearFailure class object
     2. calling its run function
    """
    HearFailure().run()

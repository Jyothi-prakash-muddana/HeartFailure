from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

Builder.load_string("""
#:import FormWindow formwindow
#:import FileuploadWindow fileuploadwindow
#:import WelcomeWindow welcomewindow
#:import Screen kivy.uix.screenmanager

<WindowManager>
    WelcomeScreen:
    FormScreen:
    FileUploadScreen:

<WelcomeScreen@Screen>:
    name : "WelcomeScreen"
    WelcomeWindow:

<FormScreen@Screen>:
    name:"FormScreen"
    FormWindow:

<FileUploadScreen@Screen>:
    name : "FileUploadScreen"
    FileUploadWindow:
    """)

class WindowManager(ScreenManager):
    pass
    """
    inherited all the properties of ScreenManager class
    created 3 screens in this class
    1.WelcomeScreen
        > it contains WelcomeWindow object
    2.FormScreen
        > it contains FormWindow object
    3.FileUploadScreen
        > it contains FileUploadWindow object
    This class is going to manage all screens of our applications
    """
    pass

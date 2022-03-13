from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("welcomewindow.kv")


class WelcomeWindow(Widget):
    """
    inherited all the properties of Widget class
    it contains a FloatLayout out
    inside floatlayout we have two buttons
    >File upload
        by pressing we will move to FileUploadScreen
    >prediction form
        by pressing we will move to FormScreen
    """
    def html_file_display(self):
        import webbrowser

        f = open('helloworld.html','w')

        message = """<html>
        <head></head>
        <body><p>Hello World!</p></body>
        </html>"""

        f.write(message)
        f.close()

        webbrowser.open_new_tab('https://jyothi-prakash-muddana.github.io/HeartFailure/')

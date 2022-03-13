from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_file("widgets.kv")


class MyPopup(Popup):
    """
    inherited all the properties of Popup class
    by calling open function of this class object a window gets popuped
    """
    pass


class MyLabel(Label):
    """
    inherited all the properties of Label
    additional features are added to make the label
    > bit transparent
    > rounded at left end
    """
    pass


class MyBoxLayout(BoxLayout):
    """
    inherited all the properties of BoxLayout
    additional features are added to make the boxlayout
    > bit transparent
    > rounded at right end
    """
    pass


class MyTextInput(TextInput):
    """
    inherited all the properties of TextInput
    additional features are added to
    > bit Transparent
    > text color to white
    > courser color to white
    > text alignment to center
    """
    pass


class RadioButton(CheckBox):
    """
    inherited all the properties of CheckBox
    > By grouping checkbox object they acts as RadioButton
    additional features are added
    > changing color to white
    """
    pass


class RadioLabel(Label):
    """
    inherited all the properties of Label
    mainly created to use them along with RadioButtons
    additional features are
    >Bit Transparent
    >White Text
    """
    pass

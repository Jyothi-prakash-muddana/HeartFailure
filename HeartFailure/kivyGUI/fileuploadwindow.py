from kivy.uix.widget import Widget
from kivy.uix.label import Label
import easygui
from kivy.lang import Builder
import pandas as pd
from modelLoading import ModelLoading
from widgets import MyPopup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import threading


Clock.max_iteration = 100

Builder.load_file("fileuploadwindow.kv")

class RecordLabel(Label):
    """
    inherited all the properties of the Label class
    > bit transparent
    > white font
    """
    pass


class IndexLabel(Label):
    """
    used to place index of the records and heading of the records
    > blue
    > white font
    """
    pass


class IGridLayout(GridLayout):
    """
    To arrange record values in order
    """
    pass


class IndexBoxLayout(BoxLayout):
    """
    to arrange index of the records
    """
    pass


class HeadingBoxLayout(BoxLayout):
    """
    to arrange headings of the columns in order
    """
    pass


class FileUploadWindow(Widget):
    """
    We have progress, popup as two class variables with None
    they are used while loading data into the Window
    """
    popup = None

    def choose_file(self):
        """
        1. it will ask user to choose file (.csv)
        3. generating a popup to show that data is loading
        4 . thread to load data t1 calls update_layout function which takes file as parameter
        :return: None
        """
        file = easygui.fileopenbox(default="*.csv")
        self.ids.heading.clear_widgets()
        self.ids.index.clear_widgets()
        self.ids.scroll.clear_widgets()
        if file is not None:
            self.ids.location.text = file
            self.file = file.replace('\\', '\\\\')
            #FileUploadWindow.popup = MyPopup()
            #FileUploadWindow.progress = ProgressBar(max=100)
            #FileUploadWindow.popup.content = Label(text = "Loading Data .....")
            #FileUploadWindow.popup.auto_dismiss = False
            #FileUploadWindow.popup.title = " "
            #FileUploadWindow.popup.open()
            #t1 = threading.Thread(target=self.update_layout, args=[file], name='t2')
            #t1.start()
            self.update_layout(self.file)


    def update_layout(self, file):
        """
        dataf is created using .csv file
        updating progress bar
        creating model object
        predicting values
        loading the data into 3 layouts
        1. index layout
        2. heading layout
        3. records layout
        adding widgets to scroll view
        :param file: name,location of file
        :return: None
        """
        dataf = pd.read_csv(file)
        #FileUploadWindow.popup.title = "Loading Data ...."
        #FileUploadWindow.progress.value = 10.11
        #time.sleep(0.03)
        real = dataf.pop("DEATH_EVENT")
        #FileUploadWindow.popup.title = "Creating Layout ...."
        iBox = IGridLayout()
        hBox = HeadingBoxLayout()
        inBox = IndexBoxLayout()
        hBox.add_widget(RecordLabel(text="DEATH_EVENT(p)"))

        for col in list(dataf.columns):
            hBox.add_widget(RecordLabel(text=col))
        #FileUploadWindow.progress.value = 22.61
        #FileUploadWindow.popup.title = "Loading Model ...."
        #time.sleep(0.02)
        model = ModelLoading()
        #FileUploadWindow.progress.value = 36.53
        #FileUploadWindow.popup.title = "Predicting  ...."
        #time.sleep(0.05)
        predict = model.multipleRecords(dataf[["age",
                                               "creatinine_phosphokinase",
                                               "ejection_fraction",
                                               "serum_creatinine",
                                               "time"]])
        #FileUploadWindow.progress.value = 50.53
        #FileUploadWindow.popup.title = "Displaying Data  ...."
        #time.sleep(0.03)
        for i in range(dataf.shape[0]):
            inBox.add_widget(IndexLabel(text=str(i + 1)))
            iBox.add_widget(RecordLabel(text=str(predict[i])))
            for j in dataf.columns:
                iBox.add_widget(RecordLabel(text=str(dataf[j][i])))
        #FileUploadWindow.progress.value = 80.93
        #time.sleep(0.3)
        self.ids.scroll.add_widget(iBox)
        self.ids.heading.add_widget(hBox)
        self.ids.index.add_widget(inBox)
        #FileUploadWindow.popup.dismiss()
        #FileUploadWindow.popup = None
        #FileUploadWindow.progress = None

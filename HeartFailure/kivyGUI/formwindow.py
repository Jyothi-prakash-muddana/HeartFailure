from widgets import MyPopup
from kivy.uix.widget import Widget
import pandas as pd
from modelLoading import ModelLoading
from kivy.lang import Builder

Builder.load_file("formwindow.kv")

class FormWindow(Widget):
    """
    inherited all the properties of Widgets
    contains some class variables for storing input
    > age, creatinine_phosphokinase, ejection_fraction, platelets,
      serum_creatinine, serum_sodium, time, anaemia, diabetes,
      high_blood_pressure, gender, smoking

    it contains multiple function to handle the form
    > radiobutton_anaemia : to handle radio button of anaemia
    > radiobutton_diabetes : to handle radio button of diabetes
    > radiobutton_high_blood_pressure : to handle radio button of high_blood_pressur
    > radiobutton_gender : to handle radio button of gender
    > radiobutton_smoking : to handle radio button of smoking
    > submit : to collect all details and popup result
    > reset : to clear all the inputs

    """
    age = None
    creatinine_phosphokinase = None
    ejection_fraction = None
    platelets = None
    serum_creatinine = None
    serum_sodium = None
    time = None
    anaemia = None
    diabetes = None
    high_blood_pressure = None
    gender = None
    smoking = None

    def radiobutton_anaemia(self, instance, value, text):
        """
        it will store the data to anaemia if the radio button is off None is assigned to anaemia
        :param instance: radio button object
        :param value: true/false :: on/off
        :param text: to assign value to anaemia variable
        :return: None
        """
        if value:
            FormWindow.anaemia = text
        else:
            FormWindow.anaemia = None

    def radiobutton_diabetes(self, instance, value, text):
        """
        it will store the data to diabetes if the radio button is off None is assigned to diabetes
        :param instance: radio button object
        :param value: true/false :: on/off
        :param text: to assign value to diabetes variable
        :return: None
        """
        if value:
            FormWindow.diabetes = text
        else:
            FormWindow.diabetes = None

    def radiobutton_high_blood_pressure(self, instance, value, text):
        """
        it will store the data to high blood pressure if the radio button is off None is assigned to high blood pressure
        :param instance: radio button object
        :param value: true/false :: on/off
        :param text: to assign value to high_blood_pressure variable
        :return: None
        """
        if value:
            FormWindow.high_blood_pressure = text
        else:
            FormWindow.high_blood_pressure = None

    def radiobutton_gender(self, instance, value, text):
        """
        it will store the data to gender if the radio button is off None is assigned to gender
        :param instance: radio button object
        :param value: true/false :: on/off
        :param text: to assign value to gender variable
        :return: None
        """
        if value:
            FormWindow.gender = text
        else:
            FormWindow.gender = None

    def radiobutton_smoking(self, instance, value, text):
        """
        it will store the data to smoking if the radio button is off None is assigned to smoking
        :param instance: radio button object
        :param value: true/false :: on/off
        :param text: to assign value to smoking variable
        :return: None
        """
        if value:
            FormWindow.smoking = text
        else:
            FormWindow.smoking = None

    def submit(self):
        """
        in this call we collect all the data from the form
        creates a list of it
        generate a data frame to give it as input to the model
        creating model object
        predicting output
        MyPopup class object is created
        and uses it to popup the ouput
        if any errors are occurred in middle it will generate a popup
        :return: None
        """
        FormWindow.age = self.ids.age_input.text.strip()
        FormWindow.creatinine_phosphokinase = self.ids.creatinine_phosphokinase_input.text.strip()
        FormWindow.ejection_fraction = self.ids.ejection_fraction_input.text.strip()
        FormWindow.platelets = self.ids.platelets_input.text.strip()
        FormWindow.serum_creatinine = self.ids.serum_creatinine_input.text.strip()
        FormWindow.serum_sodium = self.ids.serum_sodium_input.text.strip()
        FormWindow.time = self.ids.time_input.text.strip()
        columns = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
                   'ejection_fraction', 'high_blood_pressure', 'platelets',
                   'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time', ]
        Heading = ["age", "creatinine_phosphokinase", "ejection_fraction", "serum_creatinine", "time"]

        List = [[FormWindow.age, FormWindow.anaemia,
                 FormWindow.creatinine_phosphokinase, FormWindow.diabetes,
                 FormWindow.ejection_fraction, FormWindow.high_blood_pressure,
                 FormWindow.platelets, FormWindow.serum_creatinine,
                 FormWindow.serum_sodium, FormWindow.gender,
                 FormWindow.smoking, FormWindow.time]]

        df = pd.DataFrame(List, index=[1], columns=columns)
        pop = MyPopup()

        try:
            #age
            if not df["age"][1].isdigit():
                if FormWindow.age == '':
                    raise ValueError("Fill age")
                else:
                    raise ValueError("Age must be an integer in range 1 to 120")
            if not 0 < int(df["age"][1]) < 120:
                raise ValueError("Age must be in range 1 to 120")

            # anaemia
            if FormWindow.anaemia is None:
                raise ValueError("fill Aneaemia")

            # ceatinine_phosphokinase
            if not df["creatinine_phosphokinase"][1].isdigit():
                if FormWindow.creatinine_phosphokinase == '':
                    raise ValueError("Fill Creatinine Phosphokinase")
                else:
                    raise ValueError("Creatinine Phosphokinase must be an integer in range 20 to 7860")
            if not 20 <= int(df["creatinine_phosphokinase"][1]) < 8000:
                raise ValueError("Creatinine Phosphokinase must in range(20,8000)")

            # diabetes
            if FormWindow.diabetes is None:
                raise ValueError("fill Diabetes")

            # ejection_fraction
            if not df["ejection_fraction"][1].isdigit():
                if FormWindow.ejection_fraction == '':
                    raise ValueError("Fill Ejection Fraction")
                else:
                    raise ValueError("Ejection Fraction must be in range 10 to 100")
            if not 14 <= int(df["ejection_fraction"][1]) <= 80:
                raise ValueError("Ejection Fraction in range(14,80)")

            # hight_blood_pressure
            if FormWindow.high_blood_pressure is None:
                raise ValueError("Fill High Blood Pressure")

            # platelets
            if FormWindow.platelets == '':
                raise ValueError("Fill Platelets")
            if FormWindow.platelets.count('.') > 1:
                raise ValueError("Platelets more than one decimal points")
            elif not FormWindow.platelets.replace('.', '').isdigit():
                raise ValueError("Pleas enter valid input for Platelets")
            if not 25000 <= float(df["platelets"][1]) < 850000:
                raise ValueError("Platelets value must be in range(25000,850000)")

            # serum_creatinine
            if FormWindow.serum_creatinine == '':
                raise ValueError("Fill serum Creatinine")
            if FormWindow.serum_creatinine.count('.') > 1:
                raise ValueError("Serum Creatinine more than one decimal points")
            elif not FormWindow.serum_creatinine.replace('.', '').isdigit():
                raise ValueError("Pleas enter valid input for Serum Creatinine")
            if not 0.5 <= float(df["serum_creatinine"][1]) <= 9.5:
                raise ValueError("Serum Creatinine must be in range(.5 to 9.5)")

            # serum_sodium
            if FormWindow.serum_sodium == '':
                raise ValueError("Fill Serum Sodium")
            if FormWindow.serum_sodium.count('.') > 1:
                raise ValueError("Serum Sodium more than one decimal points")
            elif not FormWindow.serum_sodium.replace('.', '').isdigit():
                raise ValueError("Pleas enter valid input for Serum Sodium")
            if 100 < int(df["serum_sodium"][1]) <= 150:
                raise ValueError("Serum Sodium must be in range(100 to 150)")

            # gender
            if FormWindow.gender is None:
                raise ValueError("choose gender male/female ")

            # smoking
            if FormWindow.smoking is None:
                raise ValueError("Fill for smoking")

            model = ModelLoading()
            prediction = model.singleRecord(df[Heading])
            pop.title = "Prediction is Done"
            if prediction == 1:
                pop.ids.pop_output.text = "There is high chance to survive for this patient for long time"
            elif prediction == 0:
                pop.ids.pop_output.text = "There is a chance to survive with good medical care "

        except ValueError as ve:
            pop.title = " Value Error "
            pop.ids.pop_output.text = str(ve)

        except:
            pop.title = "Error"
            pop.ids.pop_output.text = " Something went wrong in prediction try again"

        finally:
            pop.open()

    def reset(self):
        """
        clears all values
        by replacing text with ""
        and replacing readiobuttons output to None, state to Normal
        :return:None
        """
        self.ids.age_input.text = ''
        self.ids.creatinine_phosphokinase_input.text = ''
        self.ids.ejection_fraction_input.text = ''
        self.ids.platelets_input.text = ''
        self.ids.serum_creatinine_input.text = ''
        self.ids.serum_sodium_input.text = ''
        self.ids.time_input.text = ''
        self.ids.anaemia_yes.state = "normal"
        self.ids.anaemia_no.state = "normal"
        self.ids.diabetes_yes.state = "normal"
        self.ids.diabetes_no.state = "normal"
        self.ids.high_blood_pressure_yes.state = "normal"
        self.ids.high_blood_pressure_no.state = "normal"
        self.ids.gender_female.state = "normal"
        self.ids.gender_male.state = "normal"
        self.ids.smoking_yes.state = "normal"
        self.ids.smoking_no.state = "normal"
        FormWindow.age = None
        FormWindow.creatinine_phosphokinase = None
        FormWindow.ejection_fraction = None
        FormWindow.platelets = None
        FormWindow.serum_creatinine = None
        FormWindow.serum_sodium = None
        FormWindow.time = None
        FormWindow.anaemia = None
        FormWindow.diabetes = None
        FormWindow.high_blood_pressure = None
        FormWindow.gender = None
        FormWindow.smoking = None

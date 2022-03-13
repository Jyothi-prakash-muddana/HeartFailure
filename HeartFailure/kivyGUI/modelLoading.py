import joblib
import sklearn.ensemble._forest
import sklearn.neighbors._typedefs
import sklearn.utils._weight_vector
import sklearn.neighbors._quad_tree

class ModelLoading:
    def __init__(self):
        """
        model is loading and creating a model object
        """
        self.model = joblib.load("MachineLearning\\Model.pkl")


    def singleRecord(self, dataf):
        """
        used to predict the output for single record
        :param dataf: input for model
        :return: predicted output
        """
        return self.model.predict(dataf)[0]

    def multipleRecords(self, dataf):
        """
        used to predict the output for more than one record
        :param dataf: input for model ( more than one record)
        :return: predicted output series is returned (list)
        """
        return self.model.predict(dataf)

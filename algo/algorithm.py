from sklearn.ensemble import RandomForestClassifier
from abc import ABCMeta, abstractmethod
import numpy as np

class classifer_struct(metaclass = ABCMeta):
    @abstractmethod
    def fit(self, traindata, labels):
        return None
    @abstractmethod
    def algopredict(self, traindata):
        proba = np.zeros((traindata.shape[0], 2))
        return proba

    def predict(self, traindata):
        algopredict = self.algopredict(traindata)
        predict = np.argmax(algopredict, axis=1)
        return predict
    def __init__():


class RF(classifer_struct):
    def __init__(self, n_estimators=10, min_weight_fraction_leaf=0.0,criterion='gini', min_samples_split=2,
                 min_samples_leaf=1,  min_impurity_split=1e-07,
                 bootstrap=True, warm_start=False,oob_score=False, max_features='auto',
                 max_leaf_nodes=None, class_weight=None,max_depth=None, ):

        self.clf = RandomForestClassifier(n_estimators=n_estimators,min_impurity_split=min_impurity_split,min_samples_leaf=min_samples_leaf,
                                          criterion=criterion, min_samples_split=min_samples_split,
                                          max_features=max_features, max_leaf_nodes=max_leaf_nodes,
                                          min_weight_fraction_leaf=min_weight_fraction_leaf,bootstrap=bootstrap,
                                          warm_start=warm_start, class_weight=class_weight,
                                          oob_score=oob_score, max_depth=max_depth)
                                          

    def fit(self, traindata, labels):
        self.clf.fit(traindata, labels)

    def algopredict(self, traindata):
        return self.clf.predict_proba(traindata)



import numpy as np
import pandas as pd
import os
from abc import ABCMeta, abstractmethod

def load(year):
    currpath = os.getcwd() + "/data/"
    fname = '{}year.csv'.format(year)
    fpath = currpath + fname
    data = pd.read_csv(fpath, na_values='?')
    Ydataset = data['class'].values
    Xdataset = data.drop('class', axis=1).values
    dex = np.random.permutation(len(Ydataset))
    Xdataset = Xdataset[dex, :]
    Ydataset  = Ydataset[dex]
    return Xdataset, Ydataset 

def split(Xset, Yset, frac):
    pt = int(len(Yset) * frac)
    return Xset[pt:, :], Yset[pt:], Xset[:pt, :], Yset[:pt]

class procdata():
    __metaclass__ = ABCMeta
    @abstractmethod
    def fit(self, data):
        raise NotImplementedError
    @abstractmethod
    def tran(self, data):
        raise NotImplementedError
    def fittran(self, data):
        self.fit(data)
        return self.tran(data)

class Imp(procdata):
    def fit(self, data):
        self.impval = np.nanmin(data, axis=0)
        self.connan = np.any(np.isnan(data), axis=0)
    def tran(self, data):
        fea = np.isnan(data)[:, self.connan]
        fea = np.atleast_2d(fea)
        data = np.copy(data)
        for i in range(len(data)):
            locnan = np.isnan(data[i])
            data[i, locnan] = self.impval[locnan]
        return np.concatenate((data, fea), axis=1)

class Proc(procdata):
    def __init__(self):
        self.sharemax = 1.0
    def fit(self, data):
        self.dropfea = np.zeros([len(data), 0])
        self.mean = np.nanmean(data, axis=0)
        self.std = np.nanstd(data, axis=0)
        if self.sharemax < 1.0:
            freqnan = np.isnan(data).sum(axis=0) / len(data)
            self.dropfea = np.where(freqnan > self.sharemax)[0]
    def tran(self, data):
        data = np.copy(data)
        data = (data - self.mean) / self.std
        if len(self.dropfea) > 0:
            data = np.delete(data, self.dropfea, axis=1)
        return data
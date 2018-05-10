import numpy as np
import os
import pandas as pd
import pickle
from supportfunc import load,split,Proc,Imp

def predict_algo(inputdata,year_data):
	proc = pickle.load(open("./model/{}_proc".format(year_data),"rb"))
	imp = pickle.load(open("./model/{}_imp".format(year_data),"rb"))
	model = pickle.load(open("./model/{}_algo".format(year_data),"rb"))
	X = proc.tran(inputdata)
	X = imp.tran(X)
	pred_proba = model.predict_proba(X)
	pred = np.argmax(pred_proba, axis=1)
	return pred

with open("/Users/Lwmformula/Desktop/testdata.pkl","rb") as f:
	dataset = pickle.load(f)
	testX = [dataset["2017"]]
	print (predict_algo(testX,"1"))

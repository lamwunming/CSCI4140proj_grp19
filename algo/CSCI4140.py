import numpy as np
import os
import pandas as pd
import sys
import pickle
import datetime
from supportfunc import load,split,Proc,Imp
from grabratiodata import grabratio

def predict_algo(inputdata,year_data):
	proc = pickle.load(open("./model/{}_proc".format(year_data),"rb"))
	imp = pickle.load(open("./model/{}_imp".format(year_data),"rb"))
	model = pickle.load(open("./model/{}_algo".format(year_data),"rb"))
	X = proc.tran(inputdata)
	X = imp.tran(X)
	pred_proba = model.algopredict(X)
	#pred = np.argmax(pred_proba, axis=1)
	return pred_proba 

def grabnpred(inputcode):
	if len(str(inputcode)) <= 4: stockcode = str(inputcode).zfill(4)
	else: stockcode = (inputcode.strip("0")).zfill(4)
	datainput = grabratio(stockcode)
	result = []
	for key in datainput:
		yearalgo = int(datetime.datetime.now().year) - int(key)
		if yearalgo > 5: continue
		inputX = [datainput[key]]
		result.append(predict_algo(inputX,str(yearalgo))[0])
	return result


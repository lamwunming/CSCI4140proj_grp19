from sklearn import metrics as mets
from algorithm import RF
from supportfunc import load,split,Proc,Imp
import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

def display(accinfo, yr, result_metric=[]):
    if (len(result_metric) > 0):
        print('\naccinfo for yr {}:'.format(yr))
        for metric in result_metric:
            if type(accinfo[metric]) == dict:
                print('{}={:.2f}, std={:.2f}'.format(metric,
                    accinfo[metric]['mean'], accinfo[metric]['std']))
            elif type(accinfo[metric]) == str:
                print(accinfo[metric])
            elif isinstance(accinfo[metric], float):
                print('{}={:.2f}'.format(metric, accinfo[metric]))
            else:
                print('{} cannot be printed.'.format(metric))

    plt.figure(yr)
    plt.title('roc curve yr {}'.format(yr))
    plt.plot((0, 1), (0, 1), ls='--', c='k')
    if type(accinfo['roc_curve']['fpr']) == list:
        for fpr, tpr in zip(accinfo['roc_curve']['fpr'],accinfo['roc_curve']['tpr']):
            plt.plot(fpr, tpr)
    else:
        plt.plot(accinfo['roc_curve']['fpr'], accinfo['roc_curve']['tpr'])
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')

def trainfunc(yr):
    tmpX, tmpY = load(yr)
    trainX, trainY, testX, testY = split(tmpX, tmpY,0.1)
    accinfo,algo,proc,imp = trainrun(trainX, trainY, testX, testY)
    with open(os.getcwd() + "/model/{}_algo".format(str(yr)),"wb") as f:
    	pickle.dump(algo,f)
    with open(os.getcwd() + "/model/{}_proc".format(str(yr)),"wb") as f:
        pickle.dump(proc,f)
    with open(os.getcwd() + "/model/{}_imp".format(str(yr)),"wb") as f:
        pickle.dump(imp,f)
    display(accinfo, yr,result_metric=['classification_report', 'log_loss', 'accuracy', 'roc_auc'])

def trainrun(trainX, trainY, testX, testY):
    process = Proc()
    trainX = process.fittran(trainX)
    testX = process.tran(testX)
    imp = Imp()
    trainX = imp.fittran(trainX)
    testX = imp.tran(testX)
    parameters = {"n_estimators": 100, "min_samples_split": 2,"min_samples_leaf": 1,"min_weight_fraction_leaf": 0.0,
    			  "warm_start": False,"criterion": 'entropy',"bootstrap": False,"oob_score": False,"max_features": 'auto',
    			  "max_depth": None,"max_leaf_nodes": None,"class_weight": None }

    RFalgo = RF(**parameters)

    accinfo = dict()
    accinfo['fit_info'] = RFalgo.fit(trainX, trainY)
    predresult = RFalgo.algopredict(testX)
    pred = np.argmax(predresult, axis=1)
    accinfo['log_loss'] = mets.log_loss(testY, predresult[:, 1])
    accinfo['accuracy'] = mets.accuracy_score(testY, pred)
    accinfo['recall'] = mets.recall_score(testY, pred, labels=[0, 1])
    accinfo['precision'] = mets.precision_score(testY, pred, labels=[0, 1])
    fpr, tpr, thresholds = mets.roc_curve(testY, predresult[:, 1])
    accinfo['roc_curve'] = {'fpr': fpr, 'tpr': tpr, 'thresholds': thresholds}
    accinfo['roc_auc'] = mets.auc(fpr, tpr)
    accinfo['classification_report'] = mets.classification_report(testY,pred, labels=[0, 1])
    return accinfo,RFalgo,process,imp


if __name__ == '__main__':
	np.random.seed(52)
	for yr in [1,2,3,4,5]:
		trainfunc(yr)
	plt.show()

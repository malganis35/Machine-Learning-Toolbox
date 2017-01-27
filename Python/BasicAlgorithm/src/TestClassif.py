'''
Created on 17 janv. 2017

@author: SC
'''

#if __name__ == '__main__':

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import numpy as np
import csv

i = 1

fileName = "..\..\..\data\Classification\iris\iris.data"



flowerData =  np.loadtxt(fname = fileName, delimiter = ',', dtype ={'names': ('x1', 'x2', 'x3', 'x4', 'Class'), 
                                                                  'formats': (np.float64, np.float64, np.float64, np.float64, 'S30')})

print(type(flowerData))
print(flowerData.shape[0])


nbFeats = 4

flowerDataMat = []
flowerDataLabel = []
for flower in flowerData:
        flowerDataMat.append(list(flower)[0:nbFeats])
        flowerDataLabel.append(list(flower)[4])

        
flowerDataMat = np.array(flowerDataMat).reshape([flowerData.shape[0], nbFeats])


def flower_to_class (argument):
        switcher = {
            b'Iris-setosa': 0,
            b'Iris-versicolor': 1,
            b'Iris-virginica': 2,
        }
        return switcher.get(argument, -1)

flowerDataLabelNum = []
for label in flowerDataLabel:
        flowerDataLabelNum.append(flower_to_class(label))



X_train, X_test, y_train, y_test = train_test_split(flowerDataMat, flowerDataLabelNum, test_size=.3, random_state=0)

print(y_test)

# Preprocessing
sc = StandardScaler()
sc.fit(X_train)

X_train_scaled = sc.transform(X_train)
X_test_scaled = sc.transform(X_test)


svm = SVC(C=20, cache_size=200, class_weight='balanced', coef0=0.0,
decision_function_shape='ovr', degree=3, gamma=20, kernel='rbf',
max_iter=-1, probability=False, random_state=None, shrinking=False,
tol=0.001, verbose=False)

svm.fit(X_train_scaled, y_train)
    

print('Accuracy on training set is {:.2f}'.format(svm.score(X_train_scaled, y_train)))
print('Accuracy on test set is {:.2f}'.format(svm.score(X_test_scaled, y_test)))


knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
knn.fit(X_train_scaled, y_train)

print('Accuracy of the knn classifier is {:.2f} on training data'.format(knn.score(X_train_scaled, y_train)))
print('Accuracy of the knn classifier is {:.2f} on test data'.format(knn.score(X_test_scaled, y_test)))
        
y_pred=knn.predict(X_test_scaled)    
print(metrics.confusion_matrix(y_test,y_pred))    
        
        
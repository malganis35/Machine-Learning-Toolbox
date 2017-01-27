'''
Created on 17 janv. 2017

@author: SC
'''

if __name__ == '__main__':
    
    # Import library
    print("Import libraries")
    from sklearn.svm import SVC
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.cross_validation import train_test_split
    import numpy as np
    import csv
    
    i = 1
    
    fileName = "..\..\..\data\Classification\iris\iris.data"
    print("Loading the file:", fileName)
    #flowerData = csv.reader(open(fileName, 'r'), delimiter=',', quotechar='|')
    #for row in flowerData:
    #    print(' '.join(row))
    #    i = i + 1
    #    if i == 5:
    #
    a = 1;
    a = a +1;
    a = a+2;
    flowerData =  np.loadtxt(fname = fileName, delimiter = ',', dtype ={'names': ('x1', 'x2', 'x3', 'x4', 'Class'), 
                                                                  'formats': (np.float64, np.float64, np.float64, np.float64, 'S30')})
    
    print("Display some informations about the dataset")
    print(type(flowerData))         # Print the type of flowerData
    print(flowerData.shape[0])      # Print the size of flowerData
    # print(flowerData)
    # print(flowerData[3])

    nbFeats = 4
    
    flowerDataMat = []
    flowerDataLabel = []
    for flower in flowerData:
        flowerDataMat.append(list(flower)[0:nbFeats])
        flowerDataLabel.append(list(flower)[4])
        
    flowerDataMat = np.array(flowerDataMat).reshape([nbFeats,flowerData.shape[0]]).T
    
    
    print("Convert the class label (strings) to numbers")
    #print(flowerDataLabel)
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
    
    print("Split the dataset into train and test sets")
    X_train, X_test, y_train, y_test = train_test_split(flowerDataMat, flowerDataLabelNum, test_size=.3, random_state=0)
    
    # Preprocessing
    print("Pre-processing of the data")
    sc = StandardScaler()
    sc.fit(X_train)
    
    X_train_scaled  = sc.transform(X_train)
    X_test_scaled   = sc.transform(X_test)
    
    
    #svm = SVC(kernel='rbf', random_state=0, gamma=10.10, C=50.0)
    print("Learn a SVM model")
    svm     = SVC(C=20, cache_size=200, class_weight='balanced', coef0=0.0,
                  decision_function_shape=None, degree=3, gamma=20, kernel='rbf',
                  max_iter=-1, probability=False, random_state=None, shrinking=False,
                  tol=0.001, verbose=False)
    
    svm.fit(X_train_scaled, y_train)
     

    
    #predMat = clf.predict(flowerDataMat)
    
    #print( (predMat == flowerDataLabelNum).sum()/np.array(flowerDataLabelNum).sum())
  
    print('- Accuracy on training set is {:.2f}'.format(svm.score(X_train_scaled, y_train)))
    print('- Accuracy on test set is {:.2f}'.format(svm.score(X_test_scaled, y_test)))
    
    
    print("Apply a kNN model")
    knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
    knn.fit(X_train_scaled, y_train)

    print('- Accuracy of the knn classifier is {:.2f} out of 1 on training data'.format(knn.score(X_train_scaled, y_train)))
    print('- Accuracy of the knn classifier is {:.2f} out of 1 on test data'.format(knn.score(X_test_scaled, y_test)))
        
    print("End")    
        
        
        
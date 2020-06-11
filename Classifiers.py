from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import time


def MLP(trainingData, trainingLabels, testData, testLabels):
    mlp = MLPClassifier(early_stopping=True, learning_rate_init=0.01)

    start = time.clock()
    mlp.fit(trainingData, trainingLabels)
    timer = time.clock() - start

    print("MLP Accuracy: ", mlp.score(testData, testLabels))
    print("MLP Time: ", timer)


def SVM(trainingData, trainingLabels, testData, testLabels):
    svm = SVC(kernel='linear')

    start = time.clock()
    svm.fit(trainingData, trainingLabels)
    timer = time.clock() - start

    predictions = svm.predict(testData)

    print("SVM Accuracy: ", metrics.accuracy_score(testLabels, predictions))
    print("SVM Time: ", timer)


def RF(trainingData, trainingLabels, testData, testLabels):
    rf = RandomForestClassifier(100)

    start = time.clock()
    rf.fit(trainingData, trainingLabels)
    timer = time.clock() - start

    predictions = rf.predict(testData)

    print("Random Forest Accuracy: ", metrics.accuracy_score(testLabels, predictions))
    print("Random Forest Time: ", timer)


def radialBF(trainingData, trainingLabels, testData, testLabels):
    rbf = SVC(kernel='rbf')

    start = time.clock()
    rbf.fit(trainingData, trainingLabels)
    timer = time.clock() - start

    predictions = rbf.predict(testData)

    print("RBF Accuracy: ", metrics.accuracy_score(testLabels, predictions))
    print("RBF Time: ", timer)

from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics



def MLP(trainingData, trainingLabels, testData, testLabels):
    mlp = MLPClassifier()
    mlp.fit(trainingData, trainingLabels)

    print(mlp.score(testData, testLabels))


def SVM(trainingData, trainingLabels, testData, testLabels):
    svm = SVC(kernel='linear')

    svm.fit(trainingData, trainingLabels)
    predictions = svm.predict(testData)

    print("Accuracy: ", metrics.accuracy_score(testLabels, predictions))


def RF(trainingData, trainingLabels, testData, testLabels):
    rf = RandomForestClassifier(100)

    rf.fit(trainingData, trainingLabels)

    predictions = rf.predict(testData)
    print("Accuracy: ", metrics.accuracy_score(testLabels, predictions))

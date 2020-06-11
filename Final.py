import Data
import Classifiers


samples = 5000
noise = 25

trainingData, trainingLabels, testData, testLabels = Data.createData(samples, noise)

Classifiers.MLP(trainingData, trainingLabels, testData, testLabels)

Classifiers.radialBF(trainingData, trainingLabels, testData, testLabels)

Classifiers.SVM(trainingData, trainingLabels, testData, testLabels)

Classifiers.RF(trainingData, trainingLabels, testData, testLabels)

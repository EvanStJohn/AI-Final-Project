import Data
import Classifiers



samples = 1000
noise = 5

trainingData, trainingLabels, testData, testLabels = Data.createData(samples, noise)

Classifiers.SVM(trainingData, trainingLabels, testData, testLabels)

# Forest.run(trainingData, trainingLabels, testData, testLabels)

# SVM.run(trainingData, trainingLabels, testData, testLabels)

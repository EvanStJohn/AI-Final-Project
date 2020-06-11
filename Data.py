import random
import csv

characters = []
# A
characters.append([0, 0, 1, 1, 1, 0, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 1, 1, 1, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0])
# B
characters.append([0, 1, 1, 1, 1, 0, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 1, 1, 1, 0, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 1, 1, 1, 0, 0])
# C
characters.append([0, 0, 1, 1, 1, 0, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 0, 1, 1, 1, 0, 0])
# D
characters.append([0, 1, 1, 1, 1, 0, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 1, 1, 1, 0, 0])
# E
characters.append([0, 1, 1, 1, 1, 1, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 1, 1, 1, 0, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 1, 1, 1, 1, 0])
# F
characters.append([0, 1, 1, 1, 1, 1, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 1, 1, 1, 0, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0])
# G
characters.append([0, 0, 1, 1, 1, 0, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 1, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 0, 1, 1, 1, 0, 0])
# H
characters.append([0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 1, 1, 1, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 0, 1, 0])
# I
characters.append([0, 0, 1, 1, 1, 0, 0,
                   0, 0, 0, 1, 0, 0, 0,
                   0, 0, 0, 1, 0, 0, 0,
                   0, 0, 0, 1, 0, 0, 0,
                   0, 0, 0, 1, 0, 0, 0,
                   0, 0, 0, 1, 0, 0, 0,
                   0, 0, 1, 1, 1, 0, 0])
# J
characters.append([0, 0, 0, 1, 1, 1, 0,
                   0, 0, 0, 0, 1, 0, 0,
                   0, 0, 0, 0, 1, 0, 0,
                   0, 0, 0, 0, 1, 0, 0,
                   0, 0, 0, 0, 1, 0, 0,
                   0, 1, 0, 0, 1, 0, 0,
                   0, 0, 1, 1, 0, 0, 0])

labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def flipBit(bit):
    if bit == 0:
        return 1
    else:
        return 0


def createNoise(letter, noise):
    for i in range(noise):
        index = random.randint(0, len(letter) - 1)
        letter[index] = flipBit(letter[index])
    return letter


def createData(samples, noise, letters=characters, values=labels):
    trainingAmount = int((samples + 1) * 0.6) - 1
    trainingData = []
    trainingLabels = []
    testAmount = int((samples + 1) * 0.4)
    testData = []
    testLabels = []

    for i in range(len(letters)):
        trainingData.append(letters[i][:])
        trainingLabels.append(values[i])
        for j in range(trainingAmount):
            trainingData.append(createNoise(letters[i][:], noise))
            trainingLabels.append(values[i])
        for j in range(testAmount):
            testData.append(createNoise(letters[i][:], noise))
            testLabels.append(values[i])
    return trainingData, trainingLabels, testData, testLabels

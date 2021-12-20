import os
import string

    #  The main aim of this file is to create a directory of dataset
    #  The dataset directory will contain : Training Data and Testing  Data Folders
    
datasetFolder = "dataset"
trainingDataFolder = "Training Data"
testingDataFolder = "Testing Data"

if not os.path.exists(datasetFolder):
    os.makedirs(datasetFolder)

if not os.path.exists(datasetFolder + "/" + trainingDataFolder):
    os.makedirs(datasetFolder + "/" + trainingDataFolder)

if not os.path.exists(datasetFolder + "/" + trainingDataFolder):
    os.makedirs(datasetFolder + "/" + testingDataFolder)
    

    #  Now creating the folders which contain testing and training data for every character
    #  We will do this in both: Trainng Dataset and Testing Dataset Folder

for charcater in string.ascii_uppercase:
    if not os.path.exists(datasetFolder + "/" + trainingDataFolder + "/" + charcater):
        os.makedirs(datasetFolder + "/" + trainingDataFolder + "/" + charcater)
    
    if not os.path.exists(datasetFolder + "/" + testingDataFolder + "/" + charcater):
        os.makedirs(datasetFolder + "/" + testingDataFolder + "/" + charcater)

print('\n\nDataset Folder Created Successfully !!')
print('Training Dataset Folder Created Successfully !!')
print('Tresting Dataset Folder Created Successfully !!')
print('Created Folders to store Data for characters like A, B, C, D, ........')

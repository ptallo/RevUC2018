from watson import twitterWatsonWrapper
from tensorflow import tensorFlowDataHandler

def main():
    trainDataSet = [] #list of songs lyrics
    trainDataSetLabels = [] #list of song genre's index into train data set should reference the same song

    watsonObject = twitterWatsonWrapper.WatsonAPIObject(trainDataSet)
    watsonObject.populateReturnData()
    watsonObject.populateDataSet()

    tensorFlowAPIObject = tensorFlowDataHandler.tensorFlowAPIObject(trainDataSet, len(watsonObject.dataSet.keys()))
    tensorFlowAPIObject.train(trainDataSet, trainDataSetLabels, 1000, 1000)

if __name__ == "main":
    main()
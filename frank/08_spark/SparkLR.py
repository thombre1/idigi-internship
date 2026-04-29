# Its related to some python 2.6+ version
from __future__ import print_function

from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.linalg import Vectors

if __name__ == "__main__":
    
    # Windows related spark config | create spark session
    spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("LinearRegression").getOrCreate()
    
    inputLines = spark.sparkContext.textFile("regression.txt")
    data = inputLines.map(lambda x: x.split(",")).map(lambda x: (float(x[0]), Vectors.dense(float(x[1]))))
    
    #converting 'data' RDD into dataframe
    colNames = ["label", "features"]
    df = data.toDF(colNames)
    

    #Split data into training and testing
    trainTest = df.randomSplit([0.5, 0.5])
    trainingDF = trainTest[0]
    testDF = trainTest[1]


    # This is custom linear regression model, not sop custom
    lir = LinearRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

    model = lir.fit(trainingDF)
    
    fullPredictions = model.transform(testDF).cache()

    predictions = fullPredictions.select("prediction").rdd.map(lambda x: x[0])
    labels = fullPredictions.select("label").rdd.map(lambda x: x[0])

    # collects the result from various PCs and combines them in PredictionsAndLabel
    predictionAndLabel = predictions.zip(labels).collect()
    

    # Print Preditions
    for prediction in predictionAndLabel:
        print(prediction)
    
    spark.stop()

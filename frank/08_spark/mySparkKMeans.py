from pyspark.mllib.clustering import KMeans
from numpy import array, random
from math import sqrt
from pyspark import SparkConf, SparkContext
from sklearn.preprocessing import scale

K = 5

conf = SparkConf().setMaster("local").setAppName("mySparkKMeans")
sc = SparkContext( conf = conf )

def createClusterData(N, k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    X = []
    for i in range(k):

        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])

    X = array(X)
    return X

random.seed(0)

data = sc.parallelize(scale(createClusterData(100, K)))

clusters = KMeans.train(data, K, maxIterations = 10, initializationMode = "random")

#Cache-ing the results so that we dont recompute
resultRDD = data.map(lambda point: clusters.predict(point)).cache()

print("Counts by value:")
counts = resultRDD.countByValue()
print(counts)

print("Cluster assignments: ")
results = resultRDD.collect()
print(results)



# Calculate distance from centre
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point-center)]))

#Square the distances and sum all the errors
WSSSE = data.map(lambda point: error(point)).reduce(lambda x,y : x+y)
print("Within Set Sum of Squared Error = " + str(WSSSE))


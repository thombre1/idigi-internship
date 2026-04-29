from pyspark import SparkConf, SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

conf = SparkConf().setMaster("local").setAppName("myTF-IDF")
sc = SparkContext(conf = conf)


rawData = sc.textFile("subset-small.tsv")
fields = rawData.map(lambda x: x.split("\t"))
documents = fields.map(lambda x: x[3].split(" "))

#Docnames in first column
docNames = fields.map(lambda x: x[1])

# Map words to nuumber, unqiue words wont be more than 100k
hashingTF = HashingTF(100000)
tf = hashingTF.transform(documents)


tf.cache()
idf = IDF(minDocFreq = 2).fit(tf)
tfidf = idf.transform(tf)


# map the word "gettysburg" - it does it randomly
gettysburgTF = hashingTF.transform(["Gettysburg"])

# find the index value
gettysburgHashValue = int(gettysburgTF.indices[0])


gettysburgRelevance = tfidf.map(lambda x: x[gettysburgHashValue])

zippedResults = gettysburgRelevance.zip(docNames)

print("Best document for Gettysburg is: ")
print(zippedResults.max())

from pyspark import SparkConf, SparkContext
from collections import Counter
from operator import add

conf = SparkConf().setMaster("local").setAppName("CountTemperatures")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    temperature = float(fields[3])
    return (temperature)

lines = sc.textFile("/lab07/temp.csv")
temps = lines.map(parseLine)
temps = temps.map(lambda x: (x, 1))
results = temps.reduceByKey(add).collect();

for result in results:
    print(result[0], "\t", result[1])

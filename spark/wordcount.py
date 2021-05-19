from pyspark import SparkConf, SparkContext
from collections import Counter
from operator import add

conf = SparkConf().setMaster("local").setAppName("CountWords")
sc = SparkContext(conf = conf)

words = sc.textFile("/books/pg20417.txt")
def cleaning(x):
    punc ="!@#$%^&*()_-+=|;:>.<,?/[]{}'"
    lowercased = x.lower()
    for p in punc:
        lowercased = lowercased.replace(p, "")
    return lowercased
words = words.map(cleaning)
words = words.flatMap(lambda x: x.split(" "))
words = words.filter(lambda x: x!="")
word_count = words.map(lambda x: (x, 1))
word_count = word_count.reduceByKey(lambda x,y: (x+y)).sortByKey().collect();

for word in word_count:
    print(word[0], "\t", word[1])

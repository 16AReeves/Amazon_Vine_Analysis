# Import Dependencies
from mrjob.job import MRJob

# Create a class that takes in prop from MRJob to run the full MapReduce job ### 16.2.2 (Hadoop)
class Bacon_count(MRJob):
    # next add the mapper() f(x) to assign inputs to key-value pairs
    def mapper(self, _, line): # the second parameter allows method to be mapped together, the _ tells Python we're not using that parameter. the line parameter takes the line from the file
        for word in line.split():
           if word.lower() == "bacon":
               yield "bacon", 1

    def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Bacon_count.run()

### 16.3 (Spark)

# Spark architecture: cluster manager controls drivers and executors and allocates resources to the machines on the spark apps
   # drivers (heart of app) maintains app info and responding to the code input and analyzing, distributing, and scheduling work to the executors
   # executors perform the code assigned by driver and report results
# Parallelism in Spark means running work thru a cluster (group of comp) concurrently, instead of on a single comp
   # Data is broken intto partitions, meaning a chunk of data will sit on a physical machine in your cluster

# Spark API, spark was written in Scala but the API can translate to different languages like python and javascript
# This course focuses on PySpark - scala API translated to python

#PySpark is mainly used on Google Colab Notebooks




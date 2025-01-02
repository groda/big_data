# This file was generated from PySpark_miscellanea.ipynb with nbconvert
# Source: https://github.com/groda/big_data

 #!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/groda/big_data/blob/master/PySpark_miscellanea.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <a href="https://github.com/groda/big_data"><div><img src="https://github.com/groda/big_data/blob/master/logo_bdb.png?raw=true" align=right width="90"></div></a>
# # PySpark miscellanea
# 
# 
# 
# > _PySpark is the Python API for Apache Spark. It enables you to perform real-time, large-scale data processing in a distributed environment using Python. It also provides a PySpark shell for interactively analyzing your data._
# 
# (from: [https://spark.apache.org/docs/latest/api/python/index.html](https://spark.apache.org/docs/latest/api/python/index.html))
# 
# In this notebook, we showcase various tips, tricks, and insights related to PySpark.
# 

# ## Table of contents
# 
# <div class="toc"><ul class="toc-item">
# <li><span><a href="#scrollTo=How_to_get_your_application_s_ID">How to get your application's ID</a></span></li>
# <li><span><a href="#scrollTo=Default_parallelism">Default parallelism</a></span></li>
# <li><span><a href="
# #scrollTo=How_to_change_PySpark_s_log_level">How to change PySpark's log level</a></span></li>
# <li><span><a href="#scrollTo=Add_your_own_logging_messages">Add your own logging messages</a></span></li>
# </ul></div>

# # Preliminaries
# 
# The libraries needed to run this notebook. Execute this cell before any other.

# In[1]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, sum, avg, stddev, expr, year
from datetime import timedelta, date
import os
import subprocess


# # How to get your application's ID
# 
# 
# See also: [How to extract application ID from the PySpark context](https://stackoverflow.com/questions/30983226/how-to-extract-application-id-from-the-pyspark-context).
# 
# 

# ## From the Spark session
# 
# What is a [Spark session](https://spark.apache.org/docs/latest/sql-getting-started.html#starting-point-sparksession)?

# In[2]:


spark = SparkSession \
    .builder \
    .appName("My Spark App 🌟") \
    .getOrCreate()


# Get the session's context ([what is a Spark context?](https://spark.apache.org/docs/latest/rdd-programming-guide.html#initializing-spark) and [detailed documentation](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.html)).

# In[3]:


sc = spark.sparkContext
sc


# Get `applicationId` from the context `sc`.

# In[4]:


sc.applicationId


# Or in one single step:

# In[5]:


spark.sparkContext.applicationId


# ## In the PySpark shell
# 
# If you're using the _PySpark shell_ (see [using the shell](https://spark.apache.org/docs/latest/rdd-programming-guide.html#initializing-spark)), `SparkContext` is created automatically and it can be accessed from the variable called `sc`.

# ```
# Python 3.10.12 (main, Nov  6 2024, 20:22:13) [GCC 11.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# Setting default log level to "WARN".
# To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
# 25/01/01 11:40:51 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
# 25/01/01 11:40:52 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
# Welcome to
#       ____              __
#      / __/__  ___ _____/ /__
#     _\ \/ _ \/ _ `/ __/  '_/
#    /__ / .__/\_,_/_/ /_/\_\   version 3.5.3
#       /_/
# 
# Using Python version 3.10.12 (main, Nov  6 2024 20:22:13)
# Spark context Web UI available at http://2c6bcae43959:4041
# Spark context available as 'sc' (master = local[*], app id = local-1735731652766).
# SparkSession available as 'spark'.
# >>> sc.applicationId
# 'local-1735731652766'
# >>> quit()
# ```

# You can also launch a PySpark shell within the notebook environment (note: you are going to have to input your commands in a box after clicking next to the `>>>` prompt).
# 
# We are using the `timeout` function (credit: [https://stackoverflow.com/a/52975118](https://stackoverflow.com/a/52975118)) to prevent the notebook from getting stuck when being executed automatically.

# In[6]:


get_ipython().system('timeout 20 pyspark')


# Close the Spark session with `stop()`.

# In[7]:


spark.stop()


# # Default parallelism

# ## What is `spark.default.parallelism`?
# 
# This property determines the default number of chunks in which an RDD ([Resilient Distributed Dataset](https://spark.apache.org/docs/latest/rdd-programming-guide.html#resilient-distributed-datasets-rdds)) is partitioned. This, in turn, affects how many tasks are executed concurrently.

# Unless specified by the user, the default value of `default.parallelism` is set based on the _cluster manager_:
#  - in standalone mode it is equal to the number of (virtual) cores on the local machine
#  - in Mesos: 8
#  - for YARN, Kubernetes: total number of cores on all executor nodes or 2, whichever is larger
# 
#  (see [Spark configuration/Execution behavior](https://spark.apache.org/docs/latest/configuration.html#execution-behavior))

# ## Get or set default parallelism

# Create a [Spark session](https://spark.apache.org/docs/latest/sql-getting-started.html#starting-point-sparksession).

# In[8]:


spark = SparkSession \
        .builder \
        .appName("Default Parallelism 🧵🧵") \
        .getOrCreate()


# Show the value of `defaultParallelism`:

# In[9]:


spark.sparkContext.defaultParallelism


# To change a property it's necessary to stop and start a new context/session, you can't just change the configuration on an existing session!

# In[10]:


spark = SparkSession \
        .builder \
        .config("spark.default.parallelism", 4) \
        .getOrCreate()


# Default parallelism hasn't changed!

# In[11]:


spark.sparkContext.defaultParallelism


# Same with [`SparkSession.conf.set`](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.conf.html#pyspark.sql.SparkSession.conf):

# In[12]:


spark.conf.set("spark.default.parallelism", 3)
spark.sparkContext.defaultParallelism


# Stop and start session anew.

# In[13]:


spark.stop()
spark = SparkSession \
        .builder \
        .appName("Default Parallelism 🧵🧵🧵🧵") \
        .config("spark.default.parallelism", 4) \
        .getOrCreate()


# In[14]:


spark.sparkContext.defaultParallelism


# Great! Now the context has been changed (and also the applications's name has been updated).

# In[15]:


spark.sparkContext


# The reason why you cannot change a "running" context is that
# 
# > _Once a `SparkConf` object is passed to Spark, it is cloned and can no longer be modified by the user._
# 
# (see [`SparkConf`](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.html#pyspark.SparkConf) in the PySpark API documentation)

# ## Example of how parallelism can influence the runtime of computation
# 
# Of course parallelism is ultimately limited by the number of available virtual cores but if your cluster has sufficient resources, increasing the value of `default.parallelism` has the potential of speeding up computations.
# 
# The standard Google Colab notebook has two cores, so $2$ is the maximum parallelization that can be achieved.

# In[16]:


print(f"Number of cores: {os.cpu_count()}")


# We are going to create a DataFrame with random numbers using `range` and then compute the sum, average, standard deviation, and median of all values.

# In[17]:


# Create SparkSession
spark = SparkSession.builder.appName("Parallelism Demo ⚙️⚙️").getOrCreate()

# Create a DataFrame with random numbers
df = spark.range(10**4).withColumn("value", rand())


# Define an aggregation function that computes the sum of all numbers.

# In[18]:


def aggregate_data(data_frame):
    result = data_frame.groupBy().agg(
        sum("value").alias("total_value"),
        avg("value").alias("average_value"),
        stddev("value").alias("std_deviation"),
        expr("percentile_approx(value, 0.5)").alias("median")  # Approximate median
    )
    return result


# In[19]:


aggregate_data(df).collect()


# Now run the same computation with different parallelism settings (but note that you won't be able to appreciate the effect of parallelism unless you try this on a system with more than 2 CPUs!).
# 
# ⚠️ Warning: the following computation might take a couple of minutes to run since it performs some calculations on a dataframe with $10^8$ rows and on Colab you get a maximum parallelism of $2$.

# In[20]:


for parallelism in [1, 2, 4, 8]:
  # Create SparkSession
  spark.stop()
  spark = SparkSession.builder.appName(f"Default Parallelism {'🧵'*parallelism}") \
                      .config("spark.default.parallelism", parallelism) \
                      .getOrCreate()
  # Create a DataFrame with random numbers
  df = spark.range(10**8).withColumn("value", rand())

  print(f"Parallelism: {spark.sparkContext.getConf().get('spark.default.parallelism')}")
  get_ipython().run_line_magic('time', 'aggregate_data(df).collect() # Trigger the computation')
  print("")


# I ran the same code on my laptop with $8$ CPUs and got better results where one can see how increasing parallelism reduces the total runtime.
# 
# ```
# Parallelism: 1
# CPU times: user 8.22 ms, sys: 3.96 ms, total: 12.2 ms                           
# Wall time: 42.4 s
# 
# Parallelism: 2
# CPU times: user 4.96 ms, sys: 1.97 ms, total: 6.94 ms                           
# Wall time: 23 s
# 
# Parallelism: 4
# CPU times: user 4.27 ms, sys: 1.66 ms, total: 5.93 ms                           
# Wall time: 16 s
# 
# Parallelism: 8
# CPU times: user 4.58 ms, sys: 1.78 ms, total: 6.36 ms                           
# Wall time: 15 s
# ```

# # How to change PySpark's log level
# 
# Log levels in PySpark sorted from the most verbose to the least are:
# 
# 
# * ALL
# * TRACE
# * DEBUG
# * INFO
# * WARN
# * ERROR
# * FATAL
# * OFF
# 
# 
# See [https://spark.apache.org/docs/.../api/pyspark.SparkContext.setLogLevel.html](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.setLogLevel.html).
# 

# ## In the PySpark shell
# 
# To change the log level to "INFO" in the PySpark shell just enter:
# 
#     sc.setLogLevel("INFO")
# 
# ⚠️ Anything log level above "INFO" is extermely verbose, so be prepared for a lot of output!

# In[21]:


get_ipython().system('timeout 240 pyspark')


# ```
# from pyspark.sql.functions import year
# from datetime import timedelta, date
# 
# df = spark.createDataFrame([
#     {"date": date.today(), "value": 2.1},
#     {"date": date.today() + timedelta(days=1), "value": 1.9},
#     {"date": date.today() + timedelta(days=2), "value": 2.3},
#     {"date": date.today() - timedelta(days=365*5), "value": 3.0},
# ])
# 
# sc = spark.sparkContext
# sc.setLogLevel("INFO")
# df.groupBy(year("date")).avg().show()
# sc.setLogLevel("WARN")
# df.groupBy(year("date")).avg().show()
# ```

# ## In a PySpark script
# 
# After finding `$SPARK_HOME`, we are going to create a Log4J configuration file and finally run a PySpark script showcasing different log levels.
# 
# See also: [PySpark on Google Colab](https://github.com/groda/big_data/blob/master/PySpark_On_Google_Colab.ipynb).

# In[22]:


get_ipython().system('find_spark_home.py')


# In[23]:


# Run the script and capture its output
result = subprocess.run(["find_spark_home.py"], capture_output=True, text=True)

# Print or use the captured output
print("Output of find_spark_home.py:", result.stdout)

# set SPARK_HOME environment variable
os.environ['SPARK_HOME'] = result.stdout.strip()


# Now the variable `SPARK_HOME` is set.

# In[24]:


get_ipython().system('echo $SPARK_HOME')


# Create a `log4j2.properties` file in Spark's configuration directory.

# In[25]:


get_ipython().run_cell_magic('bash', '', "# create conf directory
# with the option -p mkdir won't complain if the folder already exists
mkdir -p $SPARK_HOME/conf

# populate log4j2.properties file
FILE=$SPARK_HOME/conf/log4j2.properties

# read about heredocs: https://tldp.org/LDP/abs/html/here-docs.html
cat> $FILE <<🤖
status = warn

appender.console.type = Console
appender.console.name = STDOUT
appender.console.target = SYSTEM_ERR

rootLogger.level = warn
rootLogger.appenderRef.stdout.ref = STDOUT

# formatting
appender.console.layout.type = PatternLayout
appender.console.layout.pattern = %d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n
🤖
")


# In[26]:


get_ipython().run_cell_magic('writefile', 'my_app.py', 'from pyspark.sql import SparkSession
from datetime import timedelta, date
from pyspark.sql.functions import year
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Creating Spark session")
    spark = SparkSession.builder.appName("Logging levels 📝").getOrCreate()

    df = spark.createDataFrame([
        {"date": date.today(), "value": 2.1},
        {"date": date.today() + timedelta(days=1), "value": 1.9},
        {"date": date.today() + timedelta(days=2), "value": 2.3},
        {"date": date.today() - timedelta(days=365*5), "value": 3.0},
    ])

    df.groupBy(year("date")).avg().show()
    sc = spark.sparkContext
    logger.error("Setting log level to INFO")
    sc.setLogLevel("INFO")
    df.groupBy(year("date")).avg().show()
    spark.stop()
')


# In[27]:


get_ipython().system('spark-submit my_app.py')


# # Add your own logging messages
# 
# PySpark's logging system is based on the Log4j logger and is configured in the `log4j2.properties` file.
# 
# You can set up your own logging system and integrate it with PySpark's logging.
# 
# We are going to showcase two scenarios:
# 
# * two distinct logging systems (PySpark's logging system and Python's `logging`)
# * unified logging by redirecting PySpark's logs to Python's `logging` module

# ## Two logging systems

# In[28]:


get_ipython().run_cell_magic('writefile', 'test.py', 'from pyspark.sql import SparkSession
import logging

# Create a SparkSession
spark = SparkSession.builder \
   .appName("Logging Demo: two systems") \
   .getOrCreate()

# create my logger and set log level to WARN
logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# set PySpark log level to WARN
sc = spark.sparkContext
sc.setLogLevel("WARN")

rdd = spark.sparkContext.parallelize(range(10**5))
logger.error("Computed sum: %s", rdd.sum())

# Stop the SparkSession
spark.stop()
')


# In[29]:


get_ipython().system('spark-submit test.py')


# ## Unified logging

# In[30]:


get_ipython().run_cell_magic('writefile', 'test.py', 'from pyspark.sql import SparkSession
import logging

# Create a SparkSession
spark = SparkSession.builder \
   .appName("Logging Demo: unified log system") \
   .getOrCreate()

sc = spark.sparkContext

# use PySpark\'s logger and set log level to WARN
log4jLogger = sc._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(__name__)
logger.setLevel(log4jLogger.Level.WARN)  # Set desired logging level

# set PySpark log level to WARN
sc.setLogLevel("WARN")

rdd = spark.sparkContext.parallelize(range(10**5))
logger.warn(f"Computed sum: {rdd.sum()}")

# Stop the SparkSession
spark.stop()
')


# In[31]:


get_ipython().system('spark-submit test.py')


# Now your warning generated by the line
# 
#     logger.warn(f"Computed sum: {rdd.sum()}")
# 
# is integrated with the Log4j messages and has the same format.

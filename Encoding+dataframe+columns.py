# This file was generated from Encoding+dataframe+columns.ipynb with nbconvert
# Source: https://github.com/groda/big_data

 #!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/groda/big_data/blob/master/Encoding%2Bdataframe%2Bcolumns.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <a href="https://github.com/groda/big_data"><div><img src="https://github.com/groda/big_data/blob/master/logo_bdb.png?raw=true" align=right width="90"></div></a>
# 
# # Encode columns in csv file
# <br>
# <br>
# 
# 
# 
# I'm given a CSV file containing strings and I want to convert the characters to numeric values. I want to use different encodings of the characters on different columns or groups of columns.
# 
# Let's say for instance that I have two encodings __A__ and __B__:
#  - in encoding __A__ I want to encode the character `a` with the number `1`, the character `b` with `2`, and `c` with `3`
#  - in encoding __B__ I want to encode the character `a` with the number `2`, the character `b` with `3`, and `c` with `1`
# 
# If I use encoding __A__ to transform all columns in table
# 
# | c1| c2 |
# |-----|-----|
# | a | a|
# | b | b|
# | c | b|
# 
# I obtain
# 
# | c1_enc| c2_enc |
# |-----|-----|
# | 1 | 1|
# | 2 | 2|
# | 3 | 2|
# 
# If `col1` is encoded with __A__ and `col2` is encoded with __A__ then the table becomes
# 
# | c1_enc| c2_enc |
# |-----|-----|
# | 1 | 2|
# | 2 | 3|
# | 3 | 3|

# ## Install PySpark

# In[1]:


get_ipython().system('pip install pyspark')


# ## Download the data
# 
# Retrieve the CSV file `data-1600cols.csv` and write it to the local storage.

# In[2]:


import requests
import csv

def download_csv(url, save_path):
    response = requests.get(url)

    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"CSV file downloaded successfully and saved at: {save_path}")
    else:
        print(f"Failed to download CSV file. Status code: {response.status_code}")

url = "https://raw.githubusercontent.com/groda/big_data/master/data-1600cols.csv"
save_path = "data-1600cols.csv"

download_csv(url, save_path)


# ## Initialize Spark session
# 
# SparkContext allows me to access Dataframes, change Spark configuration, cancel a job, get status of a job, etc.
# 
# Load  the CSV file `data-1600cols.csv` into a Spark dataframe using the file's header as column names.

# In[3]:


from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import SQLContext

spark = SparkSession \
            .builder \
            .master("local") \
            .appName("Encode multiple columns") \
            .getOrCreate()

sqlContext = SQLContext(spark)
df = sqlContext.read.csv("data-1600cols.csv", header=True)


# Check configuration

# In[4]:


spark.sparkContext.getConf().getAll()


# Check size of the dataframe (number of rows and columns)

# In[5]:


print('Number of rows: {}
Number of columns: {}'.format(df.count(),len(df.columns)))


# Check if the dataframe contains any nulls?

# In[6]:


df.where(df.V2.isNull()).collect()


# Show a couple of columns

# In[7]:


df.select('V1','V2','V3').show()


# ## First approach
# 
# Using the `translate` function from `pyspark.sql` and adding a new column with `withColumn` at each step. Test on a small dataframe `test_df`.

# In[8]:


import pyspark.sql.functions as f

test_df = sqlContext.createDataFrame([('a', 'a'), ('b', 'b'), ('c', 'b')], ['c1', 'c2'])
test_df.show()

chars = "abc"
A = "123" # encoding A
B = "231" # encoding B


for col_name in ["c1", "c2"]:
    test_df = test_df.withColumn(col_name+'_enc', f.translate(f.col(col_name), "abcd", A))

test_df.show()


# Try out this approach on the big dataframe, applying the function to a few columns. I define two random encodings, `encodingA` and `encodingB` and apply each encoding to two different columns.

# In[9]:


import string
import random

# set a raneom seed
random.seed(30)

chars = string.ascii_lowercase
encodingA = ''.join(random.choice(string.digits) for i in range(len(chars)))
encodingB = ''.join(random.choice(string.digits) for i in range(len(chars)))

print("Encodings:")
print(chars)
print(encodingA)
print(encodingB)
print("-"*26)
new_df=df

for col_name in ["V1", "V3"]:  # apply encodingA to columns V1, V3
    new_df=new_df.withColumn(col_name+'_enc',f.translate(f.col(col_name), chars, encodingA))
for col_name in ["V2", "V4"]:  # apply encodingB to columns V2, V4
    new_df=new_df.withColumn(col_name+'_enc',f.translate(f.col(col_name), chars, encodingB))

new_df.select("V1","V2","V3","V4", "V1_enc", "V2_enc", "V3_enc", "V4_enc").show()


# Apply encodings to 4 columns

# In[10]:


new_df=df

for col_name in ["V1", "V3"]:  # apply encodingA to columns V1, V2
    new_df = new_df.withColumn(col_name,f.translate(f.col(col_name), chars, encodingA))
for col_name in ["V2", "V4"]:  # apply encodingB to columns V3, V4
    new_df = new_df.withColumn(col_name,f.translate(f.col(col_name), chars, encodingB))

new_df.select("V1","V2","V3","V4").show(3)


# Check:
# 
# 
# | V1 | V2 | V3 | V4
# |---|---|---|---|
# | 6 | 2 | 0 | 4 |
# | 0 | 2 | 5 | 6 |
# | 3 | 4 | 8 | 4 |

# When applying encoding to thousands of rows the previous approach is too slow. The reason is that I'm writing a new dataframe after each tranformation.
# 
# Split columns in even and odd, apply two different encodings to each set of columns.

# In[11]:


cols_e = ["V"+str(i) for i in range(2,5,2)]
cols_o = ["V"+str(i) for i in range(1,4,2)]

print(cols_e)
print(cols_o)

new_df=df

# works with a few columns (4 in total in this example) but too slow for thousands of columns
for col_name in cols_o:  # apply encodingA to columns with even numbers
    new_df=new_df.withColumn(col_name,f.translate(f.col(col_name), chars, encodingA))
for col_name in cols_e:  # apply encodingB to odd columns
    new_df=new_df.withColumn(col_name,f.translate(f.col(col_name), chars, encodingB))

new_df.select(["V"+str(i) for i in range(1,5)]).show(3)


# ## Second approach
# Using `udf` (user-defined functions). Avoiding `withColumn` and using `select` instead.

# In[12]:


from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType, StringType

# define an encoding as a list of two strings of equal length

o = ["abcdefghijklmnopqrstuvwxyz", encodingA]

def enc(*a):
    # encode string s with encoding o
    s=a[0]
    for i in range(len(o[0])):
      if s==o[0][i]:
          return o[1][i]
    return s

# create udf
encode_udf = udf(enc, StringType())

cols_o = ["V"+str(i) for i in range(7) if i%2==1]
print(cols_o)

(
df.select("V1","V3","V5",
           encode_udf("V1").alias("V1_enc"),
           encode_udf("V3").alias("V3_enc"),
           encode_udf("V5").alias("V5_enc"))
    .show(10)
)


# And now encode all even and odd numbered columns with `encodingA` and `encodingB`, respectively using `select`.

# In[13]:


# apply function to 50 columns
new_df=df.select([encode_udf("V"+str(i)).alias("V"+str(i)+"_enc") for i in range(1,100,2)])
new_df.select(["V"+str(i)+"_enc" for i in range(1,21,2)]).show(10)


# In[14]:


# apply function to 100 columns
new_df=df.select([encode_udf("V"+str(i)).alias("V"+str(i)+"_enc") for i in range(1,201,2)])
new_df.select(["V"+str(i)+"_enc" for i in range(1,21,2)]).show(10)


# In[15]:


# apply function to 400 columns
new_df=df.select([encode_udf("V"+str(i)).alias("V"+str(i)+"_enc") for i in range(1,401,2)])
new_df.select(["V"+str(i)+"_enc" for i in range(381,401,2)]).show(10)


# In[16]:


# apply function to all odd columns

new_df = df.select([encode_udf("V"+str(i)).alias("V"+str(i)+"_enc") for i in range(1,801,2)])

new_df.select(["V"+str(i)+"_enc" for i in range(781,801,2)]).show(10)


# Now I want to apply different udfs

# In[17]:


o = ["abcdefghijklmnopqrstuvwxyz", encodingA]
e = ["abcdefghijklmnopqrstuvwxyz", encodingB]

# define two encoding functions

def enc1(*a):
    # encode string s with encoding o
    s=a[0]
    for i in range(len(o[0])):
      if s==o[0][i]:
          return o[1][i]
    return s

def enc2(*a):
    # encode string s with encoding e
    s=a[0]
    for i in range(len(e[0])):
      if s==e[0][i]:
          return e[1][i]
    return s

# create udfs
encode_udf1 = udf(enc1, StringType())
encode_udf2 = udf(enc2, StringType())

new_df = df.select([encode_udf1("V"+str(i)).alias("V"+str(i)+"_enc") for i in range(1,800,2)]+
                  [encode_udf2("V"+str(i)).alias("V"+str(i)+"_enc") for i in range(2,801,2)])
new_df.select(["V"+str(i)+"_enc" for i in range(1,5)]+["V"+str(i)+"_enc" for i in range(795,801)]).show(10)


# ## Export dataframe to file

# In[18]:


import time
timestamp = time.strftime("%Y%m%d%H%M%S")
new_df.write.csv('out'+timestamp+'.csv', sep=',')
print('saved out{}.csv'.format(timestamp))


# Save to CSV with headers

# In[19]:


timestamp = time.strftime("%Y%m%d%H%M%S")
new_df.write.csv('out'+timestamp+'.csv', sep=',', header = True)
print('saved out{}.csv'.format(timestamp))


# In[20]:


get_ipython().system('ls out*')


# ## Useful commands for checking system resources
# 
# The `free -h` and `lscpu` commands are useful for retrieving information about system resources in a Linux environment.

# The `free -h` command displays information about the system's memory usage in human-readable format. With the `-h` option the command displays sizes in a more human-readable format, using units such as megabytes (MB) and gigabytes (GB) in place of bytes.

# In[21]:


get_ipython().system('free -h')


# The `lscpu` command displays detailed information about the CPU architecture.

# In[22]:


get_ipython().system('lscpu')


# In the context of distributed computing, specific values provided by the lscpu command are of particular interest:
# 
# *   the number of CPUs
# *   cores per socket
# *   threads per core
# *   sockets
# 
# Understanding these parameters is crucial for assessing the system's potential parallelism.
# 
# Sockets represents the number of physical processors. Each processor can have one or more cores and each core can execute one or two threads concurrently.
# 
# Finally, the number of CPUs indicates the total count of independent processing units within each CPU. This is the theoretical upper limit on the number of tasks that can be executed concurrently, offering valuable information for maximizing computational efficiency in distributed computing scenarios.
# 
# For instance, if you have
# 
# ```
# Thread(s) per core:    2
# Core(s) per socket:    4
# Socket(s):             1
# ```
# 
# then the total number of independent processing units is
# 
# $$ 1 × 4 × 2 = 8$$
# 
# See also: [How many physical CPUs does my machine have?](https://superuser.com/questions/1691479/how-many-physical-cpus-does-my-machine-have).
# 
# 

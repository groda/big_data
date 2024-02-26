# This file was generated from generate_data_with_Faker.ipynb with nbconvert
# Source: https://github.com/groda/big_data

 #!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/groda/big_data/blob/master/generate_data_with_Faker.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <a href="https://github.com/groda/big_data"><div><img src="https://github.com/groda/big_data/blob/master/logo_bdb.png?raw=true" align=right width="90"></div></a>
# 
# # Data Generation and Aggregation with Python's Faker Library and PySpark
# <br>
# <br>
# 
# Explore the capabilities of the Python Faker library (https://faker.readthedocs.io/) for dynamic data generation!
# 
# Whether you're a data scientist, engineer, or analyst, this tutorial will guide you through the process of creating realistic and diverse datasets using Faker and then harnessing the distributed computing capabilities of PySpark to aggregate and analyze the generated data.
# 
# 
# 
# **Note:** This is not _synthetic_ data as it is generated using simple methods and will most likely not fit any real-life distribution. Still, it serves as a valuable resource for testing purposes when authentic data is unavailable.

# # Install Faker
# 
# The Python `faker` module needs to be installed. Note that on Google Colab you can use `!pip` as well as just `pip` (no exclamation mark).

# In[ ]:


get_ipython().system('pip install faker')


# # Generate a Pandas dataframe with fake data

# Import `Faker` and set a random seed ($42$).

# In[ ]:


from faker import Faker
# Set the seed value of the shared `random.Random` object
# across all internal generators that will ever be created
Faker.seed(42)


# `fake` is a fake data generator with `DE_de` locale.

# In[ ]:


fake = Faker('de_DE')
fake.seed_locale('de_DE', 42)
# Creates and seeds a unique `random.Random` object for
# each internal generator of this `Faker` instance
fake.seed_instance(42)


# Import Pandas to save data into a dataframe

# In[ ]:


# true if running on Google Colab
import sys
IN_COLAB = 'google.colab' in sys.modules
if not IN_COLAB:
 get_ipython().system('pip install pandas==1.5.3')

import pandas as pd


# The function `create_row_faker` creates one row of fake data. Here we choose to generate a row containing the following fields:
#  - `fake.name()`
#  - `fake.postcode()`
#  - `fake.email()`
#  - `fake.country()`.

# In[ ]:


def create_row_faker(num=1):
    output = [{"name": fake.name(),
               "age": fake.random_int(0, 100),
               "postcode": fake.postcode(),
               "email": fake.email(),
               "nationality": fake.country(),
              } for x in range(num)]
    return output


# Generate a single row

# In[ ]:


create_row_faker()


# Generate a dataframe `df_fake` of 5000 rows using `create_row_faker`.
# 
# We're using the _cell magic_ `%%time` to time the operation.

# In[ ]:


get_ipython().run_cell_magic('time', '', 'df_fake = pd.DataFrame(create_row_faker(5000))
')


# View dataframe

# In[ ]:


df_fake


# For more fake data generators see Faker's [standard providers](https://faker.readthedocs.io/en/master/providers.html#standard-providers) as well as [community providers](https://faker.readthedocs.io/en/master/communityproviders.html#community-providers).

# # Generate PySpark dataframe with fake data

# Install PySpark.

# In[ ]:


get_ipython().system('pip install pyspark')


# In[ ]:


from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("Faker demo") \
    .getOrCreate()


# In[ ]:


df = spark.createDataFrame(create_row_faker(5000))


# To avoid getting the warning, either use [pyspark.sql.Row](https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.Row) and let Spark infer datatypes or create a schema for the dataframe specifying the datatypes of all fields (here's the list of all [datatypes](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=types#module-pyspark.sql.types)).

# In[ ]:


from pyspark.sql.types import *
schema = StructType([StructField('name', StringType()),
                     StructField('age',IntegerType()),
                     StructField('postcode',StringType()),
                     StructField('email', StringType()),
                     StructField('nationality',StringType())])


# In[ ]:


df = spark.createDataFrame(create_row_faker(5000), schema)


# In[ ]:


df.printSchema()


# Let's generate some more data (dataframe with $5
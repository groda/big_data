# This file was generated from Apache_Sedona_with_PySpark.ipynb with nbconvert
# Source: https://github.com/groda/big_data

 #!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/groda/big_data/blob/master/Apache_Sedona_with_PySpark.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 
# <a href="https://github.com/groda/big_data"><div><img src="https://github.com/groda/big_data/blob/master/logo_bdb.png?raw=true" align=right width="90" alt="Logo Big Data for Beginners"></div></a>
# # Apache Sedona with PySpark
# 
# Apache Sedona™ is
# 
# > *a cluster computing system for processing large-scale spatial data. Sedona extends existing cluster computing systems, such as Apache Spark, Apache Flink, and Snowflake, with a set of out-of-the-box distributed Spatial Datasets and Spatial SQL that efficiently load, process, and analyze large-scale spatial data across machines.* ([https://sedona.apache.org/](https://sedona.apache.org/))
# 
# To execute a basic Sedona demonstration using PySpark on Google Colab, we made a few minor adjustments. The Sedona notebook starts below at [Apache Sedona Core demo](#scrollTo=Apache_Sedona_Core_demo).
# 
# 

# ## Install Apache Sedona and PySpark
# 
# To start with, we are going to install PySpark with Sedona following the instructions at: https://sedona.apache.org/latest-snapshot/setup/install-python/ but first we need to downgrade `shapely` because the version 2.0.2 that comes with Google Colab does not play well with the current version of Apache Sedona (see https://shapely.readthedocs.io/en/stable/migration.html).

# ### Downgrade Shapely to version 1.7.1
# 
# We need to install install any version of `shapely>=1.7.0` but smaller than `2.0`. We picked `1.7.1` because with 1.7.0 we got the error
# 
#     geopandas 0.13.2 requires shapely>=1.7.1, but you have shapely 1.7.0 which is incompatible.
# 
# Explanation for `pip -I`:
# 
# - [`-I, --ignore-installed`](https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-I)
# > Ignore the installed packages, overwriting them. This can break your system if the existing package is of a different version or was installed with a different package manager!
# 
# 
# 
# 
# 
# 

# In[1]:


get_ipython().system('pip install -I shapely==1.7.1')


# ### Install Geopandas
# 
# This step is only needed outside of Colab because on Google Colab `geopandas` is available by default.

# In[2]:


get_ipython().system('pip install geopandas==0.13.2')


# ### Install Apache Sedona and PySpark
# 
# We can now install Apache Sedona together with PySpark (and Spark).

# In[3]:


get_ipython().system('pip install apache-sedona[spark]')


# In[4]:


get_ipython().run_line_magic('env', 'SPARK_HOME = "/usr/local/lib/python3.10/dist-packages/pyspark"')


# In[5]:


get_ipython().run_line_magic('env', 'PYTHONPATH = /usr/local/lib/python3.10/dist-packages/pyspark/python')


# In[6]:


get_ipython().system('pip info pyspark')


# ## Setup environment variables
# 
# We need to set two environment variables:
# 
# - `SPARK_HOME`
# - `PYTHONPATH`
# 
# Once we have set `SPARK_HOME`, the variable `PYTHONPATH` is `$SPARK_HOME/python`.
# 
# ### Find Spark home
# 
# There's an utility to find Spark home and I always forget how it's called exactly, what I remember is that it contains `"find"` and `"spark"`. Let us search for it:

# In[7]:


get_ipython().system('find / -name "*find*spark*"')


# The script `/usr/local/bin/find_spark_home.py` is successful at finding Spark's home.

# #### Set `SPARK_HOME`

# In[8]:


import sys
import os
IN_COLAB = 'google.colab' in sys.modules
if IN_COLAB:
  output = get_ipython().getoutput('python /usr/local/bin/find_spark_home.py')
else:
  output = get_ipython().getoutput('find / -name "pyspark" -type d 2>/dev/null|head -1')
# Store the output using %store
get_ipython().run_line_magic('store', 'output')
# get rid of extra quotation marks
os.environ['SPARK_HOME'] = output[0].replace('"', '')


# In[9]:


get_ipython().system('pip show pyspark')


# Verify that the correct `SPARK_HOME` has been set.

# In[10]:


os.environ['SPARK_HOME']


# In[11]:


get_ipython().run_line_magic('env', 'SPARK_HOME')


# #### Set `PYTHONPATH`

# In[12]:


os.environ['PYTHONPATH'] = os.environ['SPARK_HOME'] + '/python'


# Check

# In[13]:


get_ipython().run_line_magic('env', 'PYTHONPATH')


# ## Download data
# 
# In order to run, the Sedona notebook expects to find some specific files in the local folder `data`. Let us populate `data` with the files from the Sedona Github repository.

# In[14]:


get_ipython().run_cell_magic('bash', '', '# it would be more efficient to just download the "data" folder and not the whole repo
[ -d sedona ] || git clone https://github.com/apache/sedona.git

cp -r sedona/binder/data ./
')


# Verify the presence of data in the designated `data` folder.

# In[15]:


get_ipython().system('ls data')


# # Apache Sedona Core demo
# 
# The notebook is available at the following link:
# https://github.com/apache/sedona/blob/master/binder/ApacheSedonaCore.ipynb
# 

# ```
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# ```

# In[16]:


from pyspark.sql import SparkSession
from pyspark import StorageLevel
import geopandas as gpd
import pandas as pd
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType
from pyspark.sql.types import LongType
from shapely.geometry import Point
from shapely.geometry import Polygon

from sedona.spark import *
from sedona.core.geom.envelope import Envelope


# In[17]:


config = SedonaContext.builder() .\
    config('spark.jars.packages',
           'org.apache.sedona:sedona-spark-3.4_2.12:1.5.1,'
           'org.datasyslab:geotools-wrapper:1.5.1-28.2,'
           'uk.co.gresearch.spark:spark-extension_2.12:2.11.0-3.4'). \
    config('spark.jars.repositories', 'https://artifacts.unidata.ucar.edu/repository/unidata-all'). \
    getOrCreate()

sedona = SedonaContext.create(config)


# In[18]:


sc = sedona.sparkContext


# # Create SpatialRDD

# ## Reading to PointRDD from CSV file

# Suppose we want load the CSV file into Apache Sedona PointRDD
# ```
# testattribute0,-88.331492,32.324142,testattribute1,testattribute2
# testattribute0,-88.175933,32.360763,testattribute1,testattribute2
# testattribute0,-88.388954,32.357073,testattribute1,testattribute2
# testattribute0,-88.221102,32.35078,testattribute1,testattribute2
# testattribute0,-88.323995,32.950671,testattribute1,testattribute2
# testattribute0,-88.231077,32.700812,testattribute1,testattribute2
# ```

# In[19]:


point_rdd = PointRDD(sc, "data/arealm-small.csv", 1, FileDataSplitter.CSV, True, 10)


# In[20]:


## Getting approximate total count
point_rdd.approximateTotalCount


# In[21]:


# getting boundary for PointRDD or any other SpatialRDD, it returns Enelope object which inherits from
# shapely.geometry.Polygon
point_rdd.boundary()


# In[22]:


# To run analyze please use function analyze
point_rdd.analyze()


# In[23]:


# Finding boundary envelope for PointRDD or any other SpatialRDD, it returns Enelope object which inherits from
# shapely.geometry.Polygon
point_rdd.boundaryEnvelope


# In[24]:


# Calculate number of records without duplicates
point_rdd.countWithoutDuplicates()


# In[25]:


# Getting source epsg code
point_rdd.getSourceEpsgCode()


# In[26]:


# Getting target epsg code
point_rdd.getTargetEpsgCode()


# In[27]:


# Spatial partitioning data
point_rdd.spatialPartitioning(GridType.KDBTREE)


# ## Operations on RawSpatialRDD

# rawSpatialRDD method returns RDD which consists of GeoData objects which has 2 attributes
# <li> geom: shapely.geometry.BaseGeometry </li>
# <li> userData: str </li>
# 
# You can use any operations on those objects and spread across machines

# In[28]:


# take firs element
point_rdd.rawSpatialRDD.take(1)


# In[29]:


# collect to Python list
point_rdd.rawSpatialRDD.collect()[:5]


# In[30]:


# apply map functions, for example distance to Point(52 21)
point_rdd.rawSpatialRDD.map(lambda x: x.geom.distance(Point(21, 52))).take(5)


# ## Transforming to GeoPandas

# ## Loaded data can be transformed to GeoPandas DataFrame in a few ways

# ### Directly from RDD

# In[31]:


point_rdd_to_geo = point_rdd.rawSpatialRDD.map(lambda x: [x.geom, *x.getUserData().split("	")])


# In[32]:


point_gdf = gpd.GeoDataFrame(
    point_rdd_to_geo.collect(), columns=["geom", "attr1", "attr2", "attr3"], geometry="geom"
)


# In[33]:


point_gdf[:5]


# ### Using Adapter

# In[34]:


# Adapter allows you to convert geospatial data types introduced with sedona to other ones


# In[35]:


spatial_df = Adapter.\
    toDf(point_rdd, ["attr1", "attr2", "attr3"], sedona).\
    createOrReplaceTempView("spatial_df")

spatial_gdf = sedona.sql("Select attr1, attr2, attr3, geometry as geom from spatial_df")


# In[36]:


spatial_gdf.show(5, False)


# In[37]:


gpd.GeoDataFrame(spatial_gdf.toPandas(), geometry="geom")[:5]


# ### With DataFrame creation

# In[38]:


schema = StructType(
    [
        StructField("geometry", GeometryType(), False),
        StructField("attr1", StringType(), False),
        StructField("attr2", StringType(), False),
        StructField("attr3", StringType(), False),
    ]
)


# In[39]:


geo_df = sedona.createDataFrame(point_rdd_to_geo, schema, verifySchema=False)


# In[40]:


gpd.GeoDataFrame(geo_df.toPandas(), geometry="geometry")[:5]


# # Load Typed SpatialRDDs

# Currently The library supports 5 typed SpatialRDDs:
# <li> RectangleRDD </li>
# <li> PointRDD </li>
# <li> PolygonRDD </li>
# <li> LineStringRDD </li>
# <li> CircleRDD </li>

# In[41]:


rectangle_rdd = RectangleRDD(sc, "data/zcta510-small.csv", FileDataSplitter.CSV, True, 11)
point_rdd = PointRDD(sc, "data/arealm-small.csv", 1, FileDataSplitter.CSV, False, 11)
polygon_rdd = PolygonRDD(sc, "data/primaryroads-polygon.csv", FileDataSplitter.CSV, True, 11)
linestring_rdd = LineStringRDD(sc, "data/primaryroads-linestring.csv", FileDataSplitter.CSV, True)


# In[42]:


rectangle_rdd.analyze()
point_rdd.analyze()
polygon_rdd.analyze()
linestring_rdd.analyze()


# # Spatial Partitioning

# Apache Sedona spatial partitioning method can significantly speed up the join query. Three spatial partitioning methods are available: KDB-Tree, Quad-Tree and R-Tree. Two SpatialRDD must be partitioned by the same way.

# In[43]:


point_rdd.spatialPartitioning(GridType.KDBTREE)


# # Create Index

# Apache Sedona provides two types of spatial indexes, Quad-Tree and R-Tree. Once you specify an index type, Apache Sedona will build a local tree index on each of the SpatialRDD partition.

# In[44]:


point_rdd.buildIndex(IndexType.RTREE, True)


# # SpatialJoin

# Spatial join is operation which combines data based on spatial relations like:
# <li> intersects </li>
# <li> touches </li>
# <li> within </li>
# <li> etc </li>
# 
# To Use Spatial Join in GeoPyspark library please use JoinQuery object, which has implemented below methods:
# ```python
# SpatialJoinQuery(spatialRDD: SpatialRDD, queryRDD: SpatialRDD, useIndex: bool, considerBoundaryIntersection: bool) -> RDD
# 
# DistanceJoinQuery(spatialRDD: SpatialRDD, queryRDD: SpatialRDD, useIndex: bool, considerBoundaryIntersection: bool) -> RDD
# 
# spatialJoin(queryWindowRDD: SpatialRDD, objectRDD: SpatialRDD, joinParams: JoinParams) -> RDD
# 
# DistanceJoinQueryFlat(spatialRDD: SpatialRDD, queryRDD: SpatialRDD, useIndex: bool, considerBoundaryIntersection: bool) -> RDD
# 
# SpatialJoinQueryFlat(spatialRDD: SpatialRDD, queryRDD: SpatialRDD, useIndex: bool, considerBoundaryIntersection: bool) -> RDD
# 
# ```

# ## Example SpatialJoinQueryFlat PointRDD with RectangleRDD

# In[45]:


# partitioning the data
point_rdd.spatialPartitioning(GridType.KDBTREE)
rectangle_rdd.spatialPartitioning(point_rdd.getPartitioner())
# building an index
point_rdd.buildIndex(IndexType.RTREE, True)
# Perform Spatial Join Query
result = JoinQuery.SpatialJoinQueryFlat(point_rdd, rectangle_rdd, False, True)


# As result we will get RDD[GeoData, GeoData]
# It can be used like any other Python RDD. You can use map, take, collect and other functions  

# In[46]:


result


# In[47]:


result.take(2)


# In[48]:


result.collect()[:3]


# In[49]:


# getting distance using SpatialObjects
result.map(lambda x: x[0].geom.distance(x[1].geom)).take(5)


# In[50]:


# getting area of polygon data
result.map(lambda x: x[0].geom.area).take(5)


# In[51]:


# Base on result you can create DataFrame object, using map function and build DataFrame from RDD


# In[52]:


schema = StructType(
    [
        StructField("geom_left", GeometryType(), False),
        StructField("geom_right", GeometryType(), False)
    ]
)


# In[53]:


# Set verifySchema to False
spatial_join_result = result.map(lambda x: [x[0].geom, x[1].geom])
sedona.createDataFrame(spatial_join_result, schema, verifySchema=False).show(5, True)


# In[54]:


# Above code produces DataFrame with geometry Data type


# In[55]:


sedona.createDataFrame(spatial_join_result, schema, verifySchema=False).printSchema()


# We can create DataFrame object from Spatial Pair RDD using Adapter object as follows

# In[56]:


Adapter.toDf(result, ["attr1"], ["attr2"], sedona).show(5, True)


# This also produce DataFrame with geometry DataType

# In[57]:


Adapter.toDf(result, ["attr1"], ["attr2"], sedona).printSchema()


# We can create RDD which will be of type RDD[GeoData, List[GeoData]]
# We can for example calculate number of Points within some polygon data

# To do that we can use code specified below

# In[58]:


point_rdd.spatialPartitioning(GridType.KDBTREE)
rectangle_rdd.spatialPartitioning(point_rdd.getPartitioner())


# In[59]:


spatial_join_result_non_flat = JoinQuery.SpatialJoinQuery(point_rdd, rectangle_rdd, False, True)


# In[60]:


# number of point for each polygon
number_of_points = spatial_join_result_non_flat.map(lambda x: [x[0].geom, x[1].__len__()])


# In[61]:


schema = StructType([
    StructField("geometry", GeometryType(), False),
    StructField("number_of_points", LongType(), False)
])


# In[62]:


sedona.createDataFrame(number_of_points, schema, verifySchema=False).show()


# # KNNQuery

# Spatial KNNQuery is operation which help us find answer which k number of geometries lays closest to other geometry.
# 
# For Example:
#     5 closest Shops to your home. To use Spatial KNNQuery please use object
# <b> KNNQuery </b> which has one method:
# ```python
# SpatialKnnQuery(spatialRDD: SpatialRDD, originalQueryPoint: BaseGeometry, k: int,  useIndex: bool)-> List[GeoData]
# ```

# ### Finds 5 closest points from PointRDD to given Point

# In[63]:


result = KNNQuery.SpatialKnnQuery(point_rdd, Point(-84.01, 34.01), 5, False)


# In[64]:


result


# As Reference geometry you can also use Polygon or LineString object

# In[65]:


polygon = Polygon(
    [(-84.237756, 33.904859), (-84.237756, 34.090426),
     (-83.833011, 34.090426), (-83.833011, 33.904859),
     (-84.237756, 33.904859)
    ])
polygons_nearby = KNNQuery.SpatialKnnQuery(polygon_rdd, polygon, 5, False)


# In[66]:


polygons_nearby


# In[67]:


polygons_nearby[0].geom.wkt


# # RangeQuery

# A spatial range query takes as input a range query window and an SpatialRDD and returns all geometries that intersect / are fully covered by the query window.
# RangeQuery has one method:
# 
# ```python
# SpatialRangeQuery(self, spatialRDD: SpatialRDD, rangeQueryWindow: BaseGeometry, considerBoundaryIntersection: bool, usingIndex: bool) -> RDD
# ```

# In[68]:


from sedona.core.geom.envelope import Envelope


# In[69]:


query_envelope = Envelope(-85.01, -60.01, 34.01, 50.01)

result_range_query = RangeQuery.SpatialRangeQuery(linestring_rdd, query_envelope, False, False)


# In[70]:


result_range_query


# In[71]:


result_range_query.take(6)


# In[72]:


# Creating DataFrame from result


# In[73]:


schema = StructType([StructField("geometry", GeometryType(), False)])


# In[74]:


sedona.createDataFrame(
    result_range_query.map(lambda x: [x.geom]),
    schema,
    verifySchema=False
).show(5, True)


# # Load From other Formats

# GeoPyspark allows to load the data from other Data formats like:
# <li> GeoJSON </li>
# <li> Shapefile </li>
# <li> WKB </li>
# <li> WKT </li>

# In[75]:


## ShapeFile - load to SpatialRDD


# In[76]:


shape_rdd = ShapefileReader.readToGeometryRDD(sc, "data/polygon")


# In[77]:


shape_rdd


# In[78]:


Adapter.toDf(shape_rdd, sedona).show(5, True)


# In[79]:


## GeoJSON - load to SpatialRDD


# ```
# { "type": "Feature", "properties": { "STATEFP": "01", "COUNTYFP": "077", "TRACTCE": "011501", "BLKGRPCE": "5", "AFFGEOID": "1500000US010770115015", "GEOID": "010770115015", "NAME": "5", "LSAD": "BG", "ALAND": 6844991, "AWATER": 32636 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ -87.621765, 34.873444 ], [ -87.617535, 34.873369 ], [ -87.6123, 34.873337 ], [ -87.604049, 34.873303 ], [ -87.604033, 34.872316 ], [ -87.60415, 34.867502 ], [ -87.604218, 34.865687 ], [ -87.604409, 34.858537 ], [ -87.604018, 34.851336 ], [ -87.603716, 34.844829 ], [ -87.603696, 34.844307 ], [ -87.603673, 34.841884 ], [ -87.60372, 34.841003 ], [ -87.603879, 34.838423 ], [ -87.603888, 34.837682 ], [ -87.603889, 34.83763 ], [ -87.613127, 34.833938 ], [ -87.616451, 34.832699 ], [ -87.621041, 34.831431 ], [ -87.621056, 34.831526 ], [ -87.62112, 34.831925 ], [ -87.621603, 34.8352 ], [ -87.62158, 34.836087 ], [ -87.621383, 34.84329 ], [ -87.621359, 34.844438 ], [ -87.62129, 34.846387 ], [ -87.62119, 34.85053 ], [ -87.62144, 34.865379 ], [ -87.621765, 34.873444 ] ] ] } },
# ```

# In[80]:


geo_json_rdd = GeoJsonReader.readToGeometryRDD(sc, "data/testPolygon.json")


# In[81]:


geo_json_rdd


# In[82]:


Adapter.toDf(geo_json_rdd, sedona).drop("AWATER").show(5, True)


# In[83]:


## WKT - loading to SpatialRDD


# In[84]:


wkt_rdd = WktReader.readToGeometryRDD(sc, "data/county_small.tsv", 0, True, False)


# In[85]:


wkt_rdd


# In[86]:


Adapter.toDf(wkt_rdd, sedona).printSchema()


# In[87]:


Adapter.toDf(wkt_rdd, sedona).show(5, True)


# In[88]:


## WKB - load to SpatialRDD


# In[89]:


wkb_rdd = WkbReader.readToGeometryRDD(sc, "data/county_small_wkb.tsv", 0, True, False)


# In[90]:


Adapter.toDf(wkb_rdd, sedona).show(5, True)


# ## Converting RDD Spatial join result to DF directly, avoiding jvm python serde

# In[91]:


point_rdd.spatialPartitioning(GridType.KDBTREE)
rectangle_rdd.spatialPartitioning(point_rdd.getPartitioner())
# building an index
point_rdd.buildIndex(IndexType.RTREE, True)
# Perform Spatial Join Query
result = JoinQueryRaw.SpatialJoinQueryFlat(point_rdd, rectangle_rdd, False, True)


# In[92]:


# without passing column names, the result will contain only two geometries columns
geometry_df = Adapter.toDf(result, sedona)


# In[93]:


geometry_df.printSchema()


# In[94]:


geometry_df.show(5)


# In[95]:


geometry_df.collect()[0]


# ## Passing column names

# In[96]:


geometry_df = Adapter.toDf(result, ["left_user_data"], ["right_user_data"], sedona)


# In[97]:


geometry_df.show(5)


# # Converting RDD Spatial join result to DF directly, avoiding jvm python serde

# In[98]:


query_envelope = Envelope(-85.01, -60.01, 34.01, 50.01)

result_range_query = RangeQueryRaw.SpatialRangeQuery(linestring_rdd, query_envelope, False, False)


# In[99]:


# converting to df
gdf = Adapter.toDf(result_range_query, sedona)


# In[100]:


gdf.show(5)


# In[101]:


gdf.printSchema()


# In[102]:


# Passing column names
# converting to df
gdf_with_columns = Adapter.toDf(result_range_query, sedona, ["_c1"])


# In[103]:


gdf_with_columns.show(5)


# In[104]:


gdf_with_columns.printSchema()


# # Summary
# 
# We have shown how to install Sedona with Pyspark and run a basic example (source: https://github.com/apache/sedona/blob/master/binder/ApacheSedonaCore.ipynb) on Google Colab.

# This file was generated from MapReduce_Primer_HelloWorld_bash.ipynb with nbconvert
# Source: https://github.com/groda/big_data

 #!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/groda/big_data/blob/master/MapReduce_Primer_HelloWorld_bash.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <a href="https://github.com/groda/big_data"><div><img src="https://github.com/groda/big_data/blob/master/logo_bdb.png?raw=true" align=right width="90"></div></a>
# 
# # MapReduce: A Primer with <code>Hello World!</code> in bash
# <br>
# <br>
# 
# This tutorial serves as a companion to [MapReduce_Primer_HelloWorld.ipynb](https://github.com/groda/big_data/blob/master/MapReduce_Primer_HelloWorld.ipynb), with the implementation carried out in the Bash scripting language requiring only a few lines of code.
# 
# For this tutorial, we are going to download the core Hadoop distribution and run Hadoop in _local standalone mode_:
# 
# > ❝ _By default, Hadoop is configured to run in a non-distributed mode, as a single Java process._ ❞
# 
# (see [https://hadoop.apache.org/docs/stable/.../Standalone_Operation](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Standalone_Operation))
# 
# We are going to run a MapReduce job using MapReduce's [streaming application](https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html#Hadoop_Streaming). This is not to be confused with real-time streaming:
# 
# > ❝ _Hadoop streaming is a utility that comes with the Hadoop distribution. The utility allows you to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer._ ❞
# 
# MapReduce streaming defaults to using [`IdentityMapper`](https://hadoop.apache.org/docs/stable/api/index.html) and [`IdentityReducer`](https://hadoop.apache.org/docs/stable/api/index.html), thus eliminating the need for explicit specification of a mapper or reducer.
# 
# Both input and output are standard files since Hadoop's default filesystem is the regular file system, as specified by the `fs.defaultFS` property in [core-default.xml](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/core-default.xml)).
# 

# In[18]:


get_ipython().run_cell_magic('bash', '', 'HADOOP_URL="https://dlcdn.apache.org/hadoop/common/stable/hadoop-3.3.6.tar.gz"
wget --quiet --no-clobber $HADOOP_URL >/dev/null
[ ! -d $(basename $HADOOP_URL .tar.gz) ] && tar -xzf $(basename $HADOOP_URL)
HADOOP_HOME=$(pwd)\'/\'$(basename $HADOOP_URL .tar.gz)\'/bin\'
PATH=$HADOOP_HOME:$PATH
which java >/dev/null|| apt install -y openjdk-19-jre-headless
export JAVA_HOME=$(realpath $(which java) | sed \'s/\/bin\/java$//\')
echo -e "Hello, World!">hello.txt
output_dir="output"$(date +"%Y%m%dT%H%M")
mapred streaming -input hello.txt -output output_dir >log 2>&1
cat output_dir/part-00000
')

# This file was generated from MapReduce_Primer_HelloWorld with nbconvert
# Source: https://github.com/groda/big_data

 #!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/groda/big_data/blob/master/MapReduce_Primer_HelloWorld.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <a href="https://github.com/groda/big_data"><div><img src="https://github.com/groda/big_data/blob/master/logo_bdb.png?raw=true" align=right width="90"></div></a>
# 
# # MapReduce: A Primer with <code>Hello World!</code>
# <br>
# <br>
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
# MapReduce streaming defaults to using `IdentityMapper` `IdentityReducer`, thus eliminating the need for explicit specification of a mapper or reducer. Finally, we show how to run a map-only job by setting `mapreduce.job.reduce` equal to $0$.
# 

# # Download core Hadoop

# In[1]:


HADOOP_URL = "https://dlcdn.apache.org/hadoop/common/stable/hadoop-3.3.6.tar.gz"

import requests
import os
import tarfile

def download_and_extract_targz(url):
    response = requests.get(url)
    filename = url.rsplit('/', 1)[-1]
    HADOOP_HOME = filename[:-7]
    # set HADOOP_HOME environment variable
    os.environ['HADOOP_HOME'] = HADOOP_HOME
    if os.path.isdir(HADOOP_HOME):
      print("Not downloading, Hadoop folder {} already exists".format(HADOOP_HOME))
      return
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        with tarfile.open(filename, 'r:gz') as tar_ref:
            extract_path = tar_ref.extractall(path='.')
            # Get the names of all members (files and directories) in the archive
            all_members = tar_ref.getnames()
            # If there is a top-level directory, get its name
            if all_members:
              top_level_directory = all_members[0]
              print(f"ZIP file downloaded and extracted successfully. Contents saved at: {top_level_directory}")
    else:
        print(f"Failed to download ZIP file. Status code: {response.status_code}")


download_and_extract_targz(HADOOP_URL)


# # Set environment variables

# ## Set `HADOOP_HOME` and `PATH`

# In[2]:


# HADOOP_HOME was set earlier when downloading Hadoop distribution
print("HADOOP_HOME is {}".format(os.environ['HADOOP_HOME']))

os.environ['PATH'] = ':'.join([os.path.join(os.environ['HADOOP_HOME'], 'bin'), os.environ['PATH']])
print("PATH is {}".format(os.environ['PATH']))


# ## Set `JAVA_HOME`
# 
# While Java is readily available on Google Colab, we consider the broader scenario of an Ubuntu machine. In this case, we ensure compatibility by installing Java, specifically opting for the `openjdk-19-jre-headless` version.

# In[3]:


import shutil

# set variable JAVA_HOME (install Java if necessary)
def is_java_installed():
    os.environ['JAVA_HOME'] = os.path.realpath(shutil.which("java")).split('/bin')[0]
    return os.environ['JAVA_HOME']

def install_java():
    # Uncomment and modify the desired version
    # java_version= 'openjdk-11-jre-headless'
    # java_version= 'default-jre'
    # java_version= 'openjdk-17-jre-headless'
    # java_version= 'openjdk-18-jre-headless'
    java_version= 'openjdk-19-jre-headless'

    print(f"Java not found. Installing {java_version} ... (this might take a while)")
    try:
        cmd = f"apt install -y {java_version}"
        subprocess_output = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        stdout_result = subprocess_output.stdout
        # Process the results as needed
        print("Done installing Java {}".format(java_version))
        os.environ['JAVA_HOME'] = os.path.realpath(shutil.which("java")).split('/bin')[0]
        print("JAVA_HOME is {}".format(os.environ['JAVA_HOME']))
    except subprocess.CalledProcessError as e:
        # Handle the error if the command returns a non-zero exit code
        print("Command failed with return code {}".format(e.returncode))
        print("stdout: {}".format(e.stdout))

# Install Java if not available
if is_java_installed():
    print("Java is already installed: {}".format(os.environ['JAVA_HOME']))
else:
    print("Installing Java")
    install_java()


# # Run a MapReduce job with Hadoop streaming

# ## Create a file
# 
# Write the string"Hello, World!" to a local file.<p>**Note:** you will be writing to the file `./hello.txt` in your current directory (denoted by `./`).

# In[4]:


get_ipython().system('echo "Hello, World!">./hello.txt')


# ## Launch the MapReduce "Hello, World!" application
# 
# Since the default filesystem is the local filesystem (as opposed to HDFS) we do not need to upload the local file `hello.txt` to HDFS.
# 
# Run a MapReduce job with `/bin/cat` as a mapper and no reducer.
# 
# **Note:** the first step of removing the output directory is necessary because MapReduce does not overwrite data folders by design.

# In[5]:


get_ipython().run_cell_magic('bash', '', "hdfs dfs -rm -r my_output

mapred streaming \
    -input hello.txt \
    -output my_output \
    -mapper '/bin/cat'
")


# ## Verify the result
# 
# If the job executed successfully, an empty file named `_SUCCESS` is expected to be present in the output directory `my_output`.
# 
# Verify the success of the MapReduce job by checking for the presence of the `_SUCCESS` file.

# In[6]:


get_ipython().run_cell_magic('bash', '', '
echo "Check if MapReduce job was successful"
hdfs dfs -test -e my_output/_SUCCESS
if [ $? -eq 0 ]; then
	echo "_SUCCESS exists!"
fi
')


# **Note:** `hdfs dfs -ls` is the same as `ls` since the default filesystem is the local filesystem.

# In[7]:


get_ipython().system('hdfs dfs -ls my_output')


# In[8]:


get_ipython().system('ls -l my_output')


# The actual output of the MapReduce job is contained in the file `part-00000` in the output directory.

# In[9]:


get_ipython().system('cat my_output/part-00000')


# # MapReduce without specifying mapper or reducer
# 
# In the previous example, we have seen how to run a MapReduce job without specifying any reducer.
# 
# Since the only required options for `mapred streaming` are `input` and `output`, we can also run a MapReduce job without specifying a mapper.

# In[10]:


get_ipython().system('mapred streaming -h')


# In[11]:


get_ipython().run_cell_magic('bash', '', 'hdfs dfs -rm -r my_output

mapred streaming \
    -input hello.txt \
    -output my_output
')


# ## Verify the result

# In[12]:


get_ipython().run_cell_magic('bash', '', '
echo "Check if MapReduce job was successful"
hdfs dfs -test -e my_output/_SUCCESS
if [ $? -eq 0 ]; then
	echo "_SUCCESS exists!"
fi
')


# Show output

# In[13]:


get_ipython().system('cat my_output/part-00000')


# What happened here is that not having defined any mapper or reducer, the "Identity" mapper ([IdentityMapper](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/lib/IdentityMapper.html)) and reducer ([IdentityReducer](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/lib/IdentityReducer.html)) were used by default (see [Streaming command options](https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html#Streaming_Command_Options)).

# # Run a map-only MapReduce job
# 
# Not specifying mapper and reducer in the MapReduce job submission does not mean that MapReduce isn't going to run the mapper and reducer steps, it is simply going to use the Identity mapper and reducer.
# 
# To run a MapReduce job _without_ reducer one needs to use the generic option
# 
#     \-D mapreduce.job.reduces=0
# 
# (see [specifying map-only jobs](https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html#Specifying_Map-Only_Jobs)).

# In[14]:


get_ipython().run_cell_magic('bash', '', 'hdfs dfs -rm -r my_output

mapred streaming \
    -D mapreduce.job.reduces=0 \
    -input hello.txt \
    -output my_output
')


# ## Verify the result

# In[15]:


get_ipython().system('hdfs dfs -test -e my_output/_SUCCESS && cat my_output/part-00000')


# ## Why a map-only application?
# 
# The advantage of a map-only job is that the sorting and shuffling phases are skipped, so if you do not need that remember to specify `-D mapreduce.job.reduces=0 `.
# 
# On the other hand, a MapReduce job even with the default `IdentityReducer` will deliver sorted results because the data passed from the mapper to the reducer always gets sorted.
# 

# # Improved version of the MapReduce "Hello, World!" application
# 
# Taking into account the previous considerations, here's a more efficient version of the 'Hello, World!' application that bypasses the shuffling and sorting step.

# In[16]:


get_ipython().run_cell_magic('bash', '', "hdfs dfs -rm -r my_output

mapred streaming \
    -D mapreduce.job.reduces=0 \
    -input hello.txt \
    -output my_output \
    -mapper '/bin/cat'
")


# In[17]:


get_ipython().system('hdfs dfs -test -e my_output/_SUCCESS && cat my_output/part-00000')

# This file was generated from Hadoop_Setting_up_a_Single_Node_Cluster.ipynb with nbconvert
# Source: https://github.com/groda/big_data

 #!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/groda/big_data/blob/master/Hadoop_Setting_up_a_Single_Node_Cluster.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <a href="https://github.com/groda/big_data"><div><img src="https://github.com/groda/big_data/blob/master/logo_bdb.png?raw=true" align=right width="90"></div></a>
# 
# # HDFS and MapReduce on a single-node Hadoop cluster
# <br>
# <br>
# 
# In this tutorial/notebook we'll showcase the setup of a single-node cluster, following the guidelines outlined on https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html. Subsequently, we'll demonstrate the seamless execution of elementary HDFS and MapReduce commands.
# 
# Upon downloading the software, several preliminary steps must be taken, including setting environment variables, generating SSH keys, and more. To streamline these tasks, we've consolidated them under the "Prologue" section.
# 
# Upon completion of the prologue, we can launch a single-node Hadoop cluster on the current virtual machine.
# 
# Following that, we'll execute a series of test HDFS commands and MapReduce jobs on the Hadoop cluster. These will be performed using a dataset sourced from a publicly available collection.
# 
# Finally, we'll proceed to shut down the cluster.
# 

# **TABLE OF CONTENTS**
# * **[Prologue](#scrollTo=oUuQjW2oNMcJ)**
# 
#  * [Check the available Java version](#scrollTo=qFfOrktMPq8M)
# 
#  * [Download core Hadoop](#scrollTo=KE7kSYSXQYLf)
# 
#    * [Verify the downloaded file](#scrollTo=lGI4TNXPamMr)
# 
#  * [Configure `PATH`](#scrollTo=RlgP1ytnRtUK)
# 
#  * [Configure `core-site.xml` and `hdfs-site.xml`](#scrollTo=KLmxLQeJSb4A)
# 
#  * [Set environment variables](#scrollTo=kXbSKFyeMqr2)
# 
#  * [Setup localhost access via SSH key](#scrollTo=k2-Fdp73cF0V)
# 
#    * [Install `openssh` and start server](#scrollTo=-Uxmv3RdUwiF)
# 
#    * [Generate key](#scrollTo=PYKoSlaENuyG)
# 
#    * [Check SSH connection to localhost](#scrollTo=FwA6rKpScnVi)
# 
# * **[Launch a single-node Hadoop cluster](#scrollTo=V68C4cDySyek)**
# 
#    * [Initialize the namenode](#scrollTo=HTDPwnVlSbHS)
# 
#    * [Start cluster](#scrollTo=xMrEiLB_VAeR)
# 
# * **[Run some simple HDFS commands](#scrollTo=CKRRbwDFv3ZQ)**
# 
# * **[Run some simple MapReduce jobs](#scrollTo=G3KBe4R65bl1)**
# 
#    * [Simplest MapReduce job](#scrollTo=yVJA-3jSATGV)
# 
#    * [Another MapReduce example: filter a log file](#scrollTo=BbosNo0TD3oH)
# 
#    * [Aggregate data with MapReduce](#scrollTo=Sam22f-YT1xR)
# 
# * **[Stop cluster](#scrollTo=IF6-Z5RotAcO)**
# 
# * **[Concluding remarks](#scrollTo=w5N7tb0HSbZB)**
# 
# 

# # Prologue

# ## Check the available Java version
#  Apache Hadoop 3.3 and upper supports Java 8 and Java 11 (runtime only). See: https://cwiki.apache.org/confluence/display/HADOOP/Hadoop+Java+Versions
# 

# Check if Java version is one of `8`, `11`

# In[ ]:


get_ipython().system('java -version')


# In[ ]:


get_ipython().run_cell_magic('bash', '', 'JAVA_MAJOR_VERSION=$(java -version 2>&1 | grep -m1 -Po \'(\d+\.)+\d+\' | cut -d \'.\' -f1)
if [[ $JAVA_MAJOR_VERSION -eq 8 || $JAVA_MAJOR_VERSION -eq 11 ]]
 then
 echo "Java version is one of 8, 11 ✓"
 fi
')


# Find the variable for the environment variable `JAVA_HOME`

# Find the path for the environment variable `JAVA_HOME`

# In[ ]:


get_ipython().system('readlink -f $(which java)')


# Extract JAVA_HOME from the Java path by removing the `bin/java` part in the end

# In[ ]:


get_ipython().run_cell_magic('bash', '', "JAVA_HOME=$(readlink -f $(which java) | sed 's/\/bin\/java$//')
echo $JAVA_HOME
")


# ## Download core Hadoop
# Download the latest stable version of the core Hadoop distribution from one of the download mirrors locations https://www.apache.org/dyn/closer.cgi/hadoop/common/.
# 
# **Note** with the option `--no-clobber`, `wget` will not download the file if it already exists.

# In[ ]:


get_ipython().system('wget --no-clobber https://dlcdn.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz')


# Uncompress archive

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'if [ ! -d "hadoop-3.4.0" ]; then
  tar xzf hadoop-3.4.0.tar.gz
fi
')


# ### Verify the downloaded file
# 
# (see https://www.apache.org/dyn/closer.cgi/hadoop/common/)

# Download sha512 file

# In[ ]:


get_ipython().system(' wget --no-clobber https://dlcdn.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz.sha512')


# Compare

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'A=$(sha512sum hadoop-3.4.0.tar.gz | cut - -d\' \' -f1)
B=$(cut hadoop-3.4.0.tar.gz.sha512 -d\' \' -f4)
printf "%s\n%s\n" $A $B
[[ $A == $B ]] && echo "True"
')


# ## Configure `PATH`
# 
# Add the Hadoop folder to the `PATH` environment variable
# 

# In[ ]:


get_ipython().system('echo $PATH')


# In[ ]:


import os
os.environ['HADOOP_HOME'] = os.path.join(os.getcwd(), 'hadoop-3.4.0')
os.environ['PATH'] = ':'.join([os.path.join(os.environ['HADOOP_HOME'], 'bin'), os.environ['PATH']])
#os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'


# In[ ]:


import os
print(os.environ)


# In[ ]:


get_ipython().system('echo $PATH')


# ## Configure `core-site.xml` and `hdfs-site.xml`
# 
# Edit the file `etc/hadoop/core-site.xml` and `etc/hadoop/hdfs-site.xml` to configure pseudo-distributed operation.
# 
# **`etc/hadoop/core-site.xml`**
# ```
# <configuration>
#     <property>
#         <name>fs.defaultFS</name>
#         <value>hdfs://localhost:9000</value>
#     </property>
# </configuration>
# ```
# 
# **`etc/hadoop/hdfs-site.xml`**
# ```
# <configuration>
#     <property>
#         <name>dfs.replication</name>
#         <value>1</value>
#     </property>
# </configuration>
# ```

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'echo -e "<configuration> \n\
    <property> \n\
        <name>fs.defaultFS</name> \n\
        <value>hdfs://localhost:9000</value> \n\
    </property> \n\
</configuration>" >hadoop-3.4.0/etc/hadoop/core-site.xml

echo -e "<configuration> \n\
    <property> \n\
        <name>dfs.replication</name> \n\
        <value>1</value> \n\
    </property> \n\
</configuration>" >hadoop-3.4.0/etc/hadoop/hdfs-site.xml
')


# Check

# In[ ]:


cat hadoop-3.4.0/etc/hadoop/hdfs-site.xml


# ## Set environment variables
# 
# Add the following lines to the Hadoop configuration script `hadoop-env.sh`(the script is in `hadoop-3.4.0/sbin`).
# ```
# export HDFS_NAMENODE_USER=root
# export HDFS_DATANODE_USER=root
# export HDFS_SECONDARYNAMENODE_USER=root
# export YARN_RESOURCEMANAGER_USER=root
# export YARN_NODEMANAGER_USER=root
# ```

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'cp -n hadoop-3.4.0/etc/hadoop/hadoop-env.sh hadoop-3.4.0/etc/hadoop/hadoop-env.sh.org
cat <<😃 >hadoop-3.4.0/etc/hadoop/hadoop-env.sh
export HDFS_NAMENODE_USER=root
export HDFS_DATANODE_USER=root
export HDFS_SECONDARYNAMENODE_USER=root
export YARN_RESOURCEMANAGER_USER=root
export YARN_NODEMANAGER_USER=root
😃
')


# ## Setup localhost access via SSH key
# 
# We are going to allow passphraseless access to `localhost` with a secure key.
# 
# SSH must be installed and sshd must be running in order to use the Hadoop scripts that manage remote Hadoop daemons.
# 

# 
# ### Install `openssh` and start server
# 
# I'm not sure why we need the option `StrictHostKeyChecking no`. This option tells the `ssh` server to allow key authentication only from known hosts, in particular it prevents a host from authenticating with key if the key has changed. I guess this option is needed since a new ssh key is generated every time one runs this notebook.
# 
# Alternatively, one could just delete the file `~/.ssh/known_hosts` or else use `ssh-keygen -R hostname` to remove all keys belonging to hostname from the `known_hosts` file (see for instance [How to remove strict RSA key checking in SSH and what's the problem here?](https://serverfault.com/questions/6233/how-to-remove-strict-rsa-key-checking-in-ssh-and-whats-the-problem-here) or [Remove key from known_hosts](https://superuser.com/questions/30087/remove-key-from-known-hosts)). The option `ssh-keygen -R hostname` would be the most appropriate in a production setting where the file `~/.ssh/known_hosts` might contain other entries that you do not want to delete.
# 

# In[ ]:


get_ipython().run_cell_magic('bash', '', "apt-get update
apt-get -y install openssh-server
echo 'StrictHostKeyChecking no' >> /etc/ssh/ssh_config
/etc/init.d/ssh restart
")


# ### Generate key
# Generate an SSH key that does not require a password.
# 
# The private key is contained in the file `id_rsa` located in the folder `~/.ssh`.
# 
# The public key is added to the file `~/.ssh/authorized_keys` in order to allow authentication with that key.

# In[ ]:


get_ipython().run_cell_magic('bash', '', "rm $HOME/.ssh/id_rsa
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
")


# ### Check SSH connection to localhost
# 
# The following command should output "hi!" if the connection works.

# In[ ]:


get_ipython().system('ssh localhost "echo hi 👋"')


# # Launch a single-node Hadoop cluster

# ## Initialize the namenode

# In[ ]:


get_ipython().system('hdfs namenode -format -nonInteractive')


# ## Start cluster

# In[ ]:


get_ipython().system('$HADOOP_HOME/sbin/start-dfs.sh')


# In[ ]:


get_ipython().run_cell_magic('bash', '', '# Check if HDFS is in safe mode
if hdfs dfsadmin -safemode get | grep \'ON\'; then
  echo "Namenode is in safe mode. Leaving safe mode..."
  hdfs dfsadmin -safemode leave
else
  echo "Namenode is not in safe mode."
fi
')


# # Run some simple HDFS commands

# In[ ]:


get_ipython().run_cell_magic('bash', '', '# create directory "my_dir" in HDFS home
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/root # this is the "home" of user root on HDFS
hdfs dfs -mkdir my_dir

# if sampls_data does not exist, create it (so that the notebook can run also outside of Colab)
mkdir -p sample_data
touch sample_data/mnist_test.csv

# Check if the file is empty and fill it if needed
if [ ! -s sample_data/mnist_test.csv ]; then
  echo -e "0 1 2 3 4\n5 6 7 8 9" > sample_data/mnist_test.csv
fi


# upload file mnist_test.csv to my_dir
hdfs dfs -put sample_data/mnist_test.csv my_dir/

# show contents of directory my_dir
hdfs dfs -ls -h my_dir
')


# # Run some simple MapReduce jobs
# 
# We'll employ the [streaming](https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html) library, which broadens our options by enabling the use of any programming language for both the mapper and/or the reducer.
# 
# With this utility any executable or file containing code that the operating system can interpret and execute directly, can serve as mapper and/or reducer.

# ## Simplest MapReduce job
# 
# This is a "no-code" example since we are going to use the existing Unix commands `cat` and `wc` respectively as mapper and as reducer. The result will show a line with three values: the counts of lines, words, and characters in the input file(s).
# 
# Input folder is `/user/my_user/my_dir/`, output folder `/user/my_user/output_simplest`.
# 
# **Note**: the output folder should not exist because it is created by Hadoop (this is in accordance with Hadoop's principle of not overwriting data).

# Now run the MapReduce job

# In[ ]:


get_ipython().run_cell_magic('bash', '', '
hdfs dfs -rm -r output_simplest || hdfs namenode -format -nonInteractive
mapred streaming \
  -input my_dir \
  -output output_simplest \
  -mapper /bin/cat \
  -reducer /usr/bin/wc
')


# If the `output` directory contains the empty file `_SUCCESS`, this means that the job was successful.

# Check the output of the MapReduce job.

# In[ ]:


get_ipython().system('hdfs dfs -cat output_simplest/part-00000')


# The number of words is in this case equal to the number of lines because there are no word separators (empty spaces) in the file, so each line is a word.

# ## Another MapReduce example: filter a log file
# 
# We're going to use a Linux logfile and look for the string `sshd` in a given position. The file stems from [Loghub](https://github.com/logpai/loghub), a freely available collection of system logs for AI-driven log analytics research.
# 
# The mapper `mapper.py` filters the file for the given string `sshd` at field 4.
# 
# The job has no reducer (option `-reducer NONE`). Note that without a reducer the sorting and shuffling phase after the map phase is skipped.
# 

# Download the logfile `Linux_2k.log`:

# In[ ]:


get_ipython().system('wget --no-clobber https://raw.githubusercontent.com/logpai/loghub/master/Linux/Linux_2k.log')


# In[ ]:


get_ipython().run_cell_magic('bash', '', 'hdfs dfs -mkdir input || true
hdfs dfs -put Linux_2k.log input/ || true
')


# Define the mapper

# In[ ]:


get_ipython().run_cell_magic('writefile', 'mapper.py', "#!/usr/bin/env python
import sys

for line in sys.stdin:
    # split the line into words
    line = line.strip()
    fields = line.split()
    if (len(fields)>=5 and fields[4].startswith('sshd')):
      print(line)
")


# Test the script (after setting the correct permissions)

# In[ ]:


get_ipython().system('chmod 700 mapper.py')


# Look at the first 10 lines

# In[ ]:


get_ipython().system('head -10 Linux_2k.log')


# Test the mapper in the shell (not using MapReduce):

# In[ ]:


get_ipython().system('head -100 Linux_2k.log| ./mapper.py')


# Now run the MapReduce job on the pseudo-cluster

# In[ ]:


get_ipython().run_cell_magic('bash', '', '
hdfs dfs -rm -r output_filter

mapred streaming \
  -file mapper.py \
  -input input \
  -output output_filter \
  -mapper mapper.py \
  -reducer NONE
')


# Check the result

# In[ ]:


get_ipython().system('hdfs dfs -ls output_filter')


# In[ ]:


get_ipython().system('hdfs dfs -cat output_filter/part-00000 |head')


# ## Aggregate data with MapReduce
# 
# Following the example in [Hadoop Streaming/Aggregate package](https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html#Hadoop_Aggregate_Package)

# In[12]:


get_ipython().run_cell_magic('writefile', 'myAggregatorForKeyCount.py', '#!/usr/bin/env python
import sys

def generateLongCountToken(id):
    return "LongValueSum:" + id + "\t" + "1"

def main(argv):
    line = sys.stdin.readline()
    try:
        while line:
            line = line[:-1]
            fields = line.split()
            s = fields[4].split(\'[\')[0]
            print(generateLongCountToken(s))
            line = sys.stdin.readline()
    except "end of file":
        return None

if __name__ == "__main__":
     main(sys.argv)
')


# Set permissions

# In[ ]:


get_ipython().system('chmod 700 myAggregatorForKeyCount.py')


# Test the mapper

# In[ ]:


get_ipython().system('head -20 Linux_2k.log| ./myAggregatorForKeyCount.py')


# Run the MapReduce job

# In[ ]:


get_ipython().run_cell_magic('bash', '', '
chmod +x myAggregatorForKeyCount.py

hdfs dfs -rm -r output_aggregate

mapred streaming \
  -input input \
  -output output_aggregate \
  -mapper myAggregatorForKeyCount.py \
  -reducer aggregate \
  -file myAggregatorForKeyCount.py
')


# Check result

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'hdfs dfs -ls output_aggregate
hdfs dfs -cat output_aggregate/part-00000
')


# Pretty-print table of aggregated data

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'hdfs dfs -get output_aggregate/part-00000 result # download results file
# Use awk to format the output into columns and then sort by the second field numerically in descending order
awk \'{printf "%-20s %s\n", $1, $2}\' result | sort -k2nr
')


# # Stop cluster
# 
# When you're done with your computations, you can shut down the Hadoop cluster and stop the `sshd` service.

# In[ ]:


get_ipython().system('./hadoop-3.4.0/sbin/stop-dfs.sh')


# Stop the `sshd` daemon

# In[ ]:


get_ipython().system('/etc/init.d/ssh stop')


# # Concluding remarks
# 
# We have started a single-node Hadoop cluster and ran some simple HDFS and MapReduce commands.
# 
# Even when running on a single machine, one can benefit from the parallelism provided by multiple virtual cores.
# 
# Hadoop provides also a command-line utility (the CLI MiniCluster) to start and stop a single-node Hadoop cluster "_without the need to set any environment variables or manage configuration files_" (https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/CLIMiniCluster.html). The [Hadoop MiniCluster](https://github.com/groda/big_data/blob/master/Hadoop_minicluster.ipynb) notebook serves as a guide for launching the Hadoop MiniCluster.
# 
# While it can be useful to be able to start a Hadoop cluster with a single command, delving into the functionality of each component offers valuable insights into the intricacies of Hadoop architecture, thereby enriching the learning process.
# 
# If you found this notebook helpful, consider exploring:
#  - [Hadoop single-node cluster setup with Python](https://github.com/groda/big_data/blob/master/Hadoop_single_node_cluster_setup_Python.ipynb) similar to this but using Python in place of bash
#  - [Setting up Spark Standalone on Google Colab](https://github.com/groda/big_data/blob/master/Hadoop_Setting_up_Spark_Standalone_on_Google_Colab.ipynb)
#  - [Getting to know the Spark Standalone Architecture](https://github.com/groda/big_data/blob/master/Spark_Standalone_Architecture_on_Google_Colab.ipynb)
# 
# 
# 

# In[ ]:

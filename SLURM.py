# This file was generated from SLURM.ipynb with nbconvert
# Source: https://github.com/groda/big_data

 #!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/groda/big_data/blob/master/SLURM.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <a href="https://github.com/groda/big_data"><div><img src="https://github.com/groda/big_data/blob/master/logo_bdb.png?raw=true" align=right width="90" alt="Logo Big Data for Beginners"></div></a>
# # SLURM Demonstration: Unleashing Parallel Computing
# 
# <div width="110"><img src="https://github.com/groda/big_data/blob/master/Slurm_logo.svg.png?raw=true" align=left width="90" style="margin:30px" alt="SLURM logo"/></div>
# 
# 
#  **SLURM** is an acronym for **S**imple **L**inux **U**tility for **R**esource **M**anagement. The name reflects its original design goal of being a straightforward yet powerful tool for managing Linux cluster resources.
# 
# This demonstration walks you through setting up, configuring, and using SLURM on a single Ubuntu virtual machine (VM), providing a hands-on introduction to its features for high-performance computing (HPC) environments.
# 
# We’ll explore how to set up and harness SLURM’s job scheduling capabilities, whether you’re using Google Colab’s cloud environment or your own virtual machine (VM). From submitting jobs to verifying parallel execution, you’ll learn to leverage SLURM for efficient computation—perfect for your single-node Docker setup or beyond.
# 
# To make navigation easier:
# - **🚀 Critical Steps**: Sections marked with the 🚀 emoji highlight essential tasks, such as installation and configuration, that are crucial for setting up and running SLURM. Follow these steps carefully to ensure a successful deployment.
# - **📝 Side Notes**: Sections marked with the 📝 emoji contain optional, supplementary information, such as historical context or additional tips. These can be skipped if you’re focused on the core setup process but are expandable for deeper insights.
# 
# Get ready to dive into the power of SLURM for parallel computing and supercharge your workflows!
# 
# 
# 
# 

# ## Table of Contents
# 
# - [🚀 Install the SLURM Packages](#scrollTo=2QpF7XoRzry7)
# - [📝 Side Note: What is slurm-wlm?](#scrollTo=brQkWtmMi786)
# - [📝 Side Note: A Brief History of SLURM](#scrollTo=31Q0HgWMK19o)
# - [📝 Side Note: Debian's sid and SLURM](#scrollTo=VFtQ9QQgj98S)
# - [📝 Side Note: Nerdy Names, Serious Systems](#scrollTo=_Side_Note_Nerdy_Names_Serious_Systems)
# - [🚀 Configuration](#scrollTo=BhhgV7kNYT7c)
# - [📝 Configure using slurm-wlm-configurator.html](#scrollTo=XhJQeLeT99Tz)
# - [🚀 Generate a `munge` key](#scrollTo=3d8C0ay3Xa-d)
# - [🚀 Create Spool Directories](#scrollTo=fgqo9xAZXxYS)
# - [🚀 Start the Services](#scrollTo=gFMWSBKBX7Yl)
# - [🚀 Verify Cluster Status](#scrollTo=92wZzJmSfK35)
# - [📝 Useful Commands for Debugging](#scrollTo=rNeusBTLcqve)
# - [🚀 Run a simple job](#scrollTo=Ua-nBgvmsJpA)
# - [🚀 Did the Job Run in Parallel?](#scrollTo=1DAjlH9ltWXj)
# - [🚀 Single-task parallel Python with `multiprocessing` and `--cpus-per-task`](#scrollTo=uH60mvkDzzFk)
# - [🚀 Run multiple tasks with `srun`](#scrollTo=Jnx75guCFmZk)
# - [🚀 SLURM Job Arrays](#scrollTo=H-QTevQSJjJM)
# 
# 

# ## 🚀 Install the SLURM Packages
# 
# This might take a few seconds ...
# <img src="data:image/gif;base64,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" alt="Running cat" />

# In[ ]:


get_ipython().system('apt install slurm-wlm -y')


# You can use the `scontrol version` command to find out the installed SLURM version.

# In[ ]:


get_ipython().system('scontrol version')


# ## 📝 Side Note: What is `slurm-wlm`?

# `slurm-wlm` is the Debian package for SLURM and it is an unofficial distribution from **SchedMD**'s perspective (SchedMD is the company that develops and maintains the open-source Slurm Workload Manager).
# 
# According to the [Slurm Quick Start Administrator Guide](https://slurm.schedmd.com/quickstart_admin.html#quick_start), SchedMD explicitly notes:
# 
# > **NOTE**: Some Linux distributions may have unofficial Slurm packages available in software repositories. SchedMD does not maintain or recommend these packages.
# 
# Some of the reasons why SchedMD does not recommend inofficial builds might be:
# 
# 1. **SchedMD Does Not Maintain It**: The `slurm-wlm` package is maintained by the Debian community, not by SchedMD, the official developers of Slurm. Debian maintainers build and package Slurm for inclusion in their repositories, which may include modifications or configurations that differ from SchedMD's official releases.
# 
# 2. **Potential for Issues**: Unofficial packages may not always align with SchedMD's latest recommendations, configurations, or patches. This can lead to compatibility issues, missing features, or differences in behavior compared to SchedMD's official builds.
# 
# 3. **SchedMD's Recommendation**: SchedMD recommends building Slurm from source or using RPM/DEB packages built directly from their official tarballs (e.g., using `rpmbuild` or `debuild` as described in the guide). This ensures full control over the build process, dependencies, and configuration, tailored to the user's specific cluster needs.
# 
# Despite SchedMD's recommendation against unofficial packages, users might choose Debian's `slurm-wlm` for convenience, especially in environments already integrated with Debian's package management system (`apt`). Benefits include:
# 
# - **Ease of Installation**: Installing `slurm-wlm` via `apt` is simpler than building from source or creating custom packages.
# - **Dependency Management**: Debian's package manager automatically handles dependencies like `munge`, `mysql`, or other required libraries.
# - **System Integration**: The package is configured to work with Debian's conventions (e.g., systemd services, file paths like `/etc/slurm/` for configuration).
# 
# However, users should be cautious:
# 
# - **Version Lag**: Debian's `sid` repository may not always have the latest Slurm version. For example, as of October 12, 2025, `slurm-wlm` is at version `24.11.5-4`, which is recent but may lag behind SchedMD's latest releases.
# - **Customizations**: Debian's package may include patches or configurations not endorsed by SchedMD, potentially affecting behavior.
# - **Support**: Issues with Debian's package would need to be addressed through Debian's bug tracker rather than SchedMD's support channels.
# 

# ## 📝 Side Note: A Brief History of SLURM
# 

# Slurm was first developed in 2001 at **Lawrence Livermore National Laboratory (LLNL)** to manage large Linux clusters for high-performance computing (HPC). The first formal publication of Slurm appeared in a 2003 paper by Yoo, A.B., Jette, M.A., and Grondona, M., titled "SLURM: Simple Linux Utility for Resource Management," presented at the Workshop on Job Scheduling Strategies for Parallel Processing (published in Lecture Notes in Computer Science, pp. 44–60, Springer Berlin Heidelberg). This paper introduced Slurm’s design principles, emphasizing its lightweight architecture and adaptability and it is available at [https://www.osti.gov/servlets/purl/15002533](https://www.osti.gov/servlets/purl/15002533).
# 
# Slurm was designed as a lightweight, scalable alternative to existing resource managers. Over the years, SLURM gained popularity in the HPC community, with significant adoption by supercomputing centers. Key milestones include the introduction of the REST API in 2020 and support for JWT authentication in 2023.
# 
# In terms of scheduling, SLURM has evolved from initially only supporting FIFO to:
# - **Multifactor Priority Scheduling**, where multiple factors such as quality of service, age, size, _fairshare_, are taken into account when prioritizing jobs
# - **Backfill Scheduling**, allowing smaller, shorter jobs to “fill in” gaps in the schedule while waiting for larger jobs to acquire sufficient resources
# - **Preemption**, where higher-priority jobs can interrupt or suspend lower-priority jobs to access resources immediately
# - **Advanced Resource Allocation**: SLURM can allocate exactly the resources a job needs—CPUs, GPUs, memory, licenses, or even specific nodes—down to the socket or core level
# - **Burst Buffer Support**: fast intermediate storage (e.g., NVMe SSDs) placed between RAM and parallel filesystem to speed up I/O-heavy jobs without flooding slow storage
# - **Cloud & Elastic Computing**: automatically spin up/down cloud nodes (AWS, Azure, GCP) when on-prem resources are full
# - **Container Support**: run jobs inside Docker, Singularity/Apptainer, or Podman containers directly via SLURM to ensures reproducible, portable, secure software environments
# 
# Today, SLURM powers some of the world's largest supercomputers.
# 
# 

# ## 📝 Side Note: Debian's `sid` and SLURM

# Debian's versioning includes **stable** (e.g., `bookworm`), **testing** (e.g., `trixie`), and **unstable** (`sid`) branches. The `sid` branch, named after the mischievous character Sid from Toy Story (1995, Pixar Animation Studios), who breaks toys and creates chaos, reflects its role as Debian's cutting-edge, unstable repository where packages are continuously updated. As noted in Debian's documentation, `sid` is a development playground, prone to breakages but offering the latest software versions, like `slurm-wlm` version `24.11.5-4` as of October 2025.
# 
# Users might choose `slurm-wlm` from `sid` for its recent SLURM features, such as enhanced GPU autodetection (`AutoDetect=nvml` for NVIDIA GPUs) or REST API improvements (`slurmrestd`), which may not yet be in `bookworm` (e.g., `23.02.x`). Its integration with Debian’s `apt` simplifies installation and dependency management (e.g., `munge`, `mysql`). However, `sid`’s instability—akin to Sid’s destructive antics in Toy Story—makes it risky for production HPC clusters, as updates can introduce bugs or dependency conflicts. For testing or research environments needing the latest SLURM capabilities, `sid` is appealing, but SchedMD recommends building from source for reliability and official support.

# ## 📝 Side Note: Nerdy Names, Serious Systems
# 
# 

# While SLURM stands for Simple Linux Utility for Resource Management it also nods to *Slurm*, the soft drink in *Futurama*.
# 
# I notice more and more how deeply tech culture is shaped by the tastes and humor of a specific group — mostly young, male “nerds.” Debian versions named after *Toy Story* characters, SLURM taking its name from a beverage in *Futurama* — these choices aren’t random. They reveal a shared subculture that has long defined open-source and DevOps communities.
# 
# What started as playful references among enthusiasts has become a kind of tradition — a way of signaling identity and belonging. The same spirit shows up in projects like **Borg** (_Star Trek_) or **Python** (_Monty Python’s Flying Circus_). It’s a mix of wit, nostalgia, and a sense of “if you get the joke, you’re one of us.”
# 
# It encodes a certain kind of taste and belonging: if you recognize *Toy Story*, *Futurama*, *Star Wars*, or *Monty Python* jokes, you’re in the club. If not, you’re subtly reminded that the culture wasn’t built with you in mind. It’s not malicious, but it is a reflection of a narrow demographic shaping the collective tone of open-source and DevOps culture. And that tone often persists even as the field itself has become more diverse and mature.
# 
# There’s an interesting contrast here: these projects embody serious technical excellence, yet their cultural expression is stuck in a kind of perpetual adolescence — like an in-joke from a college dorm that somehow became global infrastructure.
# 
# This tendency, however, is mostly a relic of the early days of computer science up through the 1990s, when the field was dominated by a small, highly homogeneous group of enthusiasts steeped in science fiction, comics, and arcade culture. Modern technologies increasingly break away from this “nerd comics” culture, opting instead for names that are descriptive, abstract, or evocative. Examples include *Terraform*, *Docker*, *Kubernetes*, *Airflow*, *Figma*, *Notion*, and *Snowflake* — names that signal function, creativity, or metaphor rather than relying on insider pop-culture knowledge.
# 
# Perhaps what could be wished for is simply more freedom to break away from that established mold. Tech doesn’t have to lose its sense of humor to grow up a little. It can remain creative and irreverent, while exploring names, metaphors, and references that reflect the wider, richer world of ideas around it.

# ## 🚀 Configuration
# 
# Configuration instructions are provided in `/usr/share/doc/slurmctld/README.Debian`.

# In[ ]:


get_ipython().system('cat /usr/share/doc/slurmctld/README.Debian')


# We are going to create a file `slurm.conf`.
# 
# For convenience, create a symbolic link to the folder `/etc/slurm` so that the file can be opened from the left pane in Google Colab's Jupyterhub interface.

# In[ ]:


get_ipython().system('ln -s /etc/slurm ./')


# 4 CPUs, 7923 MB RAM):

# In[ ]:


get_ipython().run_cell_magic('writefile', '/etc/slurm/slurm.conf', '# Minimal slurm.conf for single-node testing
ClusterName=mylocalcluster
SlurmctldHost=localhost
AuthType=auth/munge
MpiDefault=none
ProctrackType=proctrack/linuxproc
ReturnToService=2
SlurmctldPidFile=/var/run/slurmctld.pid
SlurmctldPort=6817
SlurmdPidFile=/var/run/slurmd.pid
SlurmdPort=6818
StateSaveLocation=/var/spool/slurmctld
SlurmdSpoolDir=/var/spool/slurmd
SlurmUser=slurm
SlurmdLogFile=/var/log/slurmd.log
SlurmctldLogFile=/var/log/slurmctld.log
# Node and partition configuration
NodeName=localhost CPUs=2 RealMemory=7923 State=UNKNOWN
PartitionName=LocalQ Nodes=localhost Default=YES MaxTime=INFINITE State=UP
')


# Verify your config: NodeName, ControlMachine, and PartitionName.Nodes must match either `localhost` or `hostname -s`.

# ## 📝 Configure using `slurm-wlm-configurator.html`
# 
# Instead of editing the configuration file `slurm.conf` you could also start a minimal Web app. This is an overkill for the current demonstration but it might be interesting to see all possible SLURM configuration parameters.

# 

# Begin by creating a minimal Flask Web application.

# In[ ]:


get_ipython().run_cell_magic('writefile', 'run_flask.py', 'from flask import Flask, Response
app = Flask(__name__)

@app.route(\'/\')
def serve_configurator():
   try:
       with open(\'/usr/share/doc/slurmctld/slurm-wlm-configurator.html\', \'r\') as f:
           html_content = f.read()
       return Response(html_content, mimetype=\'text/html\')
   except FileNotFoundError:
       return "Error: slurm-wlm-configurator.html not found", 404

if __name__ == \'__main__\':
   app.run()
')


# In[ ]:


import subprocess
import os
import signal

# Check if the process is running and terminate it
if 'process' in locals() and process.poll() is None:
    print("Terminating existing Flask process...")
    process.terminate()

with open('flask.out', "w") as stdout_file, open('flask.err', "w") as stderr_file:
    process = subprocess.Popen(
        ["python", "run_flask.py"],
        stdout=stdout_file,
        stderr=stderr_file,
        preexec_fn=os.setsid  # Start the process in a new session
    )


# Serve the Web app through `output` (only works if in Google Colab). Click on the link below.

# In[ ]:


import sys
# true if running on Google Colab
IN_COLAB = 'google.colab' in sys.modules
if IN_COLAB:
  from google.colab import output
  output.serve_kernel_port_as_window(5000)


# In[ ]:


get_ipython().system('hostname -s')


# ## 🚀 Generate a `munge` key
# 
# MUNGE stands for **M**ac-based **U**ser **N**ame **G**roup **E**xpiration and it is a lightweight, high-performance authentication system used by SLURM to securely verify user identity (UID/GID) and message integrity across cluster nodes using a shared symmetric key and time-limited credentials. It ensures fast, trusted communication between SLURM daemons and clients with minimal overhead.

# Generate a secure, random 1024-byte shared key for MUNGE authentication.

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'sudo dd if=/dev/urandom of=/etc/munge/munge.key bs=1 count=1024 >/dev/null 2>&1
sudo chown munge:munge /etc/munge/munge.key
sudo chmod 400 /etc/munge/munge.key
')


# ## 🚀 Create Spool Directories

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'sudo mkdir -p /var/spool/slurmctld /var/spool/slurmd /var/lib/munge
sudo chown slurm:slurm /var/spool/slurm{ctld,d} /var/lib/munge
sudo chown munge:munge /var/lib/munge
sudo chmod 755 /var/spool/slurm* /var/lib/munge
')


# > ### 📌 Recap: installation
# > - On Ubuntu, install the unofficial Debian package for SLURM with the command `apt install slurm-wlm -y`
# > - A minimal configuration requires creating a `slurm.conf` file, a `munge` key, and spool directories.

# ## 🚀 Start the Services

# Skip the next step if you are launching the services for the first time.

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'sudo service munge stop
sudo service slurmctld stop
sudo service slurmd stop
')


# In[ ]:


get_ipython().run_cell_magic('bash', '', 'sudo service munge start
sudo service slurmctld start
sudo service slurmd start
')


# ## 🚀 Verify Cluster Status

# In[ ]:


get_ipython().system('sinfo')


# You should see something like
# ```
# PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
# LocalQ*      up   infinite      1   idle localhost
# ```
# 
# This is a 1-node cluster with no time limit for jobs.

# If the node is not idle, set it:

# In[ ]:


get_ipython().system('sudo scontrol update NodeName=6d91971d1d4a State=IDLE')


# ## 📝 Useful Commands for Debugging
# 
# To look for errors you can use:
# 
# - `tail /var/log/slurmctld.log` to view the end of the `slurmctld` log file.
# - `grep "error" /var/log/slurmctld.log` to search for specific terms like "error" in the log file.
# - `sudo -u slurm /usr/sbin/slurmctld -D -vvv` for streaming output to the console
# 
# 

# In[ ]:


get_ipython().system('grep "error" /var/log/slurmctld.log')


# > ## 📌 Recap: start SLURM
# > - Three services need to be started: `munge`, `slurmctld`, and `slurmd`.
# > - Use `sinfo` to verify the cluster status.

# ## 🚀 Run a simple job
# 
# To run a SLURM job, you generally embed _SLURM directives_ inside a shell script. This script tells SLURM what resources you need and what commands to execute.
# 
# The script must start with #!/bin/bash or another valid shell.
# 
# All SLURM directives start with `#SBATCH` and must appear at the top of the script before any commands. For instance the following directives
# ```
# #!/bin/bash
# #SBATCH --partition=LocalQ
# #SBATCH --ntasks=1
# #SBATCH --cpus-per-task=2
# #SBATCH --mem=100M
# ```
# tell SLURM:
# - to run the job in partition (queue) `LocalQ` (we chose this name in the configuration file);
# - to run one task (one single process) with $2$ CPU cores for each task;
# - to request $100$ megabytes of RAM—SLURM will reserve this amount and prevent your job from exceeding it. Depending on how memory constraints are configured, if your program uses more memory than requested, it may be terminated.
# 
# After the `#SBATCH` directives, you can write normal shell commands.
# 
# ⚠️ Be careful not insert blank lines between the shebang (`#!/bin/bash`) and the directives (`#SBATCH`) otherwise SLURM will ignore them!

# This is a bash script that computes the sum of the first $100$ numbers.

# In[ ]:


get_ipython().run_cell_magic('writefile', 'simple_job.sh', '#!/bin/bash
#SBATCH --partition=LocalQ
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=100M

echo "Job started on $(hostname) at $(date)"
echo "Running on node: $SLURM_NODELIST"
echo "Job ID: $SLURM_JOB_ID"
echo "Calculating sum of numbers 1 to 100..."
sum=0
for i in {1..100}; do
    sum=$((sum + i))
done
echo "Sum: $sum"
sleep 5
echo "Job finished at $(date)"
')


# In[ ]:


get_ipython().run_cell_magic('bash', '', 'chmod +x simple_job.sh
sbatch simple_job.sh
sleep 5
')


# In[ ]:


get_ipython().system('ls slurm-*.out')


# In[ ]:


get_ipython().system('cat slurm-1.out')


# Check if the result is correct

# In[ ]:


100*101/2


# ## 🚀 Did the Job Run in Parallel?

# In[ ]:


get_ipython().system('scontrol show job 1')


# The line
# ```
# NumNodes=1 NumCPUs=2 NumTasks=1 CPUs/Task=2 ...
# ```
# confirms that SLURM reserved 2 CPUs for our job.
# 
# But this doesn't mean that the job used the two CPUs for parallel computation since our script `simple_job.sh` is a sequential Bash loop (`for i in {1..100}`) that runs on a single process/thread.
# 
# The option `--cpus-per-task=2` means that SLURM allocates 2 CPUs to the job and that other jobs can’t use them, but the script’s computation remains single-threaded.

# > ## 📌 Recap: SLURM doesn't parallelize your code for you
# > SLURM just hooks you up with resources like CPUs or machines. If your program’s single-threaded, it’ll stick to one CPU unless you make it parallel.
# 

# **Note:** The `scontrol show job` command primarily shows information about jobs that are currently running or have recently completed and are still held in SLURM's internal state. This information is not retained indefinitely.
# 
# For long-term retention of job information, SLURM uses an accounting database that needs to be installed extra and can be queried with `sacct`). The retention period for job information in the accounting database is determined by the SLURM accounting configuration.

# ## 🚀  Single-task parallel Python with `multiprocessing` and `--cpus-per-task`

# Let us modify the script so that it runs in parallel on the two CPUs. In order to achieve this, let us use Python's `multiprocessing` library. Note that we still need to wrap our code inside a shell script.

# In[ ]:


get_ipython().run_cell_magic('writefile', 'simple_job_parallel.sh', '#!/bin/bash
#SBATCH --partition=LocalQ
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=100M

echo "Job started on $(hostname) at $(date)"
echo "Running on node: $SLURM_NODELIST"
echo "Job ID: $SLURM_JOB_ID"
echo "Calculating sum of numbers 1 to 100 in parallel with Python..."

python3 -c "
from multiprocessing import Pool
def add(x): return x
with Pool(processes=2) as pool:
    result = sum(pool.map(add, range(1, 101)))
print(f\'Sum: {result}\')
"

sleep 10
echo "Job finished at $(date)"
')


# In[ ]:


get_ipython().run_cell_magic('bash', '--out id', 'sbatch simple_job_parallel.sh
')


# In[ ]:


get_ipython().system('echo {id}')


# In[ ]:


JOB_ID = id.split()[-1]


# In[ ]:


get_ipython().system('cat slurm-{JOB_ID}.out')


# Let us introduce some logging to view the parallel processing.

# In[ ]:


get_ipython().run_cell_magic('writefile', 'simple_job_parallel.sh', '#!/bin/bash
#SBATCH --job-name="Run in Parallel"  # name of the job
#SBATCH --partition=LocalQ
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=100M
#SBATCH --time=00:02:00               # HH:MM:SS format

# Ensure psutil is installed
if ! python3 -c "import psutil" 2>/dev/null; then
    sudo apt update && sudo apt install -y python3-psutil
fi

echo "Job started on $(hostname) at $(date)"
echo "Running on node: $SLURM_NODELIST"
echo "Job ID: $SLURM_JOB_ID"
echo "Calculating sum of numbers from 1 to 100 in parallel with Python..."

python3 -c "
import multiprocessing as mp
import psutil
import os
import time

def add(x):
    # Log PID and CPU affinity
    process = psutil.Process()
    cpu_affinity = process.cpu_affinity()
    start_time = time.ctime(process.create_time())
    print(f\'Process PID={os.getpid()}, CPU affinity={cpu_affinity}, Start time={start_time}, x={x}\')
    return x

if __name__ == \'__main__\':
    with mp.Pool(processes=2) as pool:
        result = sum(pool.map(add, range(1, 101)))
    print(f\'Sum of numbers: {result}\')
"

sleep 10
echo "Job finished at $(date)"
')


# In[ ]:


get_ipython().run_cell_magic('bash', '--out id', 'sbatch simple_job_parallel.sh
')


# In[ ]:


get_ipython().system('echo {id}')


# **Note:** the number of processes (defined in `Pool(processes=2)`) should not exceed the CPUs reserved in SLURM (`--cpus-per-task=2`), otherwise some processes might have to wait while the maximum $2$ CPUs available simultaneosly are busy. Running more parallel processes than the number of CPUs reserved (via `--cpus-per-task`) is called _oversubscription_. The job might still complete if there is enough available memory, but it will be slowed down.

# In[ ]:


JOB_ID = id.split()[-1]


# In[ ]:


import time

# Wait for the job to finish
while True:
    result = get_ipython().getoutput('squeue -j {JOB_ID} -h')
    if not result:  # squeue returns empty if job is not in queue
        print(f"Job {JOB_ID} finished.")
        break
    else:
        print(f"Waiting for job {JOB_ID} to finish...")
        print("
".join(result))
        time.sleep(5) # Wait for 5 seconds before checking again

# After the job is finished, you can view the output files
get_ipython().system('cat slurm-{JOB_ID}.out')


# We can now see that two processes were spawned:

# In[ ]:


get_ipython().system("cut -d' ' -f2 slurm-{JOB_ID}.out |grep PID| sort | uniq")


# We can also see which numbers were picked by each process:

# In[ ]:


get_ipython().system("cut -d' ' -f2,12 slurm-{JOB_ID}.out |grep PID| sort | uniq -f1")


# In[ ]:


get_ipython().system('scontrol show job {JOB_ID}')


# **Note:** Python's `multiprocessing.Pool.map()` automatically splits the computation into chunks (works for **any iterable**, not just numbers):
# * `range(1, 101)` → 100 items: 1, 2, 3, …, 100
# * `Pool(processes=2)` → creates **2 worker processes**
# * `pool.map(add, range(1, 101))` splits the 100 items and for 2 processes, it might assign roughly:
#     | Process  | Items  |
#     | -------- | ------ |
#     | Worker 1 | 1–50   |
#     | Worker 2 | 51–100 |
# 
# ```
#     range(1, 101)  →  [1, 2, 3, ..., 100]
# 
#     Pool(processes=2)
#     ┌───────────────┐   ┌───────────────┐
#     │ Worker 1      │   │ Worker 2      │
#     │ 1, 2, 3 ...50 │   │ 51, 52 ...100 │
#     └───────────────┘   └───────────────┘
# 
#     Each worker applies add(x) to its chunk
#     Results are collected and combined → sum = 5050
# ```
# 

# ## 🚀 Run multiple tasks with `srun`

# In[ ]:


get_ipython().run_cell_magic('writefile', 'simple_job_srun.sh', '#!/bin/bash
#SBATCH --job-name="srun job"  # name of the job
#SBATCH --ntasks=2             # number of tasks
#SBATCH --cpus-per-task=1      # we just have 2 CPUs on COlab
#SBATCH --mem=100M
#SBATCH --time=00:02:00        # HH:MM:SS format

# Ensure psutil is installed
if ! python3 -c "import psutil" 2>/dev/null; then
    sudo apt update && sudo apt install -y python3-psutil
fi

echo "Job started on $(hostname) at $(date)"
echo "Running on node: $SLURM_NODELIST"
echo "Job ID: $SLURM_JOB_ID"
echo "Calculating sum of numbers from 1 to 100 with srun ..."

python3 -c "
import psutil
import os
import time

def add(x):
    # Log PID and CPU affinity
    process = psutil.Process()
    cpu_affinity = process.cpu_affinity()
    start_time = time.ctime(process.create_time())
    print(f\'Process PID={os.getpid()}, CPU affinity={cpu_affinity}, Start time={start_time}, x={x}\')
    return x

if __name__ == \'__main__\':
    result = sum(map(add, range(1, 101)))
    print(f\'Sum of numbers: {result}\')
"

sleep 10
echo "Job finished at $(date)"
')


# In[ ]:


get_ipython().run_cell_magic('bash', '--out id', 'sbatch simple_job_srun.sh
')


# In[ ]:


get_ipython().system('echo {id}')


# In[ ]:


JOB_ID = id.split()[-1]


# In[ ]:


import time

# Wait for the job to finish with a timeout
timeout = 30 # seconds
start_time = time.time()

while True:
    result = get_ipython().getoutput('squeue -j {JOB_ID} -h')
    if not result:  # squeue returns empty if job is not in queue
        print(f"Job {JOB_ID} finished.")
        break
    elif time.time() - start_time > timeout:
        print(f"Timeout ({timeout} seconds) reached. Job {JOB_ID} may still be running or have failed.")
        break
    else:
        print(f"Waiting for job {JOB_ID} to finish...")
        print("
".join(result))
        time.sleep(5) # Wait for 5 seconds before checking again

# After the job is finished (or timeout), you can attempt to view the output files
get_ipython().system('cat slurm-{JOB_ID}.out')


# But in this case we only ran one process

# In[ ]:


get_ipython().system("cut -d' ' -f2 slurm-{JOB_ID}.out |grep PID| sort | uniq")


# In[ ]:


get_ipython().system("cut -d' ' -f2,12 slurm-{JOB_ID}.out |grep PID| sort | uniq -f1")


# Even though $2$ CPUs were reserved, `srun` did not automatically split the job into two tasks, but instead ran the job on one CPU while keeping the second one reserved (and idle).

# In[ ]:


get_ipython().system('scontrol show job {JOB_ID}')


# With `srun` it's up to us to specify how to split the job.

# In[ ]:


get_ipython().run_cell_magic('writefile', 'simple_job_srun_manual_split.sh', '#!/bin/bash
#SBATCH --job-name="srun job"  # name of the job
#SBATCH --ntasks=2             # number of tasks
#SBATCH --cpus-per-task=1      # we just have 2 CPUs on COlab
#SBATCH --mem=100M
#SBATCH --time=00:02:00        # HH:MM:SS format

# Ensure psutil is installed
if ! python3 -c "import psutil" 2>/dev/null; then
    sudo apt update && sudo apt install -y python3-psutil
fi

echo "Job started on $(hostname) at $(date)"
echo "Running on node: $SLURM_NODELIST"
echo "Job ID: $SLURM_JOB_ID"
echo "Calculating sum of numbers from 1 to 100 with srun ..."

# Launch Python for each SLURM task
srun python3 - <<EOF
import psutil
import os
import time

def add(x):
    # Log PID and CPU affinity
    process = psutil.Process()
    cpu_affinity = process.cpu_affinity()
    start_time = time.ctime(process.create_time())
    print(f\'Process PID={os.getpid()}, CPU affinity={cpu_affinity}, Start time={start_time}, x={x}\')
    return x

if __name__ == \'__main__\':
    # SLURM environment variables
    task_id = int(os.environ.get("SLURM_PROCID", 0))
    ntasks = int(os.environ.get("SLURM_NTASKS", 1))

    # Split the range across tasks
    total = 100
    chunk_size = total // ntasks
    start = task_id * chunk_size + 1
    end = (task_id + 1) * chunk_size if task_id != ntasks - 1 else total

    # Compute partial sum
    result = sum(map(add, range(start, end + 1)))
    print(f"Task {task_id}: sum({start}..{end}) = {result}")

EOF

sleep 10
echo "Job finished at $(date)"
')


# In[ ]:


get_ipython().run_cell_magic('bash', '--out id', 'sbatch simple_job_srun_manual_split.sh
')


# In[ ]:


get_ipython().system('echo {id}')


# In[ ]:


JOB_ID = id.split()[-1]


# In[ ]:


get_ipython().system('scontrol show job {JOB_ID}')


# In[ ]:


get_ipython().system('sleep 5')
get_ipython().system('cat slurm-{JOB_ID}.out')


# Now the computation was split into two tasks, each task had its own process and the two processes ran simultaneously.

# In[ ]:


get_ipython().system("cut -d' ' -f2 slurm-{JOB_ID}.out |grep PID| sort | uniq")


# In[ ]:


get_ipython().system("cut -d' ' -f2,12 slurm-{JOB_ID}.out |grep PID| sort | uniq -f1")


# > ## 📌 Recap: how to run a SLURM job
# >
# > * Start your script with the shebang `#!/bin/bash`
# > * Use SBATCH directives to request resources: `#SBATCH --option=value`
# > * Do **not** insert empty lines between the shebang and SBATCH directives
# > * Most common directives: `--job-name`, `--output`, `--error`, `--partition`, `--ntasks`, `--cpus-per-task`, `--mem`, `--time`
# > * Write your commands **after the directives**, e.g., `python my_script.py`
# > * Run $2$ tasks in parallel with `--ntasks=1`, `--cpus-per-task=2`, and Python's `multiprocessing` with `Pool(2)`
# > * Use `srun` for parallel execution with `--ntasks` ≥$1$ but take care of splitting the computation

# ## 🚀 SLURM Job Arrays

# Here is a simple script to demonstrate SLURM job arrays. Each task in the array will print its assigned `SLURM_ARRAY_TASK_ID`.

# In[ ]:


get_ipython().run_cell_magic('writefile', 'simple_array_job.sh', '#!/bin/bash
#SBATCH --partition=LocalQ
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --output=array_output_%A_%a.out
#SBATCH --array=0-3  # This creates a job array with tasks 0, 1, 2, and 3

echo "This is array task $SLURM_ARRAY_TASK_ID of job $SLURM_JOB_ID"
echo "Running on node: $SLURM_NODELIST"
sleep 5 # Simulate some work
')


# In[ ]:


# Make the script executable
get_ipython().system('chmod +x simple_array_job.sh')


# In[ ]:


get_ipython().run_cell_magic('bash', '--out id', 'sbatch simple_array_job.sh
')


# In[ ]:


get_ipython().system('echo {id}')


# In[ ]:


JOB_ID = id.split()[-1]


# In[ ]:


# Check the job status (optional)
get_ipython().system('squeue')


# If the jobs are not yet finished, you will get an error when you try to view the output files.
# 
# ```
# cat: 'array_output_*.out': No such file or directory
# ```
# 

# In[ ]:


get_ipython().system('cat array_output_*.out')


# After the jobs are finished, you can view the output files.

# In[ ]:


import time

# Wait for all jobs to finish
while True:
    result = get_ipython().getoutput('squeue -u $(id -u)')
    # Check if the output contains more than just the header
    if len(result) <= 1:
        print("All jobs finished.")
        break
    else:
        print("Waiting for jobs to finish...")
        print("
".join(result))
        time.sleep(5) # Wait for 5 seconds before checking again

# After the jobs are finished, you can view the output files
get_ipython().system('cat array_output_*.out')

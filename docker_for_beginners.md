# Docker for beginners

## Table of Contents

* [Part I: Getting started](#part-i-getting-started)
  * [Install Docker](#install-docker)
  * [After installation, check Docker version](#after-installation-check-docker-version)
  * [Download an image from the Docker Hub](#download-an-image-from-the-docker-hub)
    * [What is Docker Hub?](#what-is-docker-hub)
    * [What is Alpine Linux?](#what-is-alpine-linux)
    * [What is an image?](#what-is-an-image)
    * [Finally, "pull the image"](#finally-pull-the-image)
  * [Run a simple echo command in a container using the ```alpine``` image](#run-a-simple-echo-command-in-a-container-using-the-alpine-image)
  * [Run another command in a Docker container](#run-another-command-in-a-docker-container)
  * [Run command in a Docker container that's not installed](#run-command-in-a-docker-container-thats-not-installed)
  * [Docker's `hello-world` image](#dockers-hello-world-image)
  * [List Docker images](#list-docker-images)
  * [View running Docker containers](#view-running-docker-containers)
  * [View all Docker containers (running or not)](#view-all-docker-containers-running-or-not)
  * [Recap: images and containers](#recap-images-and-containers)
* [Part II: Basic interactions with containers](#part-ii-basic-interactions-with-containers)
  * [How to run a Docker container as a daemon](#how-to-run-a-docker-container-as-a-daemon)
  * [Stop a running container](#stop-a-running-container)
  * [Run a docker container in the background and keep it alive](#run-a-docker-container-in-the-background-and-keep-it-alive)
  * [How to "enter" a Docker container](#how-to-enter-a-docker-container)
  * [How to change your bash prompt in a container](#how-to-change-your-bash-prompt-in-a-container)
  * [How to remove a container](#how-to-remove-a-container)
  * [Recap: running containers](#recap-running-containers)
	
    

## Part I: Getting started
### Install Docker

If Docker is not installed, you need to install Docker.
At a command prompt type:

```
[~/docker_for_beginners]$ docker -v
sh: docker: command not found
```

If you get this message then you need to install Docker.

Here you will find the instructions for installing Docker 

* on a Mac: <a href="https://docs.docker.com/docker-for-mac/install/" target="_blank">Install Docker Desktop for Mac</a> (or alternatively good instructions  <a href="https://runnable.com/docker/install-docker-on-macos" target="_blank">here</a>). Note that only the newest versions of the Mac OS are supported and you will need at least 4GB of RAM.
* on Windows: <a href="https://docs.docker.com/docker-for-windows/install/" target="_blank">Install Docker Desktop on Windows</a>. Requirements: Windows 10 with 64 bit processor and at least 4GB of RAM.
* on Linux: <a href="https://docs.docker.com/install/linux/docker-ce/ubuntu/" target="_blank">Ubuntu</a>, <a href="https://docs.docker.com/install/linux/docker-ce/centos/" target="_blank">Centos</a>, etc.


### After installation, check Docker version

```
[~/docker_for_beginners]$ docker -v
Docker version 1.13.1, build 07f3374/1.13.1
```
This is really just to check that Docker is installed.

### Download an image from the Docker Hub

#### What is Docker Hub?

Docker Hub (<a href="https://hub.docker.com" target="_blank">https://hub.docker.com</a>) is an online repository of Docker images.

You will need an image to get started with Docker—for this we're going to use Alpine Linux (<a href="https://hub.docker.com/_/alpine" target="_blank">https://hub.docker.com/_/alpine</a>).

#### What is Alpine Linux?

Alpine Linux (Alpine for short) is a minimal Linux image, designed to run from the computer's RAM. Its size is 5MB.

This is off-topic for a beginner's tutorial, but you're interested in learning more about Alpine Linux you can read an interview with its creator (<a href="https://thenewstack.io/alpine-linux-heart-docker/" target="_blank">https://thenewstack.io/alpine-linux-heart-docker/</a>) or the Wikipedia entry for Alpine Linux (<a href="https://en.wikipedia.org/wiki/Alpine_Linux" target="_blank">https://en.wikipedia.org/wiki/Alpine_Linux</a>).

#### What is an image?

The main entities in Docker are _containers_. A container is a piece of software that emulates a complete machine with some pre-installed libraries and code. Containers allow to distribute software applications together with the whole environment they need for running. By packaging an application in a container we can run it on any computer without the need for any special configuration, thus making the application seamlessly portable.

A Docker image (sometimes also called _container image_) is a file that's essentially a snapshot of a container. Images are created with the `build` command, and they'll produce a container when started with `run`.

There's a discussion on Stackoverflow that helps clarifying the difference between images and containers:
<a href="https://stackoverflow.com/questions/23735149/what-is-the-difference-between-a-docker-image-and-a-container" target="_blank">What is the difference between a Docker image and a container?</a>

Some quotes from that discussion:

What is the difference between a Docker image and a container?

<a href="https://stackoverflow.com/questions/23735149/what-is-the-difference-between-a-docker-image-and-a-container#comment79144517_23736802" target="_blank">"_the image is the recipe, the container is the cake ;-) you can make as many cakes as you like with a given recipe_")

And what  is a stopped container then?
<a href="https://stackoverflow.com/questions/23735149/what-is-the-difference-between-a-docker-image-and-a-container#comment87604872_23736802" target="_blank">"_A stopped container is a cake in the freezer_"</a>

#### Finally, "pull the image"

In the Docker world, downloading an image is known as _pulling an image_ because to download an image you need to use the command `docker pull` followed by the name of the image.


```
[~/docker_for_beginners]$ docker pull alpine
```

### Run a simple echo command in a container using the ```alpine``` image

```
[~/docker_for_beginners]$ docker container run alpine echo "Hello World!"
```

You should see the string `Hello World!`. What has happened behind the scene? Docker created a container from your newly downloaded `alpine` image and you ran the command `echo "Hello World!"` inside this container. The result of the command is shown on your terminal.

### Run another command in a Docker container

To show the message-of-the-day (motd) file we run the command `cat /etc/motd` inside the container.

```
[~/docker_for_beginners]$ docker container run alpine cat /etc/motd
Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <http://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.
```

### Run command in a Docker container that's not installed

If you run a command in a container whose image is not yet installed, the image will be downloaded automatically from the Docker Hub. This is quite a practical feature!

We're going to `echo "Hello World!"` in a `centos` container.


```
[~/docker_for_beginners]$ docker container run centos echo "Hello World!"
Unable to find image 'centos:latest' locally
Trying to pull repository docker.io/library/centos ...
latest: Pulling from docker.io/library/centos
a02a4930cb5d: Pull complete
Digest: sha256:184e5f35598e333bfa7de10d8fb1cebb5ee4df5bc0f970bf2b1e7c7345136426
Status: Downloaded newer image for docker.io/centos:latest
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   639    0   639    0     0    612      0 --:--:--  0:00:01 --:--:--   612
Hello World!
```

So, in the previous example, instead of running `docker pull alpine` followed by `docker container run alpine echo "Hello World"` we could have just used the latter command. Still, one might also need sometimes to download an image without running it, so it' good to know how to do that.

### Docker's `hello-world` image

Docker provides a special `hello-world` image that can be called with:
```
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### List Docker images

To show all locally available Docker images use `docker images`. These are the images that we have pulled sometime in the past.

```
[~/docker_for_beginners]$ docker images
REPOSITORY                    TAG                 IMAGE ID            CREATED           SIZE
docker.io/centos              7.4.1708            295a0b2bd8ea        2 days ago        197 MB
alpine                        latest              961769676411        3 weeks ago       5.58MB
docker.io/hello-world         latest              4ab4c602aa5e        5 months ago      1.84 kB
```

### View running Docker containers

List Docker containers with `docker container ls`.

```
[~/docker_for_beginners]$ docker container ls
CONTAINER ID      IMAGE           COMMAND         CREATED         STATUS          PORTS            NAMES
```

You might at this point just get an empty list unless you have some running container.

### View all Docker containers (running or not)

```
[~/docker_for_beginners]$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS                          PORTS	NAMES

e57cbe736396        alpine              "echo 'Hello World'"     2 days ago           Exited (0) 2 days ago                     amazing_buck
9edd35220ee7        alpine              "ping 8.8.8.8"           About a minute ago   Exited (0) 2 days ago                     unruffled_archimedes
e3f28fbfb08f        alpine              "cat /etc/motd"          2 days ago           Exited (0) 2 days ago                     vibrant_gates
b86e65d14484        hello-world         "/hello"                 14 minutes ago       Exited (0) About a minute ago             everent_germain
```

Note how Docker assigns fantasy names (like the "amazing_buck" or "unruffled_archimedes" above) to new containers. You can assign a name to your containers by using the option `--name your-name` when creating them.

In place of `docker container ls` (respectively `docker container ls -a`) you can also use `docker ps` (resp. `docker ps -a`). See this <a href="https://github.com/docker/docker.github.io/issues/5850" target="_blank">discussion on Github</a> on why these two commands are both allowed.

### Recap: images and containers

We've defined Docker images and containers and seen how to run simple commands in a Docker container and list all our images and containers.

## Part II: Basic interactions with containers

### How to run a Docker container as a daemon

Instead of running a Docker container with an interactive shell it is also possible to let a Docker container run as a daemon, which means that the Docker container runs in the background completely detached from your current shell (the option `-d` stands for detached).

Let us start a container in daemon mode:

```
[~/docker_for_beginners]$ docker container run -d alpine ping host.docker.internal
a592973ccb204dbcd142052a89c187cc62b8bc1817a04c02e2f79a7205b8c1f7
```

Note that we used `ping host.docker.internal` to have a command running forever, so that the `alpine` container keeps running. `host.docker.internal` is the name under which Docker containers identify the address of the host where they're running (`localhost` outside the container).

If you now list running containers you should see it

```
[~/docker_for_beginners]$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED            STATUS           PORTS           NAMES
a592973ccb20        alpine              "ping host.docker.in…"   8 seconds ago      Up 23 seconds                    nifty_blackwell
```

### Stop a running container

To stop a running container use `docker stop`:

```
[~/docker_for_beginners]$ docker stop nifty_blackwell
nifty_blackwell
```

Note that you can use either the container's id or name as an argument to `stop`.

Check:
```
[~/Documents/my/docker_for_beginners]$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
Indeed, the container is no more running.

### Run a docker container in the background and keep it alive

Note that the option `-d` forces the container to run in a separate shell but when the container has no processes running then it stops.

```
[~/docker_for_beginners]$ docker container run -d alpine
a7a87f89bad8e9a079500feaa337b612b154bbc21bb8b1376d9724005930a5bf
[~/docker_for_beginners]$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

To keep the container alive use the run option `-i`:

```
[~/docker_for_beginners]$ docker container run -di alpine
10f7ffbddbb9c2ec3212c22e67bc1b3f56827a02bceb7feb6e81ae52409e7846
[~/docker_for_beginners]$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
10f7ffbddbb9        alpine              "/bin/sh"           3 seconds ago       Up 2 seconds                            hungry_chaplygin
```

Now the "hungry_chaplygin" alpine container is up even though it has no process running.

### How to "enter" a Docker container

To run a command in a running Docker container use `exec`.

```
$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
10f7ffbddbb9        alpine              "/bin/sh"           10 minutes ago      Up 10 minutes                           hungry_chaplygin
```

We are going to run a command inside a running alpine container. The command `uname -a` shows Linux operating system information.

```
[~/docker_for_beginners]$ docker exec -it hungry_chaplygin uname -a
Linux 10f7ffbddbb9 4.9.125-linuxkit #1 SMP Fri Sep 7 08:20:28 UTC 2018 x86_64 Linux
```
Start a shell inside the container, run some commands and exit.

```
$ docker exec -it hungry_chaplygin /bin/sh
/ # pwd
/
/ # ls -p
bin/   dev/   etc/   home/  lib/   media/ mnt/   opt/   proc/  root/  run/   sbin/  srv/   sys/   tmp/   usr/   var/
/ # whoami
root
/ # exit
```

### How to change your bash prompt in a container

Open the file `$HOME/.profile` and add this line:

```
export PS1='\033[31mDOCKER ${HOSTNAME}\e[0m [$(whoami) $(pwd)]# '
```

This will show "DOCKER" followed by the name of the Docker container in red
(<a href="hhttps://misc.flogisoft.com/bash/tip_colors_and_formatting" target="_blank">here</a> you can find more tips on how to format shell prompts).

```
[~/docker_for_beginners]$ docker exec -it hungry_chaplygin /bin/sh -l
DOCKER 10f7ffbddbb9 [root /]#
```

Note: since by default `sh` won't read  the `.profile` file but it will read it only at login, the `-l` (login) option is needed.

### How to remove a container

If you don't need a container anymore, you can delete it as follows:

```
[~/docker_for_beginners]$ docker container rm <container ID>
```

Example:
```
[~/docker_for_beginners]$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS                          PORTS	NAMES

e57cbe736396        alpine              "echo 'Hello World'"     2 days ago           Exited (0) 2 days ago                     amazing_buck
9edd35220ee7        alpine              "ping 8.8.8.8"           About a minute ago   Exited (0) 2 days ago                     unruffled_archimedes
e3f28fbfb08f        alpine              "cat /etc/motd"          2 days ago           Exited (0) 2 days ago                     vibrant_gates
b86e65d14484        hello-world         "/hello"                 14 minutes ago       Exited (0) About a minute ago             everent_germain

[~/docker_for_beginners]$ docker container rm e57cbe736396
[~/docker_for_beginners]$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS                          PORTS	NAMES

9edd35220ee7        alpine              "ping 8.8.8.8"           About a minute ago   Exited (0) 2 days ago                     unruffled_archimedes
e3f28fbfb08f        alpine              "cat /etc/motd"          2 days ago           Exited (0) 2 days ago                     vibrant_gates
b86e65d14484        hello-world         "/hello"                 14 minutes ago       Exited (0) About a minute ago             everent_germain
```

As usual, you can refer to a container by its ID or by its name. 

If the container is running, you will get an error message when trying to remove it. In this case, you either first need to stop the container or use the `-f` ("force") option.

```
[~]$ docker ps
CONTAINER ID        IMAGE           COMMAND             CREATED             STATUS              PORTS           NAMES
e3eac2473614        alpine          "/bin/sh"           19 hours ago        Up 19 hours                         jolly_khayyam
[~]$ docker rm jolly_khayyam
Error response from daemon: You cannot remove a running container e3eac247361447118efea112a078fa78bcf1b2e86db7acd87bc7357511286e75. Stop the container before attempting removal or force remove
[~]$ docker rm -f e3eac2473614
e3eac2473614
[~]$ docker ps
CONTAINER ID        IMAGE           COMMAND             CREATED             STATUS              PORTS           NAMES
```

Note that removing a container does not remove the underlying image. To remove an image use `docker rmi image-name`. If you attempt to remove an image and there are containers (running or not ) using that image you will get an error message

```
[~]$ docker rmi centos
Error response from daemon: conflict: unable to remove repository reference "centos" (must force) - container ecc66757abbf is using its referenced image 67fa590cfc1c
```

If you really want to remove the image, you can then either remove all dependent containers first or force remove it with `docker rmi -f image-name`.

### Recap: running containers

We've seen how to: start a container in detached mode, keep a container alive, enter and exit a container, run a command in a running container, stop a container, remove a container.

# Terraform for beginners

**Color boxes used in this tutorial**

In this tutorial I'm using colored boxes according to the following conventions:

<div style="background-color:rgb(255, 218, 185);border:2px solid rgb(255,191,134);padding:3px">
<span style="font-variant:small-caps;font-weight:bold">Recap</span><br>
Useful summaries and takeaways.
</div>

<p>

<div style="background-color:rgb(16, 163, 127,.2);border:2px solid rgb(16, 163, 127,.3);padding:3px;">
<svg fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320"  style="width:32px;height:32px;"><g fill="currentColor"><path d="m297.06 130.97c7.26-21.79 4.76-45.66-6.85-65.48-17.46-30.4-52.56-46.04-86.84-38.68-15.25-17.18-37.16-26.95-60.13-26.81-35.04-.08-66.13 22.48-76.91 55.82-22.51 4.61-41.94 18.7-53.31 38.67-17.59 30.32-13.58 68.54 9.92 94.54-7.26 21.79-4.76 45.66 6.85 65.48 17.46 30.4 52.56 46.04 86.84 38.68 15.24 17.18 37.16 26.95 60.13 26.8 35.06.09 66.16-22.49 76.94-55.86 22.51-4.61 41.94-18.7 53.31-38.67 17.57-30.32 13.55-68.51-9.94-94.51zm-120.28 168.11c-14.03.02-27.62-4.89-38.39-13.88.49-.26 1.34-.73 1.89-1.07l63.72-36.8c3.26-1.85 5.26-5.32 5.24-9.07v-89.83l26.93 15.55c.29.14.48.42.52.74v74.39c-.04 33.08-26.83 59.9-59.91 59.97zm-128.84-55.03c-7.03-12.14-9.56-26.37-7.15-40.18.47.28 1.3.79 1.89 1.13l63.72 36.8c3.23 1.89 7.23 1.89 10.47 0l77.79-44.92v31.1c.02.32-.13.63-.38.83l-64.41 37.19c-28.69 16.52-65.33 6.7-81.92-21.95zm-16.77-139.09c7-12.16 18.05-21.46 31.21-26.29 0 .55-.03 1.52-.03 2.2v73.61c-.02 3.74 1.98 7.21 5.23 9.06l77.79 44.91-26.93 15.55c-.27.18-.61.21-.91.08l-64.42-37.22c-28.63-16.58-38.45-53.21-21.95-81.89zm221.26 51.49-77.79-44.92 26.93-15.54c.27-.18.61-.21.91-.08l64.42 37.19c28.68 16.57 38.51 53.26 21.94 81.94-7.01 12.14-18.05 21.44-31.2 26.28v-75.81c.03-3.74-1.96-7.2-5.2-9.06zm26.8-40.34c-.47-.29-1.3-.79-1.89-1.13l-63.72-36.8c-3.23-1.89-7.23-1.89-10.47 0l-77.79 44.92v-31.1c-.02-.32.13-.63.38-.83l64.41-37.16c28.69-16.55 65.37-6.7 81.91 22 6.99 12.12 9.52 26.31 7.15 40.1zm-168.51 55.43-26.94-15.55c-.29-.14-.48-.42-.52-.74v-74.39c.02-33.12 26.89-59.96 60.01-59.94 14.01 0 27.57 4.92 38.34 13.88-.49.26-1.33.73-1.89 1.07l-63.72 36.8c-3.26 1.85-5.26 5.31-5.24 9.06l-.04 89.79zm14.63-31.54 34.65-20.01 34.65 20v40.01l-34.65 20-34.65-20z"></path></svg>
Answers from ChatGPT or GPT-4.
</div>

<p>

<div style="background-color:rgb(245, 245, 220);padding:3px">
<b>Digressions</b><br>
Just random digressions and musings.
</div>

## What is Terraform?

So, you might have heard about Terraform, but what exactly is Terraform?

Let's ask ChatGPT:

<div style="background-color:rgb(16, 163, 127,.2);border:2px solid rgb(16, 163, 127,.3);padding:3px;">
<svg fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320"  style="width:32px;height:32px;"><g fill="currentColor"><path d="m297.06 130.97c7.26-21.79 4.76-45.66-6.85-65.48-17.46-30.4-52.56-46.04-86.84-38.68-15.25-17.18-37.16-26.95-60.13-26.81-35.04-.08-66.13 22.48-76.91 55.82-22.51 4.61-41.94 18.7-53.31 38.67-17.59 30.32-13.58 68.54 9.92 94.54-7.26 21.79-4.76 45.66 6.85 65.48 17.46 30.4 52.56 46.04 86.84 38.68 15.24 17.18 37.16 26.95 60.13 26.8 35.06.09 66.16-22.49 76.94-55.86 22.51-4.61 41.94-18.7 53.31-38.67 17.57-30.32 13.55-68.51-9.94-94.51zm-120.28 168.11c-14.03.02-27.62-4.89-38.39-13.88.49-.26 1.34-.73 1.89-1.07l63.72-36.8c3.26-1.85 5.26-5.32 5.24-9.07v-89.83l26.93 15.55c.29.14.48.42.52.74v74.39c-.04 33.08-26.83 59.9-59.91 59.97zm-128.84-55.03c-7.03-12.14-9.56-26.37-7.15-40.18.47.28 1.3.79 1.89 1.13l63.72 36.8c3.23 1.89 7.23 1.89 10.47 0l77.79-44.92v31.1c.02.32-.13.63-.38.83l-64.41 37.19c-28.69 16.52-65.33 6.7-81.92-21.95zm-16.77-139.09c7-12.16 18.05-21.46 31.21-26.29 0 .55-.03 1.52-.03 2.2v73.61c-.02 3.74 1.98 7.21 5.23 9.06l77.79 44.91-26.93 15.55c-.27.18-.61.21-.91.08l-64.42-37.22c-28.63-16.58-38.45-53.21-21.95-81.89zm221.26 51.49-77.79-44.92 26.93-15.54c.27-.18.61-.21.91-.08l64.42 37.19c28.68 16.57 38.51 53.26 21.94 81.94-7.01 12.14-18.05 21.44-31.2 26.28v-75.81c.03-3.74-1.96-7.2-5.2-9.06zm26.8-40.34c-.47-.29-1.3-.79-1.89-1.13l-63.72-36.8c-3.23-1.89-7.23-1.89-10.47 0l-77.79 44.92v-31.1c-.02-.32.13-.63.38-.83l64.41-37.16c28.69-16.55 65.37-6.7 81.91 22 6.99 12.12 9.52 26.31 7.15 40.1zm-168.51 55.43-26.94-15.55c-.29-.14-.48-.42-.52-.74v-74.39c.02-33.12 26.89-59.96 60.01-59.94 14.01 0 27.57 4.92 38.34 13.88-.49.26-1.33.73-1.89 1.07l-63.72 36.8c-3.26 1.85-5.26 5.31-5.24 9.06l-.04 89.79zm14.63-31.54 34.65-20.01 34.65 20v40.01l-34.65 20-34.65-20z"></path></svg>
Terraform is an infrastructure as code software that allows you to provision and manage cloud, infrastructure, and network resources.
</div>

Hmm... I'm not sure what that means...

Let's look at another definition 
from [https://kodekloud.com/playgrounds/playground-terraform](https://kodekloud.com/playgrounds/playground-terraform):
> ### What is Terraform?
> 
> Terraform is an infrastructure provisioning tool. It helps automate the process of creating and managing infrastructure using configuration files. 
> #### Terraform Workflow 
> 
> To provision infrastructure in Terraform, we follow three main steps: write, plan & apply.
> 
> **Writing:** In the writing stage, we define the infrastructure we want in a Terraform configuration file. 
> 
> **Planning:** After writing our Terraform configuration, we use the "terraform plan" command to preview the changes that will be made to our infrastructure. We use this step to verify that the changes are correct before applying them. 
> 
> **Applying:** The final step in the process is to use the "terraform apply" command to apply the changes defined in the execution plan. This will create/change the infrastructure to match the desired state defined in the configuration file. 
> #### Terraform Composition

> Terraform consists of two essential parts: the core & the providers.
> 
> <a id="core"></a>**Core:** Terraform is powered by an engine called Terraform core. The core is the Terraform binary (program) that provides all the basic functionality.
> 
> **Providers:** Terraform uses providers (plugins) to interact with different infrastructure providers, such as AWS, Azure, or Google Cloud. The providers handle all the logic required to authenticate with the providers and make API requests on our behalf. They also handle timeouts and errors that may occur during resource management.

I think the best thing to do at this point is to try out an example. But first we're going to need to:

## Install Terraform

Terraform is a tool that can be installed on your computer. 

The installation should be straightforward. Here are the instructions for installing Terraform on Mac/Linux or Windows
[https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform).

The software we just installed is the _Terraform core_ [mentioned earlier](#core).

### Verify the installation

After the installation, type

```
% terraform -help
```

or 

```
% terraform -version
Terraform v1.4.5
on darwin_amd64

Your version of Terraform is out of date! The latest version
is 1.4.6. You can update by downloading from https://www.terraform.io/downloads.html
```

at a command-prompt (note: `%` is my prompt).

In fact, I just noticed that the version that I installed not long ago (Terraform v1.4.5) is already out of date!

## Is Terraform open source?

Yes. Terraform is open source and it's written in Go. The source code can be found at: [https://github.com/hashicorp/terraform](https://github.com/hashicorp/terraform).

<div style="background-color:rgb(255, 218, 185);border:2px solid rgb(255,191,134);padding:3px">
<span style="font-variant:small-caps;font-weight:bold">Recap</span><br>
Terraform is an infrastructure as code software that allows you to provision and manage cloud, infrastructure, and network resources. 
<p>
To install Terraform on your machine follow the instructions at: <a href="https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform">https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform</a>
<p>
Terraform is written in Go and it's open source.
</div>

## What is a provider?

> Providers are a logical abstraction of an upstream API. They are responsible for understanding API interactions and exposing resources.

(quote from: [https://registry.terraform.io/browse/providers](https://registry.terraform.io/browse/providers))

### What is an upstream API?

I'm not sure what is meant by "_upstream API_" and how a  "_backstream API_" relates to it. 

As far as I understand, backstream APIs or services depend upon upstream ones.

Here are some examples of upstream and downstream for APIs and in a general context

| upstream    | downstream |
| ----------- | ----------- |
| database    | application using the database  |
| back-end    | front-end   |
| extracting raw materials | processing of materials into a product |


In a software system, an application relying on a database a is an example of downstream while the database offers the upstream service; a front-end is downstream to a back-end because it depends on the back-end; a production process involves collecting raw materials during the upstream stage and processing them into a finished product during the downstream stage.

In a river, downstream is the direction the river flows.  Upstream is going in the opposite direction to the river flow. 

Let's ask GPT4 (*)

<div style="background-color:rgb(16, 163, 127,.2);border:2px solid rgb(16, 163, 127,.3);padding:3px">
<svg fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320"  style="width:32px;height:32px;"><g fill="currentColor"><path d="m297.06 130.97c7.26-21.79 4.76-45.66-6.85-65.48-17.46-30.4-52.56-46.04-86.84-38.68-15.25-17.18-37.16-26.95-60.13-26.81-35.04-.08-66.13 22.48-76.91 55.82-22.51 4.61-41.94 18.7-53.31 38.67-17.59 30.32-13.58 68.54 9.92 94.54-7.26 21.79-4.76 45.66 6.85 65.48 17.46 30.4 52.56 46.04 86.84 38.68 15.24 17.18 37.16 26.95 60.13 26.8 35.06.09 66.16-22.49 76.94-55.86 22.51-4.61 41.94-18.7 53.31-38.67 17.57-30.32 13.55-68.51-9.94-94.51zm-120.28 168.11c-14.03.02-27.62-4.89-38.39-13.88.49-.26 1.34-.73 1.89-1.07l63.72-36.8c3.26-1.85 5.26-5.32 5.24-9.07v-89.83l26.93 15.55c.29.14.48.42.52.74v74.39c-.04 33.08-26.83 59.9-59.91 59.97zm-128.84-55.03c-7.03-12.14-9.56-26.37-7.15-40.18.47.28 1.3.79 1.89 1.13l63.72 36.8c3.23 1.89 7.23 1.89 10.47 0l77.79-44.92v31.1c.02.32-.13.63-.38.83l-64.41 37.19c-28.69 16.52-65.33 6.7-81.92-21.95zm-16.77-139.09c7-12.16 18.05-21.46 31.21-26.29 0 .55-.03 1.52-.03 2.2v73.61c-.02 3.74 1.98 7.21 5.23 9.06l77.79 44.91-26.93 15.55c-.27.18-.61.21-.91.08l-64.42-37.22c-28.63-16.58-38.45-53.21-21.95-81.89zm221.26 51.49-77.79-44.92 26.93-15.54c.27-.18.61-.21.91-.08l64.42 37.19c28.68 16.57 38.51 53.26 21.94 81.94-7.01 12.14-18.05 21.44-31.2 26.28v-75.81c.03-3.74-1.96-7.2-5.2-9.06zm26.8-40.34c-.47-.29-1.3-.79-1.89-1.13l-63.72-36.8c-3.23-1.89-7.23-1.89-10.47 0l-77.79 44.92v-31.1c-.02-.32.13-.63.38-.83l64.41-37.16c28.69-16.55 65.37-6.7 81.91 22 6.99 12.12 9.52 26.31 7.15 40.1zm-168.51 55.43-26.94-15.55c-.29-.14-.48-.42-.52-.74v-74.39c.02-33.12 26.89-59.96 60.01-59.94 14.01 0 27.57 4.92 38.34 13.88-.49.26-1.33.73-1.89 1.07l-63.72 36.8c-3.26 1.85-5.26 5.31-5.24 9.06l-.04 89.79zm14.63-31.54 34.65-20.01 34.65 20v40.01l-34.65 20-34.65-20z"></path></svg>
Upstream APIs typically refer to the APIs that a particular software system or service depends on to function properly. In other words, an upstream API is like a supplier of data or functionality that another system relies on. For example, if you have an app that needs to retrieve weather data from a weather service API, then the weather service API is considered the upstream API.
<p>
On the other hand, downstream APIs refer to the APIs that are dependent on a particular system or service. A downstream API is like a consumer of data or functionality that another system provides. For example, if you have an app that provides a payment gateway for customers to purchase products, then the payment gateway API is considered the downstream API because it relies on your app to function.
<p>
In summary, upstream APIs are the ones that supply data or functionality to a system, while downstream APIs are the ones that consume data or functionality provided by a system.
</div>
<p>

<div style="background-color:rgb(245, 245, 220);padding:3px">
<b>(*)</b><br>
I'm currently using the free trial of GPT-4 since my ChatGPT trial expired. I'm planning to get a license for one of the two after my current trial expires. I've found these language models very useful for my daily work—even though they are missing the "reasoning" part, they contain a great amount of knowledge (albeit sometimes not up-to-date) and they can often understand my information needs better than Google—at least that's my impression so far, very good at reformulating text, elaborating on a given topic, documenting code, debugging scripts, generate demos, ... but this would the topic of a longer discussion ...
</div>

### The terraform Registry

Terraform providers are listed in the Terraform registry ([https://registry.terraform.io/](https://registry.terraform.io/)).


The first three providers listed in the Terraform registry when you click on "browse providers" are:

| Provider     | # Downloads this month | # Downloads overall|
| ------------ | ----------- | ---------|
| [AWS](https://registry.terraform.io/providers/hashicorp/aws/latest)          | 34.7M       | 1.7B     | 
| [Azure](https://registry.terraform.io/providers/hashicorp/azurerm/latest)        | 6.2M        | 330.5M   |
| [Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest) | 9.2M        | 290.8M   |

I'm just going to add two other providers that interest me: Openstack because I'm working with it and local because we are going to use it for a demo later on.

| Provider     | # Downloads this month | # Downloads overall|
| ------------ | ----------- | ---------|
| [OpenStack](https://registry.terraform.io/providers/terraform-provider-openstack/openstack/latest)          | 388,655       | 11.4M     | 
| [local](https://registry.terraform.io/providers/hashicorp/local/latest)       | 4.6M        | 198.1M   |

By clicking on ["Documentation"](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) for the AWS provider you get a description of what this provider has to offer:

> **AWS Provider**
> Use the Amazon Web Services (AWS) provider to interact with the many resources supported by AWS. You must configure the provider with the proper credentials before you can use it.

> Use the navigation to the left to read about the available resources.

> To learn the basics of Terraform using this provider, follow the hands-on [get started tutorials](https://learn.hashicorp.com/tutorials/terraform/infrastructure-as-code). Interact with AWS services, including Lambda, RDS, and IAM by following the [AWS services tutorials](https://learn.hashicorp.com/collections/terraform/aws).


<div style="background-color:rgb(245, 245, 220);padding:3px">
<b>Hashicorp's tutorials are great</b><br>
Still, it might be convenient to finish the present tutorial first if you're a beginner at Terraform.</div>

<p>

<div style="background-color:rgb(255, 218, 185);border:2px solid rgb(255,191,134);padding:3px">
<span style="font-variant:small-caps;font-weight:bold">Recap</span><br>
Terraform providers are abstractions of so-called <em>upstream APIs</em>. These are typically the APIs used to set up a computing infrastructure in the cloud, such as AWS, Azure, or Google Cloud.
<p>
Terraform providers are listed in the Terraform registry (<a href="https://registry.terraform.io/">https://registry.terraform.io/</a>).
<p>
The Terraform registry also contains a trove of documentation, examples, tutorials, and interactive labs.
</div>

## Try an online example

The best way to try out Terraform is to use the hands-on labs provided by Hashicorp. These are live environments where one can try things out while learning [https://developer.hashicorp.com/tutorials/library?product=terraform&isInteractive=true](https://developer.hashicorp.com/tutorials/library?product=terraform&isInteractive=true).



### Run online hands-on lab

[https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli](https://developer.hashicorp.com/tutorials/library?product=terraform&isInteractive=true) is a lab where you're guided throught the installation of an nginx Docker container.

<div style="background-color:rgb(245, 245, 220);padding:3px">
If you don't know what Docker is you can check the tutorial <a href="https://github.com/groda/big_data/blob/master/docker_for_beginners.md">Docker for beginners</a>.
</div>

Click on "Show Terminal" and in the next screen on "Start". The setup  takes a couple of minutes. Once the environment is setup, you can work with it 20 minutes before it expires.

In this environment you can choose between "Code Editor" and "Terminal". "Code Editor" is a simple text editor and "Terminal" is a Linux terminal where you can enter the commands suggested in the side panel.


<div style="background-color:rgb(245, 245, 220);padding:3px">
<b>A small digression</b><br>
The lab environment is itself a Linux virtual machine with 2GB RAM and 20GB disk space. You can see this by running the following commands:

<img src="./handson_lab_docker_inspect.png">
The command <a href="https://www.freedesktop.org/software/systemd/man/systemd-detect-virt.html"><code>systemd-detect-virt</code></a> detects execution in a virtualized environment (in this case <code>kvm</code>).
</div>

#### The `main.tf` file

The first step in the tutorial consists in creating a `main.tf` file. You can copy-and-paste the text using the editor or else type this command in the terminal to populate the `main.tf` file:

```
cat >main.tf <<EOF
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.15.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.latest
  name  = "tutorial"
  ports {
    internal = 80
    external = 8000
  }
}
EOF
```

<div style="background-color:rgb(245, 245, 220);padding:3px">
<b>Another digression</b><br>
The construct <code>&lt;&lt;EOF</code> is useful for creating files on the command-line. Note that you can use any other string in place of <code>EOF</code> (as long as it matches the final one). I often use <code>LOL</code> in place of <code>EOF</code> because why not?
<p>
See also: <a href="https://stackoverflow.com/questions/2500436/how-does-cat-eof-work-in-bash">How does "cat << EOF" work in bash?</a>
</div>

A `.tf` file is a plain text file containing Terraform code. Sometimes `.tf` files are also called _configuration files_ (see [https://developer.hashicorp.com/terraform/language/files](https://developer.hashicorp.com/terraform/language/files)).

Terraform code can be saved all in one file or spread across multiple `.tf` files for convenience in the case of larger projects.

#### Initialize the project

By running
```
terraform init
```
in the terminal you initialize the project. The initialization consists in downloading a plugin that allows Terraform to interact with Docker.

#### Run the project

With 
```
terraform apply
```
you're going to start the infrastructure defined in the `main.tf` configuration file. 

You'll be required to enter `yes` to confirm that you want to proceed. To skip this step, use
```
terraform apply -auto-approve
```

#### Is the project running?

Use the command
```
docker ps
```
to check that a Docker container is running. 
This is the container that has been started ("_provisioned_") by Terraform using Terraform's Docker provider.

#### Destroy the infrastructure

Use the command
```
terraform destroy
```
to stop the Docker container.


<div style="background-color:rgb(255, 218, 185);border:2px solid rgb(255,191,134);padding:3px">
<span style="font-variant:small-caps;font-weight:bold">Recap</span><br>
Terraform is a tool for running projects. A project is defined in one or more Terraform configuration files. These are text files ending with <code>.tf</code> that resemble a JSON files.
<p>

Terraform tutorials and learning environments can be found at <a href="https://developer.hashicorp.com/terraform/tutorials">https://developer.hashicorp.com/terraform/tutorials</a>.
<p>
You can install Terraform on your machine or use Terraform's online learning environments to try out an initial demo. 

The main commands for launching a project with Terraform are:
<ul>
<li> <code>terraform init</code>
<li> <code>terraform apply</code> (or <code>terraform apply -auto-approve</code>)
<li> <code>terraform destroy</code>
</ul>

In Terraform lingo this is also called "<em>provisioning an infrastructure</em>".
</div>
 

 
## A brief introduction to the Terraform language


Terraform configuration uses the Terraform language  
> which is a rich language designed to be relatively easy for humans to read and write. The constructs in the Terraform language can also be expressed in JSON syntax, which is harder for humans to read and edit but easier to generate and parse programmatically. 

(quote from [https://developer.hashicorp.com/terraform/language/syntax/configuration](https://developer.hashicorp.com/terraform/language/syntax/configuration))

#### Arguments and blocks

The Terraform language syntax is built around two key syntax constructs: _arguments_ and _blocks_ ((see [https://developer.hashicorp.com/terraform/language/syntax/configuration#identifiers](https://developer.hashicorp.com/terraform/language/syntax/configuration#identifiers)).

An argument assigns a value to a particular name:

    image_id = "abc123"
    
A block is a container for other content:

	resource "aws_instance" "example" {
	  ami = "abc123"
	
	  network_interface {
	    # ...
	  }
	}
	
>A block has a type (`resource`in this example). Each block type defines how many labels must follow the type keyword. The `resource` block type expects two labels, which are `aws_instance` and `example` in the example above. A particular block type may have any number of required labels, or it may require none as with the nested `network_interface` block type.

>Following the block type keyword and any labels, the block body is delimited by the curly brackets ({}). Within the block body, further arguments and blocks may be nested, creating a hierarchy of blocks and their associated arguments.

#### The `terraform` block to begin with

The first block type that usually appears in a Terraform configuration file is the `terraform` block type. 
The `terraform` block type can be used to:

* specifying which version of Terraform we want
* what providers are required for running the project (`required_providers` block) 

The Terraform block is often put into a separate file called `terraform.tf` as a way to separate settings into their own file.

Here's a sample `terraform.tf` file (from [https://dev.to/af/hashicorp-configuration-language-hcl-blocks-5627](https://dev.to/af/hashicorp-configuration-language-hcl-blocks-5627):

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.0"
    }
  }
  required_version = ">= 1.0.1"
}
```

Note that the `terraform` block type requires no labels, it is just: `terraform { ... }`. Same for the `required_providers` block type.

The line `required_version = ">= 1.0.1"` tells Terraform that we need at least version 1.0.1 for Terraform. 

In the block `required_providers` we require the `aws` provider, specify where to find it (in `source`) and what is the minimal allowed version (`"~> 2.0"` means all versions that begin with `2`—see [the official documentation](https://developer.hashicorp.com/terraform/language/expressions/version-constraints) on how to specify version constraints).

Here can be found all Terraform providers with examples on how to use them: [https://registry.terraform.io/browse/providers](https://registry.terraform.io/browse/providers).

#### Identifiers 
> Argument names, block type names, and the names of most Terraform-specific constructs like resources, input variables, etc. are all identifiers.


>Identifiers can contain letters, digits, underscores (_), and hyphens (-). The first character of an identifier must not be a digit, to avoid ambiguity with literal numbers.
([https://developer.hashicorp.com/terraform/language/syntax/configuration#identifiers](https://developer.hashicorp.com/terraform/language/syntax/configuration#identifiers))

In the `terraform` block

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.0"
    }
  }
  required_version = ">= 1.0.1"
}
```
`terraform`, `required_providers`, `aws`, `source`, `version`, and `required_version` are all identifiers.

Honestly, I'm still not sure what's the difference between an identifier and a variable.

#### Comments

Useful to know: [comments](https://developer.hashicorp.com/terraform/language/syntax/configuration#comments) can be

* single-lines beginning with a `#` or a `//`
* multi-line between `/*` and `*/`

<div style="background-color:rgb(245, 245, 220);padding:3px">
<b>On comment-lines starting with <code>#</code> or <code>//</code></b><br>
I find it nice to be able to choose between <code>#</code> and <code>//</code> for single-line comments, also because I once tried to use <code>#</code> for comments in Javascript—it was a Proxy Auto-Configuration file and it took me forever to find out why it wasn't working—in Terraform that wouldn't have been a mistake!
</div>



#### Does the order matter?

So, Terraform relies on a series of blocks and arguments that can be spread across different files. 
But does the order of these chunks of configuration within files matter? Does the naming of the files matter? 

Up until now we've seen two different configuration files:

* `main.tf`
* `terraform.tf`

About ordering of files/blocks: according to the answer to ["can we order .tf files in terraform?"](https://stackoverflow.com/questions/74441521/can-we-order-tf-files-in-terraform):
> Terraform does not make any use of the order of .tf files or of the declarations in those files. Instead, Terraform decodes all of the blocks across all of your files and analyzes them to look for references between objects.

Also confirmed by ["Multiple .tf files in a folder"](https://stackoverflow.com/a/59516275/):
> In Terraform 0.12+ (including 1.x), the load order of *.tf files is no longer specified. Behind the scenes Terraform reads all of the files in a directory and then determines a resource ordering that makes sense regardless of the order the files were actually read.

<div style="background-color:rgb(245, 245, 220);padding:3px">
<b>Btw</b><br>
I find it a pity that a legitimate beginner's question like <a href="https://stackoverflow.com/questions/74441521/can-we-order-tf-files-in-terraform">"can we order .tf files in terraform?"</a> gets so many downvotes on Stack Overflow. 
</div>


#### `.tf` files naming conventions

About file naming, I haven't found anything about rules for the names of `.tf` files, so I assume here it's all about conventions, best practices, common sense, ... just doing what everybody else does. 
<div style="background-color:rgb(245, 245, 220);padding:3px">
<b>Go with the flow?</b><br>
I'm not recommending it as a general principle. Let's hear what GPT-4 has to say.
</div>
<p>

<div style="background-color:rgb(16, 163, 127,.2);border:2px solid rgb(16, 163, 127,.3);padding:3px">
<svg fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320"  style="width:32px;height:32px;"><g fill="currentColor"><path d="m297.06 130.97c7.26-21.79 4.76-45.66-6.85-65.48-17.46-30.4-52.56-46.04-86.84-38.68-15.25-17.18-37.16-26.95-60.13-26.81-35.04-.08-66.13 22.48-76.91 55.82-22.51 4.61-41.94 18.7-53.31 38.67-17.59 30.32-13.58 68.54 9.92 94.54-7.26 21.79-4.76 45.66 6.85 65.48 17.46 30.4 52.56 46.04 86.84 38.68 15.24 17.18 37.16 26.95 60.13 26.8 35.06.09 66.16-22.49 76.94-55.86 22.51-4.61 41.94-18.7 53.31-38.67 17.57-30.32 13.55-68.51-9.94-94.51zm-120.28 168.11c-14.03.02-27.62-4.89-38.39-13.88.49-.26 1.34-.73 1.89-1.07l63.72-36.8c3.26-1.85 5.26-5.32 5.24-9.07v-89.83l26.93 15.55c.29.14.48.42.52.74v74.39c-.04 33.08-26.83 59.9-59.91 59.97zm-128.84-55.03c-7.03-12.14-9.56-26.37-7.15-40.18.47.28 1.3.79 1.89 1.13l63.72 36.8c3.23 1.89 7.23 1.89 10.47 0l77.79-44.92v31.1c.02.32-.13.63-.38.83l-64.41 37.19c-28.69 16.52-65.33 6.7-81.92-21.95zm-16.77-139.09c7-12.16 18.05-21.46 31.21-26.29 0 .55-.03 1.52-.03 2.2v73.61c-.02 3.74 1.98 7.21 5.23 9.06l77.79 44.91-26.93 15.55c-.27.18-.61.21-.91.08l-64.42-37.22c-28.63-16.58-38.45-53.21-21.95-81.89zm221.26 51.49-77.79-44.92 26.93-15.54c.27-.18.61-.21.91-.08l64.42 37.19c28.68 16.57 38.51 53.26 21.94 81.94-7.01 12.14-18.05 21.44-31.2 26.28v-75.81c.03-3.74-1.96-7.2-5.2-9.06zm26.8-40.34c-.47-.29-1.3-.79-1.89-1.13l-63.72-36.8c-3.23-1.89-7.23-1.89-10.47 0l-77.79 44.92v-31.1c-.02-.32.13-.63.38-.83l64.41-37.16c28.69-16.55 65.37-6.7 81.91 22 6.99 12.12 9.52 26.31 7.15 40.1zm-168.51 55.43-26.94-15.55c-.29-.14-.48-.42-.52-.74v-74.39c.02-33.12 26.89-59.96 60.01-59.94 14.01 0 27.57 4.92 38.34 13.88-.49.26-1.33.73-1.89 1.07l-63.72 36.8c-3.26 1.85-5.26 5.31-5.24 9.06l-.04 89.79zm14.63-31.54 34.65-20.01 34.65 20v40.01l-34.65 20-34.65-20z"></path></svg>
Deciding whether to go with the flow or do what everyone else is doing is a personal choice that depends on your individual circumstances, values, and goals. Here are a few considerations to help you make your decision:
<p>
Individuality and Authenticity: Going with the flow may sometimes mean compromising your own unique perspectives, interests, or ambitions to align with the majority. If expressing your individuality and staying true to yourself is important to you, deviating from the norm might be a better choice.
<p>
Critical Thinking and Personal Growth: Following the crowd often involves accepting commonly held beliefs, practices, or trends without questioning them. If you value critical thinking and personal growth, it may be beneficial to challenge the status quo and explore alternative paths that align better with your own beliefs and aspirations.
<p>
Risk and Reward: Going against the grain can be riskier as it may involve uncertainty and resistance from others. However, it can also lead to greater rewards and opportunities. Consider the potential benefits and drawbacks of both options before making a decision.
<p>
Context and Consequences: Evaluate the specific situation and context in which you find yourself. Sometimes, going with the flow might be the most practical or efficient choice, especially if it aligns with your goals or if the deviation requires significant effort or resources.
<p>
Balance and Flexibility: It's not always an all-or-nothing decision. You can find a balance between going with the flow and asserting your individuality. Assess the situations where conformity is necessary and those where breaking away is beneficial. Flexibility allows you to adapt and make choices that serve you best in different circumstances.
<p>
Ultimately, the choice is yours, and there is no one-size-fits-all answer. Reflect on your values, aspirations, and what brings you fulfillment. Consider seeking guidance from trusted mentors or loved ones who understand your goals and can offer valuable insights.
</div>

<p>
<div style="background-color:rgb(255, 218, 185);border:2px solid rgb(255,191,134);padding:3px">
<span style="font-variant:small-caps;font-weight:bold">Recap</span><br>
Terraform files are composed of 
<ul>
<li><em>arguments</em>
<li><em>blocks</em>
</ul> 
An argument assigns a value to a given name, for instance <code>image_id = "abc123"</code>.

A block is a container composed by a <em>block type</em>, zero or more <em>labels</em> and some content within curly brackets, like for instance <code>terraform { ... }</code>.
<p>
The <code>terraform</code> block type can contain requirements on the Terraform version needed as well as on the required providers. 
<p>
Terraform configuration can be written to a single file or to multiple files. Ordering of configuration items does not matter as Terraform will take care of dependencies. 
<p>
Comment lines start with <code>#</code> or <code>//</code>, multi-line comments are between <code>/*</code> and <code>*/</code>.

</div>

## Hello, World! 


Let's build a "Hello, World!" project using the [`local`](https://registry.terraform.io/providers/hashicorp/local/latest) provider. 

This is the provider used to:

> manage local resources, such as creating files

Everyone has access to a local provider—that's the filesystem you're currently working on—and there's no need for authentication.

From the [docs](https://registry.terraform.io/providers/hashicorp/local/latest/docs): the local provider provides Resources for generating files (`local_file` and `local_sensitive_file`) and Data Sources for reading files (`local_file` and `local_sensitive_file`).


I'm not sure about the meaning of _sensitive_ in Terraform, I believe it's about data such as passwords that should not be shown in plain text, but let us ignore that for now and just use `local_file`.

Open a terminal on your machine or start a terminal online ([https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code) / Show Terminal / Launch --> / Start / Terminal) and type:

```
cat >main.tf <<LOL
terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
      version = "2.4.0"
    }
  }
}

resource "local_file" "hello" {
  filename = "/root/learn-terraform-docker-container/hello"
  content  = "Hello, World!\n"
  file_permission = "0400"
}
LOL
```

followed by:

```
terraform init
terraform apply -auto-approve
```

These commands will create a file called `hello` whose content is the string `"Hello, World!\n"`.

<div style="background-color:rgb(245, 245, 220);padding:3px">
<b>I'm beginning to like ...</b><br>
... the succinct and intuitive Terraform syntax without semicolons or indentation.
</div>
 

Now type:

```
cat hello
```

If everything worked, you should get the output: `Hello, World!`. In this example the only thing you might need to change is `filename` in the `terraform` provider.

Let us introduce a variable named `hello`:


```
cat>main.tf <<EOF
variable "hello" {
  type = string
  description = "greeting"
  default = "Hello. World!"
}
output "hello" {
  value = var.hello
}
EOF
```

Now use `terraform plan` to see what Terraform is going to do when calling `apply`:

```
root@workstation:~/learn-terraform-docker-container# terraform plan
local_file.hello: Refreshing state... [id=60fde9c2310b0d4cad4dab8d126b04387efba289]

Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # local_file.hello will be destroyed
  - resource "local_file" "hello" {
      - content              = <<-EOT
            Hello, World!
        EOT -> null
      - content_base64sha256 = "yYwktnfv9Ehgr+pvSTu67FuxxMuyCcb8K7tH9m/yrTE=" -> null
      - content_base64sha512 = "khYYvG2fgFlDfF4Dl7E/lzq3x6e4HwyjG3C/RI/YAKRgtn79oAIAiLyXv32dqXqeLOeyDUbgZkYuxEz2AoT5pw==" -> null
      - content_md5          = "bea8252ff4e80f41719ea13cdf007273" -> null
      - content_sha1         = "60fde9c2310b0d4cad4dab8d126b04387efba289" -> null
      - content_sha256       = "c98c24b677eff44860afea6f493bbaec5bb1c4cbb209c6fc2bbb47f66ff2ad31" -> null
      - content_sha512       = "921618bc6d9f8059437c5e0397b13f973ab7c7a7b81f0ca31b70bf448fd800a460b67efda0020088bc97bf7d9da97a9e2ce7b20d46e066462ec44cf60284f9a7" -> null
      - directory_permission = "0777" -> null
      - file_permission      = "0400" -> null
      - filename             = "/root/learn-terraform-docker-container/hello" -> null
      - id                   = "60fde9c2310b0d4cad4dab8d126b04387efba289" -> null
    }

Plan: 0 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + hello = "Hello. World!"

```

> The terraform plan command lets you to preview the actions Terraform would take to modify your infrastructure, or save a speculative plan which you can apply later

(quote from [https://developer.hashicorp.com/terraform/tutorials/cli/plan#create-a-plan](https://developer.hashicorp.com/terraform/tutorials/cli/plan#create-a-plan))

Since all we are asking for in our Terraform configuration file is to create a variable (`variable "hello" { }` block), when running `apply` Terraform is going to destroy the existing file.
 

Now run `apply -auto-approve`

```
root@workstation:~/learn-terraform-docker-container# terraform apply -auto-approve
[ . . .]
local_file.hello: Destroying... [id=60fde9c2310b0d4cad4dab8d126b04387efba289]
local_file.hello: Destruction complete after 0s

Apply complete! Resources: 0 added, 0 changed, 1 destroyed.

Outputs:

hello = "Hello. World!"
```

Note that in this last example we did not use any provider but relied just on the Terraform core.


<div style="background-color:rgb(255, 218, 185);border:2px solid rgb(255,191,134);padding:3px">
<span style="font-variant:small-caps;font-weight:bold">Recap</span><br>

Terraform allows to manage any infrastructure in a structured and succint way.
<p>

Terraform plugins called providers let Terraform interact with cloud platforms and other services via their application programming interfaces (APIs).
<p>
Providers can be found in the Terraform Registry.
</div>


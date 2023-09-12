

<!-- TOC --><a name="terraform-in-5-minutes"></a>
# Terraform in 5 minutes

Terraform is a powerful and popular tool for _infrastructure provisioning and management_. Its declarative syntax and _infrastructure-as-code_ approach make it concise and efficient for defining and managing infrastructure resources across various cloud providers.

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->


  * [Install Terraform](#install-terraform)
  * [Verify the installation](#verify-the-installation)
  * [Introduction to Terraform providers](#introduction-to-terraform-providers)
    + [The Terraform Registry](#the-terraform-registry)
    + [A basic provider block example](#a-basic-provider-block-example)
  * [Terraform project and configuration files](#terraform-project-and-configuration-files)
    + [`terraform init`](#terraform-init)
    + [`terraform apply`](#terraform-apply)
    + [`terraform destroy`](#terraform-destroy)
  * [A brief introduction to the Terraform language](#a-brief-introduction-to-the-terraform-language)
      - [Arguments and blocks](#arguments-and-blocks)
      - [The `terraform` block ](#the-terraform-block)
      - [Identifiers ](#identifiers)
      - [Comments](#comments)
  * [Terraform variables files](#terraform-variables-files)
    + [The advantage of `terraform.tfvars`](#the-advantage-of-terraformtfvars)
  * [How to generate Terraform configuration files](#how-to-generate-terraform-configuration-files)
  * [Infrastructure as Code with Automated Dependency Management](#infrastructure-as-code-with-automated-dependency-management)
  * [Recap](#recap)
  * [Happy Terraforming!](#happy-terraforming)

<!-- TOC end -->

<!-- TOC --><a name="install-terraform"></a>
## Install Terraform

Terraform is an installable tool that you can set up on your computer.

The installation process is typically straightforward. Here are step-by-step instructions for installing Terraform on Mac/Linux or Windows operating systems: 
[https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform).

The software just installed is also known as the _Terraform core_.

<!-- TOC --><a name="verify-the-installation"></a>
## Verify the installation

After completing the installation, you can open a command prompt and enter either of the following commands:

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

<!-- TOC --><a name="introduction-to-terraform-providers"></a>
## Introduction to Terraform providers

Terraform is an _infrastructure as code_ tool that enables the provisioning and management of resources across different cloud and infrastructure _providers_ by utilizing _provider plugins_ as the central mechanism for interfacing with those providers.

In simple terms, a Terraform provider is a plugin that allows Terraform to interact with a specific infrastructure or service provider, such as AWS, Azure, GCP, or OpenStack. It provides the necessary functionality to create, manage, and delete resources within that provider's environment using Terraform configuration files. 

Storing all elements of your infrastructure – such as virtual machines, networks, and security configurations – within files understandable to computers characterises the concept of "infrastructure as code".


<!-- TOC --><a name="the-terraform-registry"></a>
### The Terraform Registry

Terraform providers are listed in the Terraform registry ([https://registry.terraform.io/](https://registry.terraform.io/)).


Here's three popular providers—downloads data is from June 2023 (click on "browse providers" to see all providers):

| Provider     | # Downloads this month | # Downloads overall|
| ------------ | ----------- | ---------|
| [AWS](https://registry.terraform.io/providers/hashicorp/aws/latest)          | 34.7M       | 1.7B     | 
| [Azure](https://registry.terraform.io/providers/hashicorp/azurerm/latest)        | 6.2M        | 330.5M   |
| [Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest) | 9.2M        | 290.8M   |

And here's the Openstack entry:

| Provider     | # Downloads this month | # Downloads overall|
| ------------ | ----------- | ---------|
| [OpenStack](https://registry.terraform.io/providers/terraform-provider-openstack/openstack/latest)          | 388,655       | 11.4M     | 

<!-- TOC --><a name="a-basic-provider-block-example"></a>
### A basic provider block example

Here's a basic example of a Terraform _provider block_:

```
provider "my_aws_provider" {
    access_key = "my-access-key"
    secret_key = "my-secret-key"
    region     = "us-west-2"
}
```

In this example, the provider block configures the AWS provider. It specifies the access key, secret key, and region to authenticate and connect to the AWS services. `"my_aws_provider"` is the label or name used to identify this particular AWS provider. With this configuration, you can proceed to define and manage AWS resources using Terraform.

<!-- TOC --><a name="terraform-project-and-configuration-files"></a>
## Terraform project and configuration files

A project is defined in one or more Terraform configuration files. These are text files ending with `.tf` that resemble JSON files.

You can try out Terraform on your machine or use one of Terraform's online learning environments which can be found at [https://developer.hashicorp.com/terraform/tutorials]().

The main commands for managing an infrastructure with Terraform are:

```
terraform init
terraform apply 
terraform destroy
```

Terraform, by default, will automatically search for and process all files with a `.tf` extension in the current directory. Terraform treats all these `.tf` files as configuration files and combines them to build the overall configuration for your infrastructure. Note that the naming of the `.tf` files is not relevant.

<!-- TOC --><a name="terraform-init"></a>
### `terraform init`
With `terraform init` terraform one initializes the project. This includes downloading the required Terraform plugins. Generally one only needs to run `terraform init` once for a given Terraform project or when significant changes are made to the configuration, such as adding new providers or modifying backend configurations. 

<!-- TOC --><a name="terraform-apply"></a>
### `terraform apply`
After the initial initialization, subsequent changes in the configuaration can be applied using `terraform apply` without the need to re-run `terraform init`. In Terraform lingo this is also called "provisioning an infrastructure".

<!-- TOC --><a name="terraform-destroy"></a>
### `terraform destroy`
Finally, `terraform destroy` is the command used to remove the infrastructure created by `apply`. This is a non-trivial step because destroying an infrastructure manually can take time and it requires knowing the correct sequence of steps.

<!-- TOC --><a name="a-brief-introduction-to-the-terraform-language"></a>
## A brief introduction to the Terraform language

Terraform configuration uses the Terraform language  
> which is a rich language designed to be relatively easy for humans to read and write. The constructs in the Terraform language can also be expressed in JSON syntax, which is harder for humans to read and edit but easier to generate and parse programmatically. 

(quote from [https://developer.hashicorp.com/terraform/language/syntax/configuration](https://developer.hashicorp.com/terraform/language/syntax/configuration))

<!-- TOC --><a name="arguments-and-blocks"></a>
#### Arguments and blocks

The Terraform language syntax is built around two key syntax constructs: _arguments_ and _blocks_ (see [https://developer.hashicorp.com/terraform/language/syntax/configuration#identifiers](https://developer.hashicorp.com/terraform/language/syntax/configuration#identifiers)).

An argument assigns a value to a particular name:

    image_id = "abc123"

or

    region    = "us-west-2"
    
A block is a container for other content:

    provider "my_aws_provider" {
        access_key = "my-access-key"
        secret_key = "my-secret-key"
        region     = "us-west-2"
    }
	
>A block has a type (`resource`in this example). Each block type defines how many labels must follow the type keyword. The `resource` block type expects two labels, which are `aws_instance` and `example` in the example above. A particular block type may have any number of required labels, or it may require none as with the nested `network_interface` block type.

>Following the block type keyword and any labels, the block body is delimited by the curly brackets ({}). Within the block body, further arguments and blocks may be nested, creating a hierarchy of blocks and their associated arguments.

<!-- TOC --><a name="the-terraform-block"></a>
#### The `terraform` block 

The first block type that usually appears in a Terraform configuration file is the `terraform` block type. 
The `terraform` block type can be used to:

* specify the version of Terraform we want to use
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

The line `required_version = ">= 1.0.1"` tells Terraform that we need at least version Terraform 1.0.1. 

In the block `required_providers` we require the `aws` provider, we specify where to find it (in `source`) and what  the minimal allowed version is (`"~> 2.0"` means all versions that begin with `2`—see [the official documentation](https://developer.hashicorp.com/terraform/language/expressions/version-constraints) on how to specify version constraints).

Each Terraform provider comes with examples on how to use it: [https://registry.terraform.io/browse/providers](https://registry.terraform.io/browse/providers). Here's a minimal example from the [AWS provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs):

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# Create a VPC
resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"
}
```

You can save this configuration in a file `main.tf`, run `terraform init` and `terraform apply` and see what happens.

<!-- TOC --><a name="identifiers"></a>
#### Identifiers 
> Argument names, block type names, and the names of most Terraform-specific constructs like resources, input variables, etc. are all identifiers.


>Identifiers can contain letters, digits, underscores (_), and hyphens (-). The first character of an identifier must not be a digit, to avoid ambiguity with literal numbers.
([https://developer.hashicorp.com/terraform/language/syntax/configuration#identifiers](https://developer.hashicorp.com/terraform/language/syntax/configuration#identifiers))

For instance, in the `terraform` block

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


<!-- TOC --><a name="comments"></a>
#### Comments

Useful to know: [comments](https://developer.hashicorp.com/terraform/language/syntax/configuration#comments) can be

* single-lines beginning with a `#` or a `//`
* multi-line between `/*` and `*/`

<!-- TOC --><a name="terraform-variables-files"></a>
## Terraform variables files

It is customary in Terraform to create two files:

- `variables.tf`
- `terraform.tfvars`

The file `variables.tf` is used to define the variables that will be used in the Terraform configuration files and a typical block looks like:

```
variable "auth_url" {
  description = "OpenStack authentication URL"
}
```

A variable can have a default value:

```
variable "instance_count" {
  description = "Number of virtual machines"
  default = 3
}
```

The values assigned to the variables can be saved in `terraform.tfvars` in the format "variable = value". For instance the variable `auth_url` is assigned a value in the line
```
auth_url = "https://..."
```

Any value from `terraform.tfvars` will take precedence over the default value specified in `variables.tf`, so for instance if you specify `instance_count = 10` in `terraform.tfvars` then `instance_count` is going to have value `10` in the project. 

If a variable is defined in `variables.tf` but no value is present in `terraform.tfvars`, Terraform will prompt you to enter the value interactively. This can be useful for sensitive information such as passwords or API keys that you do not want to save in plain text files.

<!-- TOC --><a name="the-advantage-of-terraformtfvars"></a>
### The advantage of `terraform.tfvars`

Having an extra file for providing the values of variables promotes a clearer separation between configuration code and configuration data, which improves maintainability and makes it easy to switch between different sets of variable values for different scenarios.

Note that `terraform.tfvars` is the default file where Terraform looks for variables values. You can call it something else, like `my_vars.tfvars`, but you'll need to specify the file name explicitly by using the `-var-file` option with Terraform commands, like `terraform apply -var-file=my_vars.tfvars`.

<!-- TOC --><a name="how-to-generate-terraform-configuration-files"></a>
## How to generate Terraform configuration files

Once you know what you need for your infrastructure, there are many options for getting help in generating Terraform configuration files:  

 - use the [provider's documentation](https://registry.terraform.io/browse/providers)
 - large language models such as ChatGPT can be very useful for generating and debugging configuration files
 - I haven't used this yet but it exists: the [reverse Terraform](https://github.com/GoogleCloudPlatform/terraformer) to get Terraform file from an existing infrastructure



<!-- TOC --><a name="infrastructure-as-code-with-automated-dependency-management"></a>
## Infrastructure as code with automated dependency management

Terraform relies on a series of blocks and arguments that can be spread across different files. Does the order of these chunks of configuration within files matter? Does the naming of the files matter? No, the naming and order of the files does not matter and Terraform takes care of dependencies and order of execution.

This is precisely Terraform's main strength: **infrastructure as code with automated dependency management**

Terraform excels in abstracting infrastructure as code, liberating users from the burden of manually specifying the order of resource creation and their interdependencies. It automatically resolves dependencies, ensuring a consistent and reliable deployment process. This strength simplifies infrastructure management, reduces human error, and enhances the overall stability and reproducibility of infrastructure deployments.


<!-- TOC --><a name="recap"></a>
## Recap

To get started with Terraform:
1. install Terraform on your machine
2. create three files: `main.tf`, `variables.tf`, and `terraform.tfvars` containing respectively infrastructure configuration, variables declarations, and variables values. Fill these files with code from your [provider's documentation](https://registry.terraform.io/browse/providers).
4. run the command `terraform init` followed by `terraform apply` in the same directory where you stored the configuration files
5. when you're done run the command `terraform destroy` to avoid avoid unnecessary resource consumption

Terraform's power lies in its ability to transform complex infrastructure requirements into simple and declarative code, letting users focus on what infrastructure should look like rather than how to create it and how to manage dependencies. This simplifies infrastructure management and enhances the efficiency and reliability of infrastructure operations.


<!-- TOC --><a name="happy-terraforming"></a>
## Happy Terraforming!
 


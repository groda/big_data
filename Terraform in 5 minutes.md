# Terraform in 5 minutes

Terraform is a powerful and popular tool for infrastructure provisioning and management. Its declarative syntax and infrastructure-as-code approach make it concise and efficient for defining and managing infrastructure resources across various cloud providers.

## Install Terraform

Terraform is an installable tool that you can set up on your computer.

The installation process is typically straightforward. Here are step-by-step instructions for installing Terraform on Mac/Linux or Windows operating systems: 
[https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform).

The software just installed is also known as the _Terraform core_.

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

## Introduction to Terraform providers

Terraform is an infrastructure as code tool that enables the provisioning and management of resources across different cloud and infrastructure _providers_ by utilizing provider plugins as the central mechanism for interfacing with those providers.

In simple terms, a Terraform provider is a plugin that allows Terraform to interact with a specific infrastructure or service provider, such as AWS, Azure, or GCP. It provides the necessary functionality to create, manage, and delete resources within that provider's environment using Terraform configuration files.


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

### A basic provider block example

Here's a basic example of a Terraform provider block for AWS:

```
provider "aws" {
  access_key = "your-access-key"
  secret_key = "your-secret-key"
  region     = "us-west-2"
}
```

In this example, the provider block configures the AWS provider. It specifies the access key, secret key, and region to authenticate and connect to the AWS services. With this configuration, you can proceed to define and manage AWS resources using Terraform.

## Terraform project and configuration files

A project is defined in one or more Terraform configuration files. These are text files ending with `.tf` that resemble JSON files.

Terraform tutorials and learning environments can be found at [https://developer.hashicorp.com/terraform/tutorials]().

You can install Terraform on your machine or use Terraform's online learning environments to try out an initial demo. The main commands for launching a project with Terraform are:

```
terraform init
terraform apply 
terraform destroy
```

With `terraform init` terraform one initializes the project. This includes downloading the required Terraform plugins. Generally one only needs to run `terraform init` once for a given Terraform project or when significant changes are made to the configuration, such as adding new providers or modifying backend configurations. 

After the initial initialization, subsequent changes in the configuaration can be applied using `terraform apply` without the need to re-run `terraform init`. In Terraform lingo this is also called "provisioning an infrastructure".

Finally, `terraform destroy` is the command used to remove the infrastructure created by `apply`. This is a non-trivial step because destroying an infrastructure manually can take time and it requires knowing the correct sequence of steps.

## A brief introduction to the Terraform language

Terraform configuration uses the Terraform language  
> which is a rich language designed to be relatively easy for humans to read and write. The constructs in the Terraform language can also be expressed in JSON syntax, which is harder for humans to read and edit but easier to generate and parse programmatically. 

(quote from [https://developer.hashicorp.com/terraform/language/syntax/configuration](https://developer.hashicorp.com/terraform/language/syntax/configuration))

#### Arguments and blocks

The Terraform language syntax is built around two key syntax constructs: _arguments_ and _blocks_ (see [https://developer.hashicorp.com/terraform/language/syntax/configuration#identifiers](https://developer.hashicorp.com/terraform/language/syntax/configuration#identifiers)).

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

#### The `terraform` block 

The first block type that usually appears in a Terraform configuration file is the `terraform` block type. 
The `terraform` block type can be used to:

* specifying the version of Terraform we want to use
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

In the block `required_providers` we require the `aws` provider, we specify where to find it (in `source`) and what is the minimal allowed version (`"~> 2.0"` means all versions that begin with `2`—see [the official documentation](https://developer.hashicorp.com/terraform/language/expressions/version-constraints) on how to specify version constraints).

Each Terraform provider comes with examples on how to use it: [https://registry.terraform.io/browse/providers](https://registry.terraform.io/browse/providers).

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


#### Comments

Useful to know: [comments](https://developer.hashicorp.com/terraform/language/syntax/configuration#comments) can be

* single-lines beginning with a `#` or a `//`
* multi-line between `/*` and `*/`

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

The values assigned to the variables are saved in `terraform.tfvars` in the format "variable = value". For instance the variable `auth_url` is assigned a value in the line
```
auth_url = "https://..."
```

## A note on ordering of files and blocks

Terraform relies on a series of blocks and arguments that can be spread across different files. Does the order of these chunks of configuration within files matter? Does the naming of the files matter? 

The answer is given in ["can we order .tf files in terraform?"](https://stackoverflow.com/questions/74441521/can-we-order-tf-files-in-terraform):
> Terraform does not make any use of the order of .tf files or of the declarations in those files. Instead, Terraform decodes all of the blocks across all of your files and analyzes them to look for references between objects.

So, no the order does not mattewr and Terraform takes care of dependencies and order of execution.

## Happy Terraforming!
 


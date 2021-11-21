# CDISC-SDMX
Automation of CDISC outputs using SDMX

## Project goals

The goal of this project is a proof-of-concept to create a model of a clinical trial analysis using SDMX and to  transform that model into CDISC (ADaM and ARM) compliant outputs.

## Research questions

Key research questions for this project are:

- Demonstrate how SDMX can be used to describe typical clinical trial analyses based on the [CDISC ADaM Examples in Commonly used Statistical Analysis Methods](https://www.cdisc.org/standards/foundational/adam/adam-examples-commonly-used-statistical-analysis-methods) 
- Can a domain specific language (DSL) be created that will allow analyses to be specified in a sufficiently high-level declarative language that supports easy human review and validation, which can be programmatically converted to SDMX
- Can SDMX annotations be used to automate a mapping to CDISC ADaM datasets. A stretch goal is to explore if this mechanism could be used for creation of CDISC ARM metadata.       


## How to run the project

The easiest way to run the project is to create and account with [gitpod.io](https://gitpod.io)

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/metadatadriven/CDISC-SDMX)


## Runtime environment

- The SDTM-to-CDISC programming is implemented in Python 3
- [Powershell Core](https://github.com/PowerShell/PowerShell) (i.e. Pwsh running on Ubuntu) is the build environment
- The operating system is Ubuntu docker image that is running in [Gitpod](https://gitpod.io/)

The environment is detailed in the `.gitpod.Dockerfile` and `.gitpod.yml` files in the root of the repo

## Directory structure

This repo directory structure has been created to be compatable with the [Phuse Script Metadata Recommendations for Sharing](https://phuse.s3.eu-central-1.amazonaws.com/Deliverables/Standard+Analyses+and+Code+Sharing/Script+Metadata+Recommendation+for+Sharing.pdf)

There are some additional directories that are required for this project.

The Phuse standard directories are:

- ./conf – store any configuration files
- ./data – datasets used by scripts
- ./lib - script libraries, macros or utility programs
- ./log – store the log files; this starts empty.
- ./pkg – store R or other language packages
- ./script – store script files
- ./output – store output files such as dataset, reports, graphs, etc; this starts empty.

Additional directories:

- ./ref - reference material including standards, lookup tables, etc.
- ./docs - documentation


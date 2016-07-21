# Intellij 2016.1.3 RPM built for RHEL 6.5

**Description**:  

    The most intellijent java IDE

## Dependencies

    Currently, only RHEL and CentOS 6.5 have been tested.  
    You need to install and set up your JAVA_HOME

## Installation
 
### Build the RPM using Vagrant

1. Once the repo has been cloned, run "vagrant up" to create the build VM
2. Run "vagrant ssh" to connect
3. CD to ~/rpmbuild
4. Run "rpmbuild -ba SPECS/intellij.spec"

### Build the RPM on a server
1. Once the repo has been cloned, run "sh ./bootstrap.sh"
2. CD to ~/rpmbuild
3. Run "rpmbuild -ba SPECS/intellij.spec"

### Install the RPM

Install the built RPM by running "sudo yum install RPMS/x86_64/intellij-2016.1.3-1.el6.x86_64.rpm .rpm"

## Configuration

Edit the SPEC ($HOME/rpmbuild/SPEC/intellij.spec) file to make necessary changes to the build configuration.


## Known issues


## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## Getting involved

To contribute, please see [CONTRIBUTING](CONTRIBUTING.md).

----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)

----

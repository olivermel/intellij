%global _version	2016.1.3


Name:       	intellij
Version: 		%{_version}
Release: 		1%{?dist}
Summary:		IntelliJ IDEA - The Most Intelligent Java IDE

Group:			Development/Tools
License:		IntelliJ IDEA Commercial
URL:			https://download.jetbrains.com
Source:			https://download.jetbrains.com/idea/ideaIC-2016.1.3.tar.gz

Provides:		intellij == 2016.1.3


%description
IntelliJ IDEA - The Most Intelligent Java IDE that brings the whole range of precise developers tools, all tied together to create the convenient development environment


###############################################################################################################################################################
# Build requirements

BuildRoot: %(mktemp -ud %{_tmppath}/build/%{name}-%{version}-%{release}-XXXXXX)


###############################################################################################################################################################
#PREP and SETUP
# The prep directive removes existing build directory and extracts source code so we have a fresh code base .....-n flag where present, defines the name of the directory

%prep
%setup -qc
echo $PWD
cd idea-IC-145.1617.8/bin
bash -x idea.sh

###############################################################################################################################################################
%build

make

###############################################################################################################################################################
%install

%make_install

###############################################################################################################################################################
%files


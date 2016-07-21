%global __os_install_post %{nil}
%global _version	2016.1.3
%global prefix		/usr/local
%global sharedir	/usr/share
%global	optdir		/opt/idea


Name:		       	intellij
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


###############################################################################################################################################################
%install

echo $PWD
mkdir -p %{buildroot}%{optdir}
mkdir -p %{buildroot}%{prefix}/bin/idea
mkdir -p %{buildroot}%{sharedir}/pixmaps

cp -a %{_builddir}/intellij-2016.1.3/idea-IC-145.1617.8/ %{buildroot}%{optdir}
mkdir -p %{buildroot}%{sharedir}/applications


echo '[Desktop Entry]' 					>> %{buildroot}%{sharedir}/applications/idea.desktop
echo 'Name=IntelliJ IDEA' 				>> %{buildroot}%{sharedir}/applications/idea.desktop
echo 'Type=Application'					>> %{buildroot}%{sharedir}/applications/idea.desktop
echo 'Exec=idea.sh'					>> %{buildroot}%{sharedir}/applications/idea.desktop
echo 'Terminal=false'					>> %{buildroot}%{sharedir}/applications/idea.desktop
echo 'Icon=idea'					>> %{buildroot}%{sharedir}/applications/idea.desktop
echo 'Comment=Integrated Development Environment'	>> %{buildroot}%{sharedir}/applications/idea.desktop
echo 'NoDisplay=false'					>> %{buildroot}%{sharedir}/applications/idea.desktop
echo 'Categories=Development;IDE;' 			>> %{buildroot}%{sharedir}/applications/idea.desktop
echo 'Name[en]=IntelliJ IDEA'				>> %{buildroot}%{sharedir}/applications/idea.desktop

cd %{buildroot}%{sharedir}/applications

cd %{buildroot}%{prefix}/bin
ln -s %{optdir}/idea-IC-145.1617.8/bin/idea.sh %{buildroot}%{prefix}/bin/idea.sh
cp %{buildroot}%{optdir}/idea-IC-145.1617.8/bin/idea.png   %{buildroot}%{prefix}/bin/idea.png
###############################################################################################################################################################


###############################################################################################################################################################
%files
%defattr(-,root,root,-)

/opt/idea/idea-IC-145.1617.8
/usr/share/applications
/usr/local/bin/idea.png
/usr/local/bin/idea.sh

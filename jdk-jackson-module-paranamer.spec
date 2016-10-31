Name     : jdk-jackson-module-paranamer
Version  : 2.6.5
Release  : 4
URL      : https://repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-paranamer/2.6.5/jackson-module-paranamer-2.6.5.jar
Source0  : https://repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-paranamer/2.6.5/jackson-module-paranamer-2.6.5.jar
Source1  : https://repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-paranamer/2.6.5/jackson-module-paranamer-2.6.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-jackson-module-paranamer-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-jackson-module-paranamer package.
Group: Data

%description data
data components for the jdk-jackson-module-paranamer package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/jackson-module-paranamer.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/jackson-module-paranamer.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/jackson-module-paranamer.xml \
%{buildroot}/usr/share/maven-poms/jackson-module-paranamer.pom \
%{buildroot}/usr/share/java/jackson-module-paranamer.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/jackson-module-paranamer.jar
/usr/share/maven-metadata/jackson-module-paranamer.xml
/usr/share/maven-poms/jackson-module-paranamer.pom

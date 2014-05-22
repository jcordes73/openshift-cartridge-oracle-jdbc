Name: openshift-cartridge-oracle-jdbc
Version: 1.0.0
Release: 1
Summary: OpenShift cartridge which embeds Oracle JDBC configuration in EAP 6
License: LGPL
Group: Applications/Systems
autoprov: yes
autoreq: yes
BuildRoot: /NotBackedUp/jcordes/openshift-cartridge-oracle-jdbc/target/rpm/openshift-cartridge-oracle-jdbc/buildroot

%description
OpenShift cartridge which embeds Oracle JDBC configuration in EAP 6

%install
if [ -e $RPM_BUILD_ROOT ];
then
  mv /NotBackedUp/jcordes/openshift-cartridge-oracle-jdbc/target/rpm/openshift-cartridge-oracle-jdbc/tmp-buildroot/* $RPM_BUILD_ROOT
else
  mv /NotBackedUp/jcordes/openshift-cartridge-oracle-jdbc/target/rpm/openshift-cartridge-oracle-jdbc/tmp-buildroot $RPM_BUILD_ROOT
fi

%files
%defattr(755,-,root,-)
 "/usr/libexec/openshift/cartridges/oraclejdbc"
 "/usr/share/jbossas/modules"

%post
CLASSPATH="/usr/share/jbossas/modules/system/layers/base/org/picketbox/main/picketbox.jar:/usr/share/jbossas/modules/system/layers/base/org/jboss/logging/main/jboss-logging.jar"
password=`java -cp ${CLASSPATH} org.picketbox.datasource.security.SecureIdentityLoginModule tiger | cut -d' ' -f3`
sed "s/password=/password=$password/g" /usr/libexec/openshift/cartridges/oraclejdbc/bin/install > /usr/libexec/openshift/cartridges/oraclejdbc/bin/install.new
mv /usr/libexec/openshift/cartridges/oraclejdbc/bin/install.new /usr/libexec/openshift/cartridges/oraclejdbc/bin/install

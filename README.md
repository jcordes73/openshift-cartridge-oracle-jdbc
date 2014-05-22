openshift-cartridge-oracle-jdbc
===============================

An OpenShift cartridge for provisioning a Oracle JDBC driver an a Oracle datasource

- Download Oracle JDBC driver

http://www.oracle.com/technology/software/tech/java/sqlj_jdbc/index.html

- Copy Oracle JDBC driver

cp ojdbc6-<version>.jar src/main/resources/modules/com/oracle/jdbc/main

- Build

mvn clean install

- Install

scp target/rpm/openshift-cartridge-oracle-jdbc/RPMS/noarch/openshift-cartridge-oracle-jdbc-<cartridge-version>-1.noarch.rpm root@<openshift-node-ip>:/tmp

rpm -ivh openshift-cartridge-oracle-jdbc-<cartridge-version>.rpm

oo-admin-cartridge -a install -s /usr/libexec/openshift/cartridges/oraclejdbc
oo-admin-broker-cache --clear --console

- Remove cartridge

rpm -e openshift-cartridge-oracle-jdbc-<cartridge-version>-1.noarch

oo-admin-cartridge -l
oo-admin-cartridge -a erase --name oraclejdbc --version <version> --cartridge_version <cartridge-version>

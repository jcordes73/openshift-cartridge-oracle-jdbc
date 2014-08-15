# openshift-cartridge-oracle-jdbc

## Description

An OpenShift cartridge for provisioning a Oracle JDBC driver and a Oracle datasourc on JBoss EAP 6 cartridge.

## Adding Oracle JDBC driver

First you have to download the Oracle JDBC driver from http://www.oracle.com/technology/software/tech/java/sqlj_jdbc/index.html. It is not included in the project due to licensing.

Afterwards copy the Oracle JDBC driver into the project

```bash
cp ojdbc6.jar src/main/resources/modules/com/oracle/jdbc/main
```

## Build

For building the project you need Maven installed. I have used Maven 3.0.5.

Just execute (after setting mvn on the PATH):

```bash
mvn clean install
```

Below you can find information on what properties are used and can be overriden by passing system properties (i.e. using -D{name})

|Property|Default|
|--------|-------|
|oracle.db.host|MYHOST|
|oracle.db.port|MYHOST|
|oracle.db.schemaName|SID|
|oracle.db.username|scott|
|oracle.db.password|tiger|
|rpm.key.name|D3AABAF5|
|rpm.key.passphrase|redhat|

## Install

After the build you need to copy the resulting RPM to the target OpenShift node (for convenience I have used the /tmp directory):

```bash
scp target/rpm/openshift-cartridge-oracle-jdbc/RPMS/noarch/openshift-cartridge-oracle-jdbc-${project.version}-1.noarch.rpm root@${openshift.node.ip}:/tmp
```

then install it using

```bash
rpm -ivh openshift-cartridge-oracle-jdbc-${project.version}.rpm
```

After the RPM has been installed successfully you need to install the cartridge like this:

```bash
oo-admin-cartridge -a install -s /usr/libexec/openshift/cartridges/oraclejdbc
```

The last installation step is to clear the caches on the OpenShift Broker:

```bash
oo-admin-broker-cache --clear --console
```

## Remove

To remove the cartridge you first need to remove the package installed via RPM:

```bash
rpm -e openshift-cartridge-oracle-jdbc-${project.version}-1.noarch
```

The next command will list all available OpenShift cartridges along with it's versions and cartridge-versions:

```bash
oo-admin-cartridge -l
```

Finally you delete the cartridge using this command

```bash
oo-admin-cartridge -a erase --name oraclejdbc --version ${oracle.jdbc.version} --cartridge_version ${project.version}
```

## Cartridge creation

When creating the cartridge you can pass the following environment variables to override the defaults specified in the pom.xml earlier:

|Name|Default (pom.xml)|
|----|------------------|
|OPENSHIFT_ORACLEJDBC_JNDINAME|oracle.jdbc.jndiName|
|OPENSHIFT_ORACLEJDBC_HOST|oracle.db.host|
|OPENSHIFT_ORACLEJDBC_PORT|oracle.db.port|
|OPENSHIFT_ORACLEJDBC_SCHEMANAME|oracle.db.schemaName|
|OPENSHIFT_ORACLEJDBC_USERNAME|oracle.db.username|
|OPENSHIFT_ORACLEJDBC_PASSWORD|oracle.db.password|

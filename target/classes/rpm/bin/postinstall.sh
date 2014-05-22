CLASSPATH="/usr/share/jbossas/modules/system/layers/base/org/picketbox/main/picketbox.jar:/usr/share/jbossas/modules/system/layers/base/org/jboss/logging/main/jboss-logging.jar"
password=`java -cp ${CLASSPATH} org.picketbox.datasource.security.SecureIdentityLoginModule tiger | cut -d' ' -f3`
sed "s/password=/password=$password/g" /usr/libexec/openshift/cartridges/oraclejdbc/bin/install > /usr/libexec/openshift/cartridges/oraclejdbc/bin/install.new
mv /usr/libexec/openshift/cartridges/oraclejdbc/bin/install.new /usr/libexec/openshift/cartridges/oraclejdbc/bin/install
#!/bin/bash
#zookeeper server
~/Downloads/kafka_2.13-3.3.1/bin/zookeeper-server-start.sh ~/Downloads/kafka_2.13-3.3.1/config/zookeeper.properties;


#kafka server
~/Downloads/kafka_2.13-3.3.1/bin/kafka-server-start.sh ~/Downloads/kafka_2.13-3.3.1/config/server.properties;


#cmak server:
cd ~/Downloads/CMAK/target/universal/cmak-3.0.0.7/;
~/Downloads/CMAK/target/universal/cmak-3.0.0.7/bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080;
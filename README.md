# GPSS configuration istruction

The following repository contains two folders: gpssfiles and pythonparser </br>
The first one contains the configuration files to start gpss server and gpsscli clients </br>
The other one contains the python script to generate the gpsscli mapping starting from the relative json files 

## Prerequisites

the only prerequisites needed is to enable gpss extension from the database you want to use:

```
newtest=# create extension gpss;
CREATE EXTENSION
```

## Starting gpss server

Gpss server just takes in input a configuration file where you need to specify host and port for gpss and gpfdist servers (you can find it in ./gpssfiles/gpss.conf </br>

```
{
    "ListenAddress": {
        "Host": "172.21.0.5",
        "Port": 50009,
        "SSL": false
    },
    "Gpfdist": {
        "Host": "172.21.0.5",
        "Port": 50010
    }
}
```
```
[gpadmin@mdw gpss]$ gpss gpss.conf 
20210123 13:15:12.40350,47377,info,using config file: gpss.conf
20210123 13:15:12.40357,47377,info,config file content:
{"ListenAddress":{"Host":"172.21.0.5","Port":50009,"Certificate":{"CertFile":"","KeyFile":"","CAFile":""}},"Gpfdist":{"Host":"172.21.0.5","Port":50010,"ReuseTables":true,"Certificate":{"CertFile":"","KeyFile":"","CAFile":""},"BindAddress":"0.0.0.0"},"logging":{}}
20210123 13:15:12.40361,47377,info,gpss-listen-address-prefix: 172.21.0.5:50009
20210123 13:15:12.40371,47377,info,librdkafka version: 1.4.2(10402ff)
20210123 13:15:12.40388,47377,info,gpfdist listening on 0.0.0.0:50010
20210123 13:15:12.40396,47377,info,gpss listening on 172.21.0.5:50009
```

## Submitting and starting a new job with gpsscli

gpsscli takes a configuration file as well like the ones in gpssfiles folder. At the moment we have mapping for customer, subscriber and usage</br>
Configuration file for gpsscli takes in input greenplum and kafka connection parameters as well as the mapping </br>

You can submit and run it in this way: </br>

```
gpsscli submit --name task-customer --gpss-port 50009 --gpss-host 172.21.0.5 ./task-customer-new.yaml
gpsscli start task-customer --gpss-port 50009 --gpss-host 172.21.0.5
```

## Ingesting data on kafka

You can use as an example the standard kafka-console producer to ingest the data inside the topic:

```
./kafka-console-producer.sh --broker-list localhost:9092 --topic customertopic  < customer_subscriber_transaction2.json 
```

You shoud see then the greenplum table populated

## Ingesting data on kafka








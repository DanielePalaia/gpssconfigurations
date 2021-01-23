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

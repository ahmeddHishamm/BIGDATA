# Hive

Linux must be the OS used to be able to work on this project

while running docker desktop

Navigate inside the Hive directory on your local and run the single docker compose command to create and start all services required by our Hive cluster.

1- $ docker-compose up 


2- $ docker exec -it hive-server /bin/bash

Navigate to the Arsenal directory on the hive-server container.

3- 
root@dc86b2b9e566:/opt# ls

hadoop-2.7.4  hive

root@dc86b2b9e566:/opt# cd ..

root@dc86b2b9e566:/# ls

bin  boot  dev arsenal  entrypoint.sh  etc  hadoop-data  home  lib  
lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  
var

root@dc86b2b9e566:/# cd arsenal/

----------------------------------------

On the hive-server, launch hive to verify the contents of the arsenal table.

4- root@df1ac619536c:/arsenal# hive

hive> show databases;

OK

default

arsenalclean

hive> use arsenalclean;

OK

hive> show tables;

OK

arsenalc


hive> select * from arsenalc limit 10;

----------------------------------------------

In a new terminal, execute below command to stop all docker containers.

7- $ docker-compose down





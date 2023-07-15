Task 3 

Docker File for Postgres

FROM postgres:latest
ENV POSTGRES_PASSWORD=mysecretpassword
COPY ./inputfiles/cleansd.txt /tmp
ADD ./scripts/postgrescreatetable.sql /docker-entrypoint-initdb.d/


#docker build -t  my-db:1.0 .

#docker network create mynetwork

root@vaibhavdev:~# docker run -d -t --network mynetwork --name my-dbcontainer1 my-db:1.0

Test container 
==================

docker exec -it my-dbcontainer1 bash

root@da2211249319:/# su - postgres
postgres@da2211249319:~$ psql
psql (15.3 (Debian 15.3-1.pgdg120+1))
Type "help" for help.

postgres=# \c postgres
You are now connected to database "postgres" as user "postgres".
postgres=# select * from students;

                      ^
postgres=# select * from student;
   name    | password | hostel  | room | mess | messpref
-----------+----------+---------+------+------+----------
 Dodi      | password | GarnetA |    0 |    1 |        1
 Elbertine | password | GarnetA |    0 |    3 |        1
 Trish     | password | GarnetA |    1 |    3 |        1
 Trenna    | password | GarnetA |    1 |    1 |        1
 Teddy     | password | GarnetA |    2 |    1 |        1
 Dynah     | password | GarnetB |    2 |    3 |        1
 Inga      | password | GarnetB |    3 |    1 |        1
 Selena    | password | GarnetB |    3 |    2 |        1
 Carleen   | password | GarnetB |    4 |    2 |        1
 Adore     | password | GarnetB |    2 |    2 |        1
 Gwenneth  | password | GarnetB |    2 |    3 |        1
 Meris     | password | Opal    |    3 |    3 |        1
 Laurel    | password | Opal    |    3 |    3 |        1
 Kathryne  | password | Opal    |    4 |    1 |        1
 Maribelle | password | Agate   |    4 |    2 |        1
 Dottie    | password | Agate   |    0 |    2 |        1
 Josephina | password | Agate   |    0 |    3 |        1
 Betsey    | password | Agate   |    3 |    2 |        1
 Reyna     | password | Agate   |    4 |    3 |        1
 Minnnie   | password | Agate   |    4 |    3 |        1
(20 rows)



root@da2211249319:/var/log/postgresql# apt-get update
G
root@da2211249319:/var/log/postgresql# apt-get install net-tools

root@da2211249319:/var/log/postgresql# netstat -an | grep -i 54
tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN
tcp6       0      0 :::5432                 :::*                    LISTEN
unix  2      [ ACC ]     STREAM     LISTENING     93356    /var/run/postgresql/.s.PGSQL.5432

Dockerfile for App container 


FROM ubuntu:latest
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:
RUN mkdir /root/inputfiles
RUN mkdir /root/scripts
RUN mkdir /root/serverscripts
RUN mkdir /root/clientscripts
COPY ./inputfiles /root/inputfiles
COPY ./scripts /root/scrip1ts
COPY ./serverscripts /root/severscripts
COPY ./clientscripts /root/clientcripts
RUN apt update  && apt-get install -y python3 libpq-dev python-dev-is-python3 python3-psycopg2 net-tools


docker build -t  my-app:1.0 .


docker run -d -t --network mynetwork --name my-appcontainer1 my-app:1.0

root@vaibhavdev:~# docker exec -it my-appcontainer1 bash


Testing the connection 

root@90a1dfc5a803:~/serverscripts# python3 connectDB.py
User:Dodi
User:  Dodi
Enter Password:password
Password is :  password
[('Dodi', 'password', 'GarnetA', 0, 1, 1)]
password
Both strings are  equal
root@90a1dfc5a803:~/serverscripts#

Docker Compose - 

docker login --username kanagalekarv2511 --password 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 ghcr.io

 docker build . -t ghcr.io/kanagalekarv2511/sysadmtask3myapp

docker push ghcr.io/kanagalekarv2511/sysadmtask3myapp

FROM postgres:latest
ENV POSTGRES_PASSWORD=mysecretpassword
COPY ./inputfiles/cleansd.txt /tmp
ADD ./scripts/postgrescreatetable.sql /docker-entrypoint-initdb.d/
RUN apt update && apt-get install -y  net-tools vim

docker build . -t ghcr.io/kanagalekarv2511/sysadmtask3mydb

docker push ghcr.io/kanagalekarv2511/sysadmtask3mydb


version: '2.19.1'
services:
      my-app:
       image: ghcr.io/kanagalekarv2511/sysadmtask3myapp
       tty: true
       stdin_open: true
       volumes:
        - /data/Adore
        - /data/Betsey
        - /data/Carleen
        - /data/Dodi
        - /data/Dottie
        - /data/Dynah
        - /data/Elbertine
        - /data/Gwenneth
        - /data/Inga
        - /data/Josephina
        - /data/Kathryne
        - /data/Laurel
        - /data/Maribelle
        - /data/Meris
        - /data/Minnnie
        - /data/Reyna
        - /data/Selena
        - /data/Teddy
        - /data/Trenna
        - /data/Trish
      my-db:
       image: ghcr.io/kanagalekarv2511/sysadmtask3mydb
       container_name: mydbcontainer
       ports:
       - 5432:5432

docker compose -f docker-compose-sysadmtask3.yaml up -d 





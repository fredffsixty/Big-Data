create table passengers (id int, survived int, class int, name varchar(64), sex varchar(8), age float, sibsp int, parch int, ticket varchar(20), fare float, cabin varchar(20), embarked char(1)) row format serde 'org.apache.hadoop.hive.serde2.OpenCSVSerde' TBLPROPERTIES ("skip.header.line.count"="1");

load data local inpath '/home/cloudera/InputMapReduce/titanic.csv' into table passengers;

create table passengers_qualified (id int, survived int, class int, name varchar(64), sex varchar(8), age float, sibsp int, parch int, ticket varchar(20), fare float, cabin varchar(20), embarked char(1)) row format delimited fields terminated by '\t';

insert overwrite table passengers_qualified select * from passengers;


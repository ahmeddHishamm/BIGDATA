create database if not exists ArsenalClean;
use ArsenalClean;
create external table if not exists ArsenalC (
  username string, 
  tweet string, 
  likes_count int, 
  retweets_count int
)
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/ArsenalClean.db/ArsenalC';
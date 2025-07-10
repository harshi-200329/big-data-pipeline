CREATE KEYSPACE IF NOT EXISTS iot_data
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE iot_data;

CREATE TABLE IF NOT EXISTS sensor_readings (
    sensor_id text,
    reading_date date,
    reading_time timestamp,
    r1 double,
    r2 double,
    r3 double,
    r4 double,
    r5 double,
    r6 double,
    r7 double,
    r8 double,
    temperature double,
    humidity double,
    PRIMARY KEY ((sensor_id, reading_date), reading_time)
) WITH CLUSTERING ORDER BY (reading_time ASC);

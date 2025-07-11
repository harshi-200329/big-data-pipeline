# big-data-pipeline
Ingestion, Storage, Processing, Cloud Integration
# 📊 Big Data Pipeline with Redis and Cassandra

This project demonstrates a simple big data ingestion pipeline using **Redis**, **Cassandra**, **Docker**, and **Python**.


##  Project Structure

big-data-pipeline/
├── data/ # Dataset (Iot_300k.csv)
├── ingestion/ # Python ingestion script
│ └── cassandra_ingest.py
├── docker-compose.yml # Defines Redis & Cassandra services
├── README.md # Project documentation
└── docs/ # (Optional) Screenshots or extra docs



##  Requirements

- Docker & Docker Compose installed
- Python 3 installed
- Python packages: `cassandra-driver`

Install dependencies:
```bash
pip install cassandra-driver


## How to Run
1️. Start Redis & Cassandra
bash
Copy
Edit
docker-compose up -d
Verify containers:

bash
Copy
Edit
docker ps


2️. Create Keyspace & Table in Cassandra
Enter Cassandra shell:

bash
Copy
Edit
docker exec -it cassandra cqlsh
Run in cqlsh:

sql
Copy
Edit
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



3️. Run the Python Ingestion Script
bash
Copy
Edit
python ingestion/cassandra_ingest.py



4️. Verify Data in Cassandra
bash
Copy
Edit
docker exec -it cassandra cqlsh
USE iot_data;
SELECT * FROM sensor_readings LIMIT 5;




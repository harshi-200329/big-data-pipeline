from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
import csv
from datetime import datetime, date

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('iot_data')

insert_stmt = session.prepare("""
    INSERT INTO sensor_readings (sensor_id, reading_date, reading_time,
    r1, r2, r3, r4, r5, r6, r7, r8, temperature, humidity)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""")

with open('data/Iot_300k.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    batch = BatchStatement()
    for i, row in enumerate(reader):
        batch.add(insert_stmt, (
            str(row['id']),
            date.today(),
            datetime.utcnow(),
            float(row['R1']),
            float(row['R2']),
            float(row['R3']),
            float(row['R4']),
            float(row['R5']),
            float(row['R6']),
            float(row['R7']),
            float(row['R8']),
            float(row['Temp']),
            float(row['Humidity'])
        ))

        if i % 100 == 0:
            session.execute(batch)
            batch.clear()

    if batch:
        session.execute(batch)

cluster.shutdown()

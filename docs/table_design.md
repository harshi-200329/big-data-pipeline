# Table Design for Sensor Time-Series Data

## PostgreSQL Table Schema

```sql
CREATE TABLE sensor_readings (
    id SERIAL PRIMARY KEY,
    sensor_id INTEGER NOT NULL,
    reading_time TIMESTAMP NOT NULL,
    r1 DOUBLE PRECISION,
    r2 DOUBLE PRECISION,
    r3 DOUBLE PRECISION,
    r4 DOUBLE PRECISION,
    r5 DOUBLE PRECISION,
    r6 DOUBLE PRECISION,
    r7 DOUBLE PRECISION,
    r8 DOUBLE PRECISION,
    temperature DOUBLE PRECISION,
    humidity DOUBLE PRECISION
);

CREATE INDEX idx_sensor_time ON sensor_readings(sensor_id, reading_time);

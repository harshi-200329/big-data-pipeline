import pandas as pd
import redis

# Load CSV
df = pd.read_csv("Iot_300k.csv").head(1000)

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Insert data as hashes
for idx, row in df.iterrows():
    key = f"sensor:{row['id']}:{idx}"
    data = {
        "time": str(row["time"]),
        "R1": str(row["R1"]),
        "R2": str(row["R2"]),
        "R3": str(row["R3"]),
        "R4": str(row["R4"]),
        "R5": str(row["R5"]),
        "R6": str(row["R6"]),
        "R7": str(row["R7"]),
        "R8": str(row["R8"]),
        "Temp": str(row["Temp"]),
        "Humidity": str(row["Humidity"])
    }
    r.hset(key, mapping=data)

print("Ingestion complete.")

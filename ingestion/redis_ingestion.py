import redis
import pandas as pd

# Load CSV
df = pd.read_csv("data/Iot_300k.csv")

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Batch config
BATCH_SIZE = 1000

count = 0

for batch_start in range(0, len(df), BATCH_SIZE):
    batch_df = df.iloc[batch_start : batch_start + BATCH_SIZE]

    pipeline = r.pipeline()

    for idx, row in batch_df.iterrows():
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
            "Humidity": str(row["Humidity"]),
        }

        pipeline.hset(key, mapping=data)

    pipeline.execute()
    count += len(batch_df)
    print(f"Inserted {count} records (batch).")

print("Batch ingestion complete.")

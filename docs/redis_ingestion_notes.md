# Redis Ingestion Notes

**Dataset:** Iot_300k.csv

**Steps:**
- Started Redis container via Docker
- Ingested dataset using Python script
- Verified keys in Redis
- Performed CRUD operations

**Docker Commands:**
docker run --name redis-iot -p 6379:6379 -d redis  
docker exec -it redis-iot redis-cli

**Verification Commands:**
keys *  
hgetall sensor:0:0  
hset sensor:0:0 Temp 27.5  
del sensor:0:0

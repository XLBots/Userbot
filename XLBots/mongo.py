import config
import motor.motor_asyncio

print("[INFO] connecting to database") 

DB_URI = config.MONGO_DB_URI

MongoDB = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)

db = MongoDB.program

print("[INFO] database connection successfully!") 

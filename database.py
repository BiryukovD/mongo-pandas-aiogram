import pymongo
from config import DB_HOST, DB_PORT, DB_NAME

client = pymongo.MongoClient(f'mongodb://{DB_HOST}:{DB_PORT}/{DB_NAME}')
db = client.test_db

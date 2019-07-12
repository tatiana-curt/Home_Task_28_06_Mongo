from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)

netology_db = client['test_bd']

def add_course(collection):
    course = {
        'name': 'python',
        'start_at': datetime.now(),
        'tags': ['program']
    }

    return collection.insert_one(course).inserted_id


course_collection = netology_db['courses']
add_course(course_collection)

print(list(course_collection.find()))
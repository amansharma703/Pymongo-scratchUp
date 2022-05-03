import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
connectionStr = os.environ.get("CONN_STR")


def insertDoc(studentInfo):
    collection.insert_one(studentInfo).inserted_id


def readDoc():
    # myStudent = collection.find({"name": "Raj"})
    myStudent = collection.find({})

    for student in myStudent:
        print(student)


def updateDoc():
    collection.update_one({"name": "Raj"}, {'$inc': {'marks.math': 20}})


def deleteDoc():
    collection.delete_one({"name": "Raj"})


if __name__ == '__main__':
    client = pymongo.MongoClient(connectionStr)
    # create a database fora school
    db = client['wisdom-academy']

    # create a collection
    collection = db.class1

    # inserting into collection
    studentInfo = {
        "name": "Ajay",
        "section": 1,
        "marks": {
            "math": 50,
            "Science": 90,
            "English": 95,
            "Computer": 88,
        }
    }
    # insertDoc(studentInfo)

    # Reading collection
    readDoc()

    # updating a document
    # updateDoc()

    # deleting a document
    # deleteDoc()

    # same code will goes for insert_many(), update_many(), delete_many() with minor changes

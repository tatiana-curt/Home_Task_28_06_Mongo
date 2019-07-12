import csv
from pymongo import MongoClient


def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(row)


def add_course(collection):


if __name__ == "__main__":
    csv_path = "artists.csv"
    with open(csv_path, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)
import pymongo
from pymongo.server_api import ServerApi
from constants import uri

client = pymongo.MongoClient(uri, server_api=ServerApi('1'))

mydb = client["database"]
people = mydb["people"]


class Person:
    def __init__(self):
        name = input("whats the users name?")
        self.name = name
        age = input("whats the users age?")
        self.age = age
        height = input("whats the users height?")
        self.height = height
        gender = input("whats the users gender")
        self.gender = gender

    def adduser(self):
        user = {"name": self.name, "age": self.age, "height": self.height, "gender": self.gender}
        insert = people.insert_one(user)
        print(f"added {self.name} to the database")


class Search:
    def __init__(self):
        name = input("who are you searching for? : ")
        self.name = name

    def searchuser(self):
        query = {"name": self.name}
        searcher = people.find(query)
        for name in searcher:
            print(name)


search = Search()
search.searchuser()

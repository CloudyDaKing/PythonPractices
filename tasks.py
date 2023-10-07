import pymongo
from pymongo.server_api import ServerApi
from constants import uri


class TaskManager:
    def __init__(self, uri):
        self.client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
        self.database = self.client["database"]
        self.tasks = self.database["tasks"]

    def new_task(self, title, taskdescription):
        task = {"title": title, "description": taskdescription, "complete": False}
        self.tasks.insert_one(task)
        print("task successfully added")

    def mark_complete(self, title):
        query ={"title": title}
        update = {"$set": {"complete": True}}
        self.tasks.update_one(query, update)

    def view_tasks(self):
        for x in self.tasks.find():
            print(x)

    def remove_task(self):
        query = {"complete": True}
        self.tasks.delete_many(query)
        print("deleted all completed tasks")


if __name__ == "__main__":
    manager = TaskManager(uri)
    while True:
        print("select an option\n1.new task \n2.mark complete \n3.view all tasks\n4.remove all complete tasks\n5.exit")
        option = input(": ")
        if option == "1":
            name = input("set a task name")
            content = input("set a task description")
            manager.new_task(name, content)
            pass
        elif option == "2":
            name = input("what task do you want to set as complete?")
            manager.mark_complete(name)
        elif option == "3":
            manager.view_tasks()
        elif option == "4":
            manager.remove_task()
        elif option == "5":
            exit("thanks")

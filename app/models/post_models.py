from datetime import datetime
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['kenzie']

class Post():

    def __init__(self, title, author, tags, content) -> None:
        self.id = self.create_id()
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.title = title 
        self.author = author
        self.tags = tags 
        self.content = content


    @staticmethod
    def get_all():
        post_list = list(db.posts.find())
        return post_list


    @staticmethod
    def get_by_id(id):
        post = db.posts.find_one({"id": int(id)})
        return post


    @staticmethod
    def delete(id):
        post = db.posts.find_one({"id": int(id)})
        db.posts.delete_one(post)
        return post


    @staticmethod
    def update(data, update):
        db.posts.update_one(data, update)
        return data


    def insert_post(self):
        db.posts.insert_one(self.__dict__)
        return self.__dict__


    def create_id(self):
        post_list = list(db.posts.find())   

        try:
            id = [post['id'] for post in post_list]
            return max(id) + 1
        except:
            return 1

    @staticmethod
    def update_time(data):
        db.posts.update_one(data, {"$set": {"updated_at": datetime.utcnow()}}) 
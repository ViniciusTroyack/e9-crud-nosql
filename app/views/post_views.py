from flask import Flask
from http import HTTPStatus
from app.controllers.post_controllers import list_post, insert_new_post, find_by_id, delete_post, update_post


def post_view(app: Flask):

    @app.get("/post")
    def read_posts():
        return list_post()


    @app.get("/post/<post_id>")
    def read_post_by_id(post_id):
        return find_by_id(post_id)


    @app.delete("/post/<post_id>")
    def delete(post_id):
        return delete_post(post_id)
        

    @app.patch("/post/<post_id>")
    def update(post_id):
        return update_post(post_id)


    @app.post("/post")
    def create_post():
        return insert_new_post()
from flask import jsonify, request
from app.models.post_models import Post


def list_post():
    posts = Post.get_all()
    for post in posts:
        del post['_id']
    return jsonify(posts), 200


def find_by_id(id):
    try:
        post = Post.get_by_id(id)
        del post['_id']
        return post
    except:
        return {"message": "O post não existe"}, 404


def delete_post(id):
    try:
        post_to_be_del = Post.delete(id)
        del post_to_be_del['_id']
        return post_to_be_del, 200
    except: 
        return {"message": "O post não existe"}, 404


def update_post(id):
    try:
        update_request = request.get_json()
        update = {"$set": update_request}
        database = find_by_id(id)
        Post.update(database, update)
        Post.update_time(database)
        return find_by_id(id), 200
    except:
        return {"message": "O post não existe"}, 404


def insert_new_post():
    try:
        data = request.get_json()
        new_post = Post(**data)
        new_post.insert_post()
        return find_by_id(new_post.id)
    except:
        return {"message": "Requisição invalida"}, 400
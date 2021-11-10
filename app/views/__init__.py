from flask import Flask

def init_app(app: Flask):

    from app.views.post_views import post_view
    post_view(app)

    return app
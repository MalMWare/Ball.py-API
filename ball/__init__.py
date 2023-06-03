from flask import Flask

#factory
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, Ball Corp!"

    #register reptile blueprints
    from . import reptile
    app.register_blueprint(reptile.bp)

    return app
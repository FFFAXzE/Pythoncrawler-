from flask import Flask
from flask_script import Manager
from users.views import user
from extends import db

app = Flask(__name__)
app.config.from_pyfile("settings.py")
# 初始化db
db.init_app(app)

manager = Manager(app)
app.register_blueprint(user)


if __name__ == '__main__':
    manager.run()

from flask import Flask

# 导入blue
from src.app.user import user_blue

app = Flask(__name__)

# 注册blue
app.register_blueprint(user_blue, url_prefix='/user')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello!'


if __name__ == '__main__':
     app.run(host='127.0.0.1',port=5555)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    print("欢迎来到个人博客！")
    
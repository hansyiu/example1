# _*_ coding: utf-8 _*_
from app import app

@app.route('/')
def hello_world():
    return '这是根目录'


@app.route('/index')
def index():
    return '这是首页'
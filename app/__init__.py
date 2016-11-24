# _*_ coding: utf-8 _*_
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config.from_object('app.settings')
# app.config.from_envvar('FLASKR_SETTINGS')

# 生成数据库对象
db = SQLAlchemy(app)





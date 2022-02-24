# coding: utf-8
from extends import db
from users.base import DBBase

class Tbbeike(db.Model,DBBase):
    __tablename__ = 'beike'

    id = db.Column(db.Integer, primary_key=True, info='序号')
    position = db.Column(db.String(255), nullable=False, info='位置')
    title = db.Column(db.String(155), nullable=False, info='标题')
    houseInfo = db.Column(db.String(255),nullable=False, index=True, info='房产信息')
    totalPrice = db.Column(db.String(10), nullable=False, info='总价')
    unitPrice = db.Column(db.String(10), nullable=False,  info='每平米价格')

class TbShorts(db.Model,DBBase):
    __tablename__ = 'tb_shorts'

    userid = db.Column(db.Integer, primary_key=True, info='ID')
    users = db.Column(db.String(20),nullable=False, info='用户')
    views = db.Column(db.Integer, info='喜爱度')
    times = db.Column(db.DateTime, info='发表时间')
    votes = db.Column(db.Integer, info='被采纳')
    shorts = db.Column(db.String(20), nullable=False, info='短论')

class MoviesInfo(db.Model,DBBase):
    __tablename__ = 'movies_info'

    id = db.Column(db.Integer, primary_key=True, info='序号')
    mName = db.Column(db.String(255), nullable=False, info='名称')
    pf = db.Column(db.String(255), nullable=False, info='评分')
    detial = db.Column(db.String(255), nullable=False, info='电影信息')
    Dtime = db.Column(db.String(255), nullable=False, info='日期')
    # unitPrice = db.Column(db.String(10), nullable=False, info='每平米价格')


class TbPopulation(db.Model, DBBase):
    __tablename__ = 'tb_population'

    id = db.Column(db.Integer, primary_key=True, info='ID')
    pro=db.Column(db.String, info='省份')
    total15 = db.Column(db.Integer, info='15岁及以上合计')
    male15 = db.Column(db.Integer, info='15岁及以上男性')
    female15 = db.Column(db.Integer, info='15岁及以上女性')
    totalNotMarry = db.Column(db.Integer, info='未婚合计')
    maleNotMarry = db.Column(db.Integer, info='未婚男性')
    femaleNotMarry = db.Column(db.Integer, info='未婚女性')

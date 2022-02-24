# Description:
# @File    : base.py
# @Author  : 成少雷
# @QQ      : 313728420
# @Time    : 2021/1/19 14:29
from extends import db
class DBBase:
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()

    # 添加多条数据
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
        except:
            db.session.rollback()

    # 删除⼀条数据
    def delete(self):
        try:
            db.session.delete(self)  # 添加⼀条数据
            db.session.commit()  # 提交
        except:
             db.session.rollback()
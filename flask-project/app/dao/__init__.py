import pymysql
from app.app import app

def creatConnet():
    connect=pymysql.connect(host=app.config['HOST'],user=app.config['USER'],password=app.config['PASSWORD'],
                            port=app.config['PORT1'],db=app.config['DB'])
    return connect
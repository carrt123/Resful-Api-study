SECRET_KEY = "aswunxqkxqlxnwza;lf"

# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'restful_api'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "2368996924@qq.com"
MAIL_PASSWORD = "huxyljfxunyuebic"
MAIL_DEFAULT_SENDER = "2368996924@qq.com"
LOGIN_SECRET = '123456789apple banana'


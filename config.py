from decouple import config 
class Config:
    SECRET_KEY = '|b2Jqw)h)35LHmKX'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='libreria-db.cja2iq24edq4.us-east-1.rds.amazonaws.com'
    MYSQL_USER='admin'
    MYSQL_PASSWORD='Adminroot'
    MYSQL_DB='libreria-db'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS = True
    MAIL_USERNAME=''
    MAIL_PASSWORD=''
    
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
#FS/5o3f71KbIPv@]

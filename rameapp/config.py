class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    #ENV = "development"
    FLASK_ENV="development"
    FLASK_DEBUG = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:36571916@localhost/rame"


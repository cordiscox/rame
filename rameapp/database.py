from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import current_app, g
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:36571916@localhost/rame')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from . import models
    Base.metadata.create_all(bind=engine)


def get_db():
    if 'db' not in g:
        engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
        g.db = scoped_session(sessionmaker(bind=engine))

    return g.db()
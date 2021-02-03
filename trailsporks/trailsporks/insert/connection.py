from sqlalchemy import create_engine
import pandas as pd
# from trailsporks import credentials as cr

def create_sqlacchemy_engine(db="sqlite"):
    if db.lower() == 'postgres':
        engine_str = """postgresql://postgres:postgres@localhost:5432/trailsporks"""
        # engine_str = """postgresql://{username}:{password}@localhost:5432/{mydatabase}""".format(username=cr.username, password=cr.password,mydatabase=cr.mydatabase)
    elif db.lower() == 'sqlite':
        engine_str = 'sqlite:///../DB/trailsporks.db'
    engine = create_engine(engine_str)
    return engine

def pandas_to_postgres(df, tablename):
    engine = create_sqlacchemy_engine()
    df.to_sql(tablename, engine,if_exists='append',index=False)

def pandas_read_sql(query):
    df = pd.read_sql(query,con=create_sqlacchemy_engine())
    return df
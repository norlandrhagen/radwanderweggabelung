from sqlalchemy import create_engine
import credentials as cr

def create_sqlacchemy_engine():
    engine_str = """postgresql://{username}:{password}@localhost:5432/{mydatabase}""".format(username=cr.username, password=cr.password,mydatabase=cr.mydatabase)
    engine = create_engine(engine_str)
    return engine

def pandas_to_postgres(df, tablename, replace):
    engine = create_sqlacchemy_engine()
    df.to_sql(tablename, engine)
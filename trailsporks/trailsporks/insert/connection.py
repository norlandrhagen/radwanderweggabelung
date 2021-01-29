from sqlalchemy import create_engine
# from trailsporks import credentials as cr

def create_sqlacchemy_engine():
    engine_str = """postgresql://postgres:postgres@localhost:5432/trailsporks"""

    # engine_str = """postgresql://{username}:{password}@localhost:5432/{mydatabase}""".format(username=cr.username, password=cr.password,mydatabase=cr.mydatabase)
    engine = create_engine(engine_str)
    return engine

def pandas_to_postgres(df, tablename):
    engine = create_sqlacchemy_engine()
    df.to_sql(tablename, engine,if_exists='append',index=False)
from database.config import Config
import psycopg2

def connect(config: Config):
    conn = psycopg2.connect(database = config.database, 
                        user = config.username, 
                        host= config.host,
                        password = config.password,
                        port = config.port)
    
    # print(conn)
    return conn
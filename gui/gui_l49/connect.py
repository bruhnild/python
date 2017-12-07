#!/usr/bin/python
import psycopg2
from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    
    # read connection parameters
    params = config()
 
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)
 
    # create a cursor
    cur = conn.cursor()
 
 
 
if __name__ == '__main__':
    connect()

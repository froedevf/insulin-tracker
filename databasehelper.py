#!/usr/bin/python
import psycopg2
import os

def executeSql( sql ):
    """ Insert data into table """
    conn = None
    try:
        # connect to the PostgreSQL server
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        cur.execute( sql )
        conn.commit()
        
        cur.close()
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def query( sql ):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        cur.execute( sql )

        user_id = cur.fetchone()
        return user_id[0]
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def queryUserId(userName=''):
    return query("SELECT id from users where name='{0}'".format(userName))

if __name__ == '__main__':
    connect()
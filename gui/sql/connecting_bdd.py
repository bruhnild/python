import psycopg2
import sys
 
def connect_to_database():
	#Define our connection string
	conn_string = "host='www.metis-reseaux.fr' dbname='l49' user='postgres' password='UhtS.1Hd2' port=5678"
 
	# print the connection string we will use to connect
	print ("Connecting to database")
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print ("Connected!\n")
 
if __name__ == "__main__":
	connect_to_database()

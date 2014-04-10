
import sys
import MySQLdb
import csv

if len(sys.argv) < 2:
        print "use: %s TABLE_NAME"%(sys.argv[0])
        exit()

#connect to DB
#change the credentials to yours
db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="db")
cur = db.cursor()
cur.execute("SELECT * FROM %s"%(sys.argv[1]))


rows = cur.fetchall()
fp = open('file.csv', 'w+')
fileP = csv.writer(fp)
fileP.writerows(rows)
fp.close()

db.close()
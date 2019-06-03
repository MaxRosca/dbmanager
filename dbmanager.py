import sqlite3

class dataBase():
    dbname = ""
    tablename = ""
    categories = ()
    conn = 0
    c = 0

    def __init__(this, dbname, tablename, categories):
        this.dbname = dbname
        this.tablename = tablename
        this.categories = categories
        this.conn = sqlite3.connect(this.dbname)
        this.c = this.conn.cursor()
    
    def open(this):
        this.conn = sqlite3.connect(this.dbname)
        this.c = this.conn.cursor()
    
    def close(this):
        this.c.close()
        this.conn.close()

    def insert(this, args):
        this.open()
        try:
            var_string = ', '.join('?' * len(args))
            query_string = 'INSERT INTO {} VALUES ({});'.format(this.tablename, var_string)

            this.c.execute(query_string, args)
            this.conn.commit()
            this.close()
            return 0
        except Exception as e:
            this.close()
            if 'name' in str(e):
                return "name"
            elif 'id' in str(e):
                return 'id'
            
    def getValue(this, searchCategory, category, value):
        this.open()
        this.c.execute("SELECT {} FROM {} WHERE {}={}".format(str(searchCategory), str(this.tablename), category, value))
        name = this.c.fetchall()
        this.close()
        return name[0][0]

    def changeValue(this, category, newValue, scategory, sValue):
        this.open()
        try:
            this.c.execute("UPDATE {} SET {} = {} WHERE {} = {}".format(this.tablename, category, newValue, scategory, sValue))
            this.conn.commit()
            this.close()
            return 0
        except Exception as e:
            return e
        return 0

    def deleteColumn(this, category, value):
        this.open()
        try:
            this.c.execute("DELETE FROM {} WHERE {} = {}".format(this.tablename, category, value))
            this.conn.commit()
            this.close()
            return 0
        except Exception as e:
            this.close()
            return e

    def getAll(this):
        this.open()
        this.c.execute("SELECT * FROM {}".format(this.tablename))
        result = this.c.fetchall()
        this.close()
        return result

    def addColumn(this, name, type1):
        this.open()
        this.c.execute("ALTER TABLE {} ADD COLUMN {} {};".format(this.tablename, name, type1))
        this.close()

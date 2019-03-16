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
    
    def insert(this, args):
        try:
            var_string = ', '.join('?' * len(args))
            query_string = 'INSERT INTO {} VALUES ({});'.format(this.tablename, var_string)

            this.c.execute(query_string, args)
            this.conn.commit()
            return 0
        except Exception as e:
            if('name' in str(e)):
                return "name"
            elif('id' in str(e)):
                return 'id'
            else:
                return 'error'
            
    def getValue(this, s, value):
        this.c.execute("SELECT {} FROM {} WHERE id={}".format(str(value), str(this.tablename), s))
        name = this.c.fetchall()
        return name[0][0]

    def changeValue(this, category, newValue, scategory, sValue):
        this.c.execute("UPDATE {} SET {} = {} WHERE {} = {}".format(this.tablename, category, newValue, scategory, sValue))
        this.conn.commit()

    def deleteColumn(this, category, value):
        this.c.execute("DELETE FROM {} WHERE {} = {}".format(this.tablename, category, value))
        this.conn.commit()

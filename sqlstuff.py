import sqlite3 as lite

DBNAME = 'marius.db'

def storeAmount(name, amt):
    con = lite.connect(DBNAME)
    with con:
        cur = con.cursor()
        cmd = "SELECT * from Money where Name = ?"
        cur.execute(cmd, (name,))
        if cur.fetchone():
            # Exists, so update
            cur.execute("UPDATE Money Set Amount = ? where Name = ?",
                    (amt, name))
        else:
            # Does not exist, so insert
            cur.execute("INSERT Into Money(Name, Amount) Values (?, ?)",
                    (name, amt))

def loadAmount(name):
    con = lite.connect(DBNAME)
    with con:
        cur = con.cursor()
        cmd = "SELECT Amount from Money where Name = ?"
        cur.execute(cmd, (name,))
        d = cur.fetchall()
        if d:
            return d[0][0];
        else:
            return None


def initialize():
    con = lite.connect(DBNAME)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Money")
        cur.execute("CREATE TABLE Money("
            "Name TEXT, Amount INT, CONSTRAINT UQ_NAME UNIQUE(Name))")

def main():
    initialize()

if __name__ == '__main__':
    main()

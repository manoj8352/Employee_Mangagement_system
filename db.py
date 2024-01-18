import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            Name text,
            Date text,
            Gender text,
            Age text,
            Email text,
            Contact text,
            City text,
            Education text,
            Field text
            
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self,Name,Date, Gender, Age , Email, Contact, City,Education,Field):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?,?,?)",(Name,Date, Gender, Age , Email, Contact, City,Education,Field))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from employees where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, Name,Date, Gender, Age , Email, Contact, City,Education,Field):
        self.cur.execute(
            "update employees set Name=?, Date=?,Gender=?, Age=?, Email=?,  Contact=?, City=? ,Education=?,Field=? where id=?",
            (Name,Date, Gender, Age , Email, Contact, City,Education,Field, id))
        self.con.commit()







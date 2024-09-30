import sqlite3
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS employee(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    code TEXT,
                    email TEXT,
                    contact TEXT,
                    gender TEXT,
                    address TEXT
                    )
                """
        self.cur.execute(sql)
        self.con.commit()
        
    # Insert Function
    def insert(self, name, code, email, contact, gender, address):
        self.cur.execute(
        "INSERT INTO employee (name, code, email, contact, gender, address) VALUES (?, ?, ?, ?, ?, ?)",
        (name, code, email, contact, gender, address))
        self.con.commit()

    
    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * FROM employee")
        rows = self.cur.fetchall()
        return rows
        
    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("DELETE FROM employee WHERE id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, code, email, contact, gender, address):
        self.cur.execute(
        "UPDATE employee SET name=?, code=?, email=?, contact=?, gender=?, address=? WHERE id=?",
        (name, code, email, contact, gender, address, id))
        self.con.commit()


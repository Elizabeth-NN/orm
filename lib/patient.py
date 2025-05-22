from __init__ import CURSOR, CONN

class Patient:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<patient {self.id}: {self.name}>"

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of patient instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists patients instances"""
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name value of the current patient instance"""
        sql = """
            INSERT INTO patients (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name):
        """Initialize a new patient instance and save the object to the database"""
        patient = cls(name)
        patient.save()
        return patient

    def update(self):
        """Update the table row corresponding to the current patient instance"""
        sql = """
            UPDATE patients
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current patient instance"""
        sql = """
            DELETE FROM patients
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
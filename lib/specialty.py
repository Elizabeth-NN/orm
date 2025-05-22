from __init__ import CURSOR, CONN

class Specialty:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Specialty {self.id}: {self.name}>"

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Specialty instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS specialties (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists specialties instances"""
        sql = """
            DROP TABLE IF EXISTS specialties;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name value of the current Specialty instance"""
        sql = """
            INSERT INTO specialties (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name):
        """Initialize a new Specialty instance and save the object to the database"""
        specialty = cls(name)
        specialty.save()
        return specialty

    def update(self):
        """Update the table row corresponding to the current Specialty instance"""
        sql = """
            UPDATE specialties
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Specialty instance"""
        sql = """
            DELETE FROM specialties
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
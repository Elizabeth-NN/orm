from __init__ import CURSOR, CONN

class Doctor:
    def __init__(self, name, specialty_id, id=None):
        self.id = id
        self.name = name
        self.specialty_id = specialty_id

    def __repr__(self):
        return f"<Doctor {self.id}: {self.name}, Specialty ID: {self.specialty_id}>"

    @classmethod
    def create_table(cls):
        """Create a new table with foreign key to specialties"""
        sql = """
            CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            specialty_id INTEGER,
            FOREIGN KEY (specialty_id) REFERENCES specialties(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the doctors table"""
        sql = """
            DROP TABLE IF EXISTS doctors;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the doctor's attributes"""
        sql = """
            INSERT INTO doctors (name, specialty_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.specialty_id))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, specialty_id):
        """Initialize a new Doctor instance and save the object to the database"""
        doctor = cls(name, specialty_id)
        doctor.save()
        return doctor

    def update(self):
        """Update the table row corresponding to the current Doctor instance"""
        sql = """
            UPDATE doctors
            SET name = ?, specialty_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.specialty_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Doctor instance"""
        sql = """
            DELETE FROM doctors
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def specialty(self):
        """Return the Specialty object associated with this doctor"""
        from specialty import Specialty
        sql = """
            SELECT * FROM specialties
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.specialty_id,))
        row = CURSOR.fetchone()
        if row:
            return Specialty(row[1], row[0])  # name, id
        return None

    @classmethod
    def get_by_specialty(cls, specialty_id):
        """Return all doctors with the given specialty_id"""
        sql = """
            SELECT * FROM doctors
            WHERE specialty_id = ?
        """
        CURSOR.execute(sql, (specialty_id,))
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]  # name, specialty_id, id
from __init__ import CURSOR, CONN

class Appointment:
    def __init__(self, name, doctor_id, patient_id, id=None):
        self.id = id
        self.name = name
        self.doctor_id = doctor_id
        self.patient_id = patient_id

    def __repr__(self):
        return f"<appointment {self.id}: {self.name}, Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id}>"

    @classmethod
    def create_table(cls):
        """Create a new table with foreign key to doctors and patients"""
        sql = """
            CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            doctor_id INTEGER,
            patient_id INTEGER,
            FOREIGN KEY (doctor_id) REFERENCES doctors(id),
            FOREIGN KEY (patient_id) REFERENCES patients(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the appointments table"""
        sql = """
            DROP TABLE IF EXISTS appointments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the appointment's attributes"""
        sql = """
            INSERT INTO appointments (name, doctor_id, patient_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.doctor_id, self.patient_id))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, doctor_id, patient_id):
        """Initialize a new appointment instance and save the object to the database"""
        appointment = cls(name, doctor_id, patient_id)
        appointment.save()
        return appointment

    def update(self):
        """Update the table row corresponding to the current appointment instance"""
        sql = """
            UPDATE appointments
            SET name = ?, doctor_id = ?, patient_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.doctor_id, self.patient_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current appointment instance"""
        sql = """
            DELETE FROM appointments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
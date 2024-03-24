import sqlite3

class RegistrationDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_record(self, name, email, dob):
        try:
            self.cursor.execute("INSERT INTO Registration (Name, Email, DateOfBirth) VALUES (?, ?, ?)", (name, email, dob))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error creating record:", e)
            return False

    def read_record(self, registration_id):
        try:
            self.cursor.execute("SELECT * FROM Registration WHERE ID=?", (registration_id,))
            record = self.cursor.fetchone()
            if record:
                return record
            else:
                print("No record found with ID", registration_id)
                return None
        except sqlite3.Error as e:
            print("Error reading record:", e)
            return None

    def update_record(self, registration_id, name, email, dob):
        try:
            self.cursor.execute("UPDATE Registration SET Name=?, Email=?, DateOfBirth=? WHERE ID=?", (name, email, dob, registration_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error updating record:", e)
            return False

    def delete_record(self, registration_id):
        try:
            self.cursor.execute("DELETE FROM Registration WHERE ID=?", (registration_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error deleting record:", e)
            return False

# Connect to the SQLite database
conn = sqlite3.connect('registration.db')

# Create a RegistrationDB instance
db = RegistrationDB('registration.db')

# Example usage
# Create a record
db.create_record('Jowhar', 'jowhar@gmail.com', '1999-05-10')

# Read a record
record = db.read_record(1)
if record:
    print("Read record:", record)

# Update a record
db.update_record(1, 'Dashin', 'Dashin@gmail.com.com', '2001-02-20')


# Delete a record
db.delete_record(1)

# Close the connection
conn.close()

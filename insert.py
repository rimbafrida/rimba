import sqlite3

try:
    sqliteConnection = sqlite3.connect('database.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    
    sqlite_insert_query = """CREATE TABLE IF NOT EXISTS projects (
	id text PRIMARY KEY,
	pw text
    );"""
    count = cursor.execute(sqlite_insert_query)
    sqlite_insert_query = """INSERT INTO projects
                          (id, pw) 
                           VALUES 
                          ("reza", "123")"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

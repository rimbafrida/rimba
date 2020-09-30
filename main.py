import getpass
import sqlite3

# Get login details from user
user = input('User: ')
password = getpass.getpass('Password: ')

# Connect to database
db = sqlite3.connect('/fog/database.db')
c = db.cursor()

# Execute sql statement and grab all records where the "usuario" and
# "senha" are the same as "user" and "password"
c.execute('SELECT * FROM projects WHERE id = ? AND pw = ?', (user, password))

# If nothing was found then c.fetchall() would be an empty list, which
# evaluates to False 
if c.fetchall():
    print('Welcome')
else:
    print('Login failed')

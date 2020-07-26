import json
import sqlite3
import socket
import fileinput
import datetime
import sys
class Timer(object):
    """A simple timer class"""
    
    def __init__(self):
        pass
    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
    def stop(self):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        print str(self.stop - self.start)
    def elapsed(self):
        """Time elapsed since start was called"""
        print str(datetime.datetime.now() - self.start)[:-3]
    def now(self):
        print str(datetime.datetime.now())[:-3]
listensocket = socket.socket()
port=8081
ip = ''
listensocket.bind((ip,port))
listensocket.listen(5)
clientsocket, client_address = listensocket.accept()
watch=Timer()
watch.start()
with open ('received_file.json', 'w') as f:
  while True:
    print('receiving data...')
    data = clientsocket.recv(1024).decode()
    if not data:
      break
    else:
      print('data=%s', (data))
    f.write("["+data+"]")
listensocket.close()
file = '/home/pausjumpstyle/received_file.json'
s = open(file).read()
data = json.loads(s)
# Open the file containing the SQL database.
with sqlite3.connect("database.db") as conn:
    # Create the table if it doesn't exist.
    conn.execute(
        """CREATE TABLE IF NOT EXISTS tab(
                username varchar(100),
                password varchar(100)
            );"""
        )
        # Insert each entry from json into the table.
    keys = ["username", "password"]
    for entry in data:
        # This will make sure that each key will default to None
        # if the key doesn't exist in the json entry.
        values = [entry.get(key, None) for key in keys]
        # Execute the command and replace '?' with the each value
        # in 'values'. DO NOT build a string and replace manually.
        # the sqlite3 library will handle non safe strings by doing this.
        cmd = """INSERT INTO tab VALUES(
                    ?,
                    ?
                );"""
        conn.execute(cmd, values)
    conn.commit()
watch.elapsed()
listensocket.close()

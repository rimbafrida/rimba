import socket
import json
from cryptography.fernet import Fernet
listensocket = socket.socket()
port=8089
ip =''
listensocket.bind(('',port))
listensocket.listen(5)
print ("menunggu koneksi")
clientsocket, client_address = listensocket.accept()
#watch=Timer()
#watch.start()
running = True
while running:
        file = '/home/pausjumpstyle/received_file.json'
        s = open(file).read()
        data = str(json.loads(s))
        print (data)
        file = open('key.key', 'rb')
        key = file.read() # The key will be type bytes
        file.close()
        f2=Fernet(key)
        decrypted = f2.encrypt(data)
        clientsocket.send(decrypted.encode())
        break
listensocket.close()

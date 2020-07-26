import socket
import random 
import operator
import os
import time
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
        print str(datetime.datetime.now() - self.start)[:-1]
    def now(self):
        print str(datetime.datetime.now())[:-1]

ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul}
num1 = random.randint(0,12)
num2 = random.randint(0,12)  
op = random.choice(list(ops.keys()))
answer = ops.get(op)(num1,num2)
soal = ('berapa hasil operasi perhitungan  {} {} {}?\n'.format(num1, op, num2))
#main
print (answer)
listensocket = socket.socket()
port=8085
ip =''
listensocket.bind(('',port))
listensocket.listen(5)
print ("menunggu koneksi")
clientsocket, client_address = listensocket.accept()
watch=Timer()
watch.start()
while True:
        print('receiving data...')
        clientsocket.send(str(soal.encode())) #pemberian challenge
        print("Pengguna Terhubung ")
        watch.elapsed()
        print(soal)
        time.sleep(1)
        jawaban = clientsocket.recv(1024).decode()
        watch.elapsed()
        print("jawaban Diterima ")
               answerstr = str(jawaban)
        answerString = str(answer)
        if answerString == answerstr: #penyamaan jawaban yang diberikan
                respon = ("jawaban anda benar")
                print("Mulai tersambung Dengan Client ")
                watch.elapsed()
                os.system("python test.py")
                break
        else:
                print ('Client salah dalam menjawab chaaallenge')
                break
listensocket.close()
exit()

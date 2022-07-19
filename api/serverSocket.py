# coding: utf-8

from http import client
import socket
import threading
import select
from tkinter.tix import Tree

bind_ip = '192.168.15.100'
bind_port = 5000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print('[*] escutando %s %d'%(bind_ip,bind_port))

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print('[*] Recebido: %s'%request)
    print('\n------------------------------\n')
    client_socket.send('\nMensagen destinada ao cliente: %s\n' %addr[0] )
    client_socket.send('\n ACK! \nRecbido pelo servidor!\n')
    client_socket.close()

while True:
    client,addr = server.accept()
    print('[*] Conexão aceita de: %s %d' %(addr[0],addr[1]))
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
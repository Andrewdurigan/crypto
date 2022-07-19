# coding: utf-8
import socket
from sqlite3 import connect
import threading
import select

def conecta( cliente , endereco ):
    print('Clinte {} Recebido!'.format(endereco))
    servidor = socket.socket()
    servidor.connect( ( 'nl.serverip.co',8080 ) )
    
    try:
        while True:
            leitura, escreita, erro = select.select([servidor,cliente],[],[servidor,cliente], 3)
            if erro:  raise 
            for i in leitura:
                dados = i.recv( 8192 )
                if not dados: raise
                if i is servidor: 
                    #download
                    cliente.send( dados )
            else:
            #Upload
                servidor.send( dados )
    except:
        print('Cliente desconectado!')
            

#Listen => 
IP='127.0.0.1'
PORT= 8088
listen = socket.socket()
listen.bind( ( IP,PORT ) )
listen.listen(0)
print('Esperando o cliente no IP e Porta: 127.0.0.1:8088')
while True:
  cliente , endereco = listen.accept()
  threading.Thread( target= conecta, args=(cliente,endereco)).start()
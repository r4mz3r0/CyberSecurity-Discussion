#Like ncat, we need to open a port. 
import socket
import threading 

#bind_ip is the local internet protocol 
binding_ip = "192.168.1.105"
binding_port = 666
#Choosing ports under 1024 not recommened, "priviliged ports" 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((binding_ip,binding_port))
#How many connections to allow? Here we allow only 2
server.listen(2)

print("[*] Listening %s:%d"%(binding_ip,binding_port))
  #handshaking
#Our client 
def handle_client(client_socket):
    request = client_socket.recv(1024)

    print "[*] Message Recieved: %s" % request 
    #send back a packet
    client_socket.send("Welcome!")
    client_socket.close()
 #who is the client
while True:
    client,addr = server.accept()
    print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

# Echo client program
import socket
HOST = “192.168.1.31” # The remote host(ROBOT)
PORT = 30002 # Te same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
txt = “set_digital_out(0,True)” + “\n”
msg = txt.encode(“utf8”)
s.send (msg)
data = s.recv(1024)
s.close()
print (“Received”, repr(data))

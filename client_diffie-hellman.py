import socket

ip_server = 'XXX.XX.XX.X'
porta_server = 4500
g = 40
n = 991

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect((ip_server,porta_server))

while(True):
    a = int(input("inserisci il numero scelto a"))
    A = (g**a) % n
    #invio dei dati al server
    client.sendall(A.encode())
    #leggo il risultato, B
    B = int(client.recv(4096))
    sol = (B**a)%n
    print("Soluzione: " + sol)

client.close()
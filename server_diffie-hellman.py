import socket as sock

s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

ip = "xxx.xx.xx.x"
port = 4500
g = input("Inserire il numero 1(g): \n")
n = input("Inserire il numero 2(n): \n")

a = input("Inserire il numero 3(a): \n")

A = g**a %n


address = (ip, port)

def server():
    s.bind(address)
    s.listen()
    conn, add = s.accept()


def main():
    server()
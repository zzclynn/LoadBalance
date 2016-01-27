if __name__ == '__main__':  
    import socket
    import time  
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 5555))
        time.sleep(2)
        sock.send('Hello, this is the sender')
        print sock.recv(1024)
        sock.close() 
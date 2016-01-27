if __name__ == '__main__':  
    import socket  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.bind(('localhost', 8888))  
    sock.listen(5)  
    while True:  
        connection,address = sock.accept()  
        try:  
            buf = connection.recv(1024)  
            print buf
            connection.send('welcome to server1!')  
        except socket.timeout:  
            print 'time out'  
        connection.close() 
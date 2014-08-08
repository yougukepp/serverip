#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

gAuthPort = 8001
gBufSize = 1024

def main():
    host = ''
    port = gAuthPort 
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port)) 
    
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)

    while True:
        data = conn.recv(gBufSize)
        if not data:
            break
        conn.sendall(all)
        conn.close()

if __name__ == '__main__':
    main()


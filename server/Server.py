#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

import socket


class Server:
    def __init__(self, address, server_port, server_data_size):
        self._data_size = server_data_size
        self._create_socket()
        self._bind_socket_to_port(address, server_port)

    def _create_socket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _bind_socket_to_port(self, address, server_port):
        server_address = (address, server_port)
        self._socket.bind(server_address)

    def handle_connection(self):
        self._socket.listen(1)
        while True:
            connection, client_address = self._socket.accept()
            data = connection.recv(self._data_size)
            if data:
                print(data)
                connection.send(data)
            connection.close()


if __name__ == "__main__":
    host = "localhost"
    port = 50001
    data_size = 1024
    server = Server(host, port, data_size)
    server.handle_connection()

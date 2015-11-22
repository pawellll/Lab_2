#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

import socket
from Board import Board


class Client:
    def __init__(self, address, server_port, server_data_size):
        self._data_size = server_data_size
        self._create_socket()
        self._connect_to_server(address, server_port)

    def _create_socket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _connect_to_server(self, address, server_port):
        server_address = (address, server_port)
        self._socket.connect(server_address)

    def send_msg(self, msg):
        self._socket.send(bytes(msg, 'UTF-8'))
        response = self._socket.recv(self._data_size)
        self._socket.close()
        print("received {0}".format(response))

if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 1024
    client = Client(host, port, data_size)
    client.send_msg("lalaggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
    board = Board()
    board.print_board()
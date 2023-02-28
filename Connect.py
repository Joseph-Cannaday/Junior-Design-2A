#!/usr/bin/env python3
# Authors: Joseph Cannaday
# Junior Design 2023 Group 2A

import sys
import socket
import selectors
import traceback
import multiprocessing
import time

from Protocol import libserver
from Protocol import libclient

from Utils.robotUtils import create_request, listen_for_director, start_connection, initiate_connection

def register(host="127.0.0.1", port=65432, listen_port=65433, robot_name="Snapdragonfly"):
    print('Register with director...')

    registration_request = create_request(robot_name, "Register", listen_port) 
    initiate_connection(host, port, registration_request, libclient)
    print('Finished registration, booting up server to listen...')

def listen(host="127.0.0.1", port=65432, listen_port=65433, robot_name="Snapdragonfly"):
    msg = listen_for_director(host, listen_port, libserver)

    print(msg)
    if msg['value'] == 'break':
      break

    print('Main Loop recieved ', msg, ' so will start to do task')

def decodeMessage(msg):
    return
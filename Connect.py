#!/usr/bin/env python3
# Authors: Joseph Cannaday, Arman Allahverdi
# Junior Design 2023 Group 2A

import socket
import json
import time

# Global Constants
DIRECTOR_HOST = "107.23.238.206"
DIRECTOR_PORT = 3336
CONNECTION_RETRY = 5          # Number of Tries before failure
CONNECTION_RETRY_DELAY = 5000 # Milliseconds
ROBOT_ID = 'Snapdragonfly'

class Connect:
  def __init__(self):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP + IPv4
    self.self.status = 'CONNECTING'  # System self.status (CONNECTING, CONNECTED, RUNNING, FAILED)

  # Perform initial connection and identification procedure
  def connect(self, host, port):
    self.s.connect((host, port))

    # Perform identification procedure
    message = encode_json({ "cmd": "IDENTIFY", "data": ROBOT_ID })
    self.s.send(message)
    
    # Verify identification was successful
    callback = json.loads(self.s.recv(1024).decode())
    if (callback['cmd'] == 'IDENTIFY' and callback['data'] == True):
      print("[CLIENT] Connection successful")
      self.status = 'CONNECTED'
    
    # Identification was unsuccessful
    print("[CLIENT] Connection failed:", callback['data'])
    self.status = 'FAILED'

  # Central message decoder. Decodes the JSON message and performs actions
  # based on the message.
  def decode_message(self, message):
    payload = json.loads(message)
    
    if payload['cmd'] == 'LINE':
    # Line given by the server once presentation starts and it is your turn
      return payload['data']

    # Server signal that the presentation is complete
    elif payload['cmd'] == 'PRESENTATION_COMPLETE':
      print("[CLIENT] Presentation is complete")
      return ''
      
    # All lines for a given robot. Given by the server during initial connection
    # when running in echo mode
    elif payload['cmd'] =='LINES':
      print("[CLIENT] Got lines:", payload['data'])
      return ''

    # When the server is running in echo mode, all messages sent to it
    # will be returned to origin
    elif payload['cmd'] == 'ECHO':
      print('[CLIENT] Got echo from server:', payload['data'])
      return ''

    # If the command does not match any of the commands above, move on
    else:
      print('[CLIENT] Got undefined response from server:', payload['cmd'])
      return ''

  def encode_json(self, obj):
    return json.dumps(obj, separators=(',', ':')).encode()

if __name__ == '__main__':
    c1 = Connect()
    c1.connect(DIRECTOR_HOST, DIRECTOR_PORT)
    
    if (c1.status != 'CONNECTED'): return print("Failed connection, exiting")
    try:
      while True:
        c1.decode_message(c1.s.recv(1024).decode())
    except socket.error:
      print("[CLIENT] Failed...", )
      c1.s.close()
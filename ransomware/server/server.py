# import modules
import socket
import json
import os



# importing helpers
from utils.helpers import attack_request,resolve_attack


# define constants
SERVER_IP = "192.168.3.144"
SERVER_PORT = 5678


# create and maintain socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # bind and host server
    s.bind((SERVER_IP,SERVER_PORT));
    s.listen(1);
    

    # Message : Awaiting Connection
    print(f"Awaiting Connection at {SERVER_IP}:{SERVER_PORT}");

    # accept connection & Message : Connected
    connection,address = s.accept();
    print(f"Connect Established with {connection.getpeername()}");

    request_type = connection.recv(1024);
    if(request_type.decode('utf-8') == '0'):
        attack_request(connection);
    else:
        resolve_attack(connection);


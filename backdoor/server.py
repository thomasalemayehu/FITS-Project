# import modules
import socket

# define constants
SERVER_IP = "192.168.3.144"
SERVER_PORT = 5676;

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
    
    # continously accept commands
    while True:

        # input command
        command = input("Enter your command here : ");
        
        # exit command
        if(command == "exit -t"):
            break;

        # send command
        connection.send(command.encode('utf-8'));

        # recieve output and show user
        output = connection.recv(1024).decode('utf-8');
        print(output);

    # close connection after exit
    connection.close()
    
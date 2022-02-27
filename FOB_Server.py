import socket
import os
import shutil
import sys
HOST = 'localhost'
PORT = 1024

directory = "FOB"

parent_dir = "home/User/Documents"

path = os.path.join(parent_dir, directory)


os.mkdir(path)
print("Directory '%s' created" %directory)
 
clone = "git clone git@github.com:whatever /home/$USER/Documents/peas"

os.system(clone) # Cloning

shutil.make_archive(output_filename, 'zip', dir_name)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)
while (1):
    conn, addr = socket.accept()
    reqFile = conn.recv(1024)
    with open(reqFile, 'rb') as file_to_send:
        for data in file_to_send:
            conn.sendall(data)
    conn.close()

socket.close()

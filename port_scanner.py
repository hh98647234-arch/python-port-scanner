import socket
target = "127.0.0.1"
print("scaning localhost. . .")
for port in range(1, 101):
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket. settimeout(0.5)

    result = sock.connect_ex((target, port))

   if result == 0:
      print(f"port {port} is OPEN")
   sock.close()

print("scan complete)

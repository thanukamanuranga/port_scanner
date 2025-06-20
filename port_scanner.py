import socket
import time

target = input("Enter the IP address to scan: ")
start_time = time.time()

print(f"\nScanning target {target}...\n")

for port in range(1, 101):  # Scans ports 1 to 100
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)  # Timeout for each port
    result = sock.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        print(f"Port {port} is OPEN ({service})")
    sock.close()

end_time = time.time()
print(f"\nScan completed in {round(end_time - start_time, 2)} seconds.")

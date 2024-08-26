import socket

def port_scanner(target_ip, start_port, end_port):
    print(f"Scanning target: {target_ip} from port {start_port} to {end_port}")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    port_scanner(target_ip, start_port, end_port)

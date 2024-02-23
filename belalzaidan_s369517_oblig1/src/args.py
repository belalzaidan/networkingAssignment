import sys
import argparse
import socket

def validate_ip(ip):
    '''
        This function takes in an IP and returns a boolean
        wheather the IP is valid or not

    '''
    parts = ip.split('.')
    
    if len(parts) != 4: return False
    
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True 

def validate_port(port):
    '''
        This function takes in an integer, and returns a boolean
        wheather it's valid as a port number or not
    '''
    if port.isdigit():
        try:
            port_num = int(port)
            if 1024 <= port_num <= 65553:
                return True
            else:
                return False
        except:
            return False
    else: return False 

def data_exchange(args, mode):
    '''
        This is the function where we handle data exchange based on mode 
        (server or client). The function takes in two arguments.
        mode: either client mode or server mode are required to 
        run the program as.
        args: array of arguments brought from the terminal where the
        program is intended to be run. it holds the ip and port if they are
        specified by the user, otherwise a default value for the ip and the port
        are set to be set.

    '''
    # Setting default values for host and port if not provided
    if args.host:
        if validate_ip(args.host):
            host = args.host 
        else: 
            print("Your ip address must be in this format: x.x.x.x")
            sys.exit()
    else: host = '127.0.0.1'
    
    if args.port:
        if  validate_port(args.port):
            port = args.port
        else: 
            print("Your port must be within the range [1024,65553]")
            sys.exit()
    else: port = 22000

    # Server mode
    if mode == 'server':
        message = args.message
        # Creating a socket object for server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Binding socket to host and port
            s.bind((host, port))
            print(f"Server is connected to ip: {host} and port: {port}")
            # Listening for incoming connections
            s.listen(1)
            # Accepting incoming connections
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                # Receiving data from client
                data = conn.recv(1024).decode()
                print(f"Client says: {data}")
                if not data:
                    sys.exit("No data received")
                # Sending back the received data
                conn.sendall(data.encode())
    
    # Client mode
    elif mode == 'client':
        message = str(args.message)
        # Creating a socket object for client
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connecting to server
        c.connect((host, port))
        # Sending data to server
        c.sendall(message.encode())
        # Receiving response from server
        data = c.recv(1024).decode()
        print('Received: ', data)

# Setting up argument parser
host = argparse.ArgumentParser(description='TCP data exchange')
host.add_argument('-i', '--host', help='Host IP')
host.add_argument('-p', '--port', type=int, help='Port')
host.add_argument('-s', '--server', '-server',  action='store_true', help='Run in server mode')
host.add_argument('-c', '--client', '-client',  action='store_true', help='Run in client mode')
host.add_argument('-m', '--message', help='Message to send in client mode')
args = host.parse_args()

mode = ''
# Determining mode based on arguments provided
if args.server:
    mode = 'server'
if args.client:
    mode = 'client'

# Handling conflicting modes
if args.client and args.server:
    print("You cannot use both client and server modes at the same time.")
    sys.exit()
elif not args.client and not args.server:
    print("You should specify either client or server mode.")
    sys.exit()

# Calling the data_exchange function with arguments and mode
data_exchange(args, mode)
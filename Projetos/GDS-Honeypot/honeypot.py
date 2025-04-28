# Gabriel Domingues Silva
# gabriel.domingues.silva@usp.br
# github.com/gds-domingues
# This is a simple SSH Honeypot that listens for incoming connections and prints the username and password for demonstration purposes.

# Importing Libraries
import socket
import paramiko
import threading

# Custom SSH server class that extends paramiko.ServerInterface
class SSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username: str, password: str) -> int:
        # Print the username and password for demonstration purposes
        print(f"{username} : {password}")
        # Always return AUTH_FAILED for simplicity, you may implement proper authentication logic here
        return paramiko.AUTH_FAILED

# Function to handle incoming connections
def handle_connection(client_sock):
    # Create a new Transport object for the connection
    transport = paramiko.Transport(client_sock)
    
    # Load the server's private key for authentication
    server_key = paramiko.RSAKey.from_private_key_file('key')
    
    # Add the server's key to the transport
    transport.add_server_key(server_key)
    
    # Create an instance of the custom SSHServer class
    ssh = SSHServer()
    
    # Start the SSH server on the transport
    transport.start_server(server=ssh)

# Main function to run the SSH server
def main():
    # Create a TCP socket for the server
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set socket option to allow reusing the address
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the specified address and port
    server_sock.bind(('', 2222))
    
    # Listen for incoming connections with a backlog of 223
    server_sock.listen(223)

    # Main server loop
    while True:
        # Accept an incoming connection
        client_sock, addr = server_sock.accept()
        
        # Print a message indicating a successful connection
        print(f"Connected to {addr}")
        
        # Create a new thread to handle the connection
        client_thread = threading.Thread(target=handle_connection, args=(client_sock,))
        client_thread.start()

# Entry point of the script
if __name__ == '__main__':
    main()

"""
This code sets up a simple SSH server using the Paramiko library. 
It listens on port 2222 for incoming connections and, for each connection, 
spawns a new thread to handle the SSH communication. 
The authentication logic is minimal, printing the provided username and password 
for demonstration purposes and always returning paramiko.AUTH_FAILED.
"""
# Code Explanation

This code sets up a simple SSH server using the Paramiko library. It listens on port 2222 for incoming connections and, for each connection, spawns a new thread to handle the SSH communication. The authentication logic is minimal, printing the provided username and password for demonstration purposes and always returning paramiko.AUTH_FAILED.

1. Import necessary modules:

```python
import socket
import paramiko
import threading
```

- **`socket`**: Provides low-level networking support and is used for creating sockets.
- **`paramiko`**: Implements the SSH protocol and is used for SSH server and client functionality.
- **`threading`**: Enables the creation and management of threads for concurrent execution.

1. Define a custom SSH server class:

```python
class SSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username: str, password: str) -> int:
        print(f"{username} : {password}")
        return paramiko.AUTH_FAILED
```

- **`SSHServer`** is a subclass of **`paramiko.ServerInterface`**, providing a custom implementation of the server-side SSH protocol.
- The **`check_auth_password`** method is called during the authentication process, and in this example, it prints the provided username and password and returns **`paramiko.AUTH_FAILED`** (authentication failure).

1. Create a function to handle incoming connections:

```python
def handle_connection(client_sock):
    transport = paramiko.Transport(client_sock)
    server_key = paramiko.RSAKey.from_private_key_file('key')
    transport.add_server_key(server_key)
    ssh = SSHServer()
    transport.start_server(server=ssh)
```

- **`handle_connection`** is responsible for setting up the SSH connection when a client connects.
- It creates a **`paramiko.Transport`** object using the provided socket (**`client_sock`**).
- Loads the server's private key from the file 'key'.
- Adds the server's key to the transport.
- Instantiates the custom **`SSHServer`** class.
- Starts the SSH server on the transport.

1. Define the main function:

```python
def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('', 2222))
    server_sock.listen(223)

    while True:
        client_sock, addr = server_sock.accept()
        print(f"Connected to {addr}")
        client_thread = threading.Thread(target=handle_connection, args=(client_sock,))
        client_thread.start()
```

- **`main`** is the main entry point of the script.
- Creates a TCP socket (**`server_sock`**) using IPv4 and TCP.
- Sets a socket option to allow reusing the address to avoid issues when restarting the script.
- Binds the socket to the specified address ('' for all available interfaces) and port 2222.
- Listens for incoming connections with a backlog of 223.
- Enters into a continuous loop to accept incoming connections.
- When a connection is accepted, it prints a message indicating the connection and starts a new thread (**`client_thread`**) to handle the connection using the **`handle_connection`** function.

1. Execute the script when it's run as the main program:

```python
if __name__ == '__main__':
    main()
```

- This block ensures that the **`main`** function is only executed if the script is run directly (not imported as a module).

import socket

def main():
    try:
        # Get server details from the user
        server_ip = input("Enter the server's IP address: ")
        server_port = int(input("Enter the server's port number: "))

        # Create a client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((server_ip, server_port))
        print(f"Connected to {server_ip}:{server_port}")

        # Receive and display the quote from the server
        quote_bytes = client_socket.recv(1024)
        quote = quote_bytes.decode('utf-8')
        print(f"Received quote: {quote}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    main()

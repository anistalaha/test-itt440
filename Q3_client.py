import socket

def main():
    try:
        # Get server details from user
        ip = input("Enter server IP: ")
        port = int(input("Enter server port: "))

        # Create client socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client.connect((ip, port))
        print(f"Connected to {ip}:{port}")

        # Get user input for the radius
        r = float(input("Enter radius of the sphere: "))

        # Send radius to the server
        client.sendall(str(r).encode('utf-8'))

        # Receive and display sphere volume from the server
        volume_bytes = client.recv(1024)
        volume = float(volume_bytes.decode('utf-8'))
        print(f"Sphere volume with radius {r} is: {volume:.2f}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        client.close()

if __name__ == "__main__":
    main()

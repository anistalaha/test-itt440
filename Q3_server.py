import socket
import math

def calc_vol(r):
    return (4/3) * math.pi * r**3

def handle_client(client):
    try:
        # Receive the radius value from the client
        r_bytes = client.recv(1024)
        radius = float(r_bytes.decode('utf-8'))

        # Calculate the sphere volume
        volume = calc_vol(radius)

        # Send the calculated sphere volume to the client
        client.sendall(str(volume).encode('utf-8'))

    except Exception as e:
        print(f"Error handling client: {e}")

    finally:
        # Close the connection
        client.close()

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('192.168.84.81', 8080))
    server_sock.listen(5)

    print("Server waiting for connections...")

    while True:
        try:
            # Accept a connection
            client_sock, addr = server_sock.accept()
            print(f"Connected to {addr}")

            # Handle the client in a separate function
            handle_client(client_sock)

        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == "__main__":
    main()

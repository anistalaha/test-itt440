import socket

class StudentIDClient:
    def __init__(self):
        self.server_address = "izani.synology.me"
        self.server_port = 8443

    def connect_and_send_id(self):
        student_id = input("Enter UiTM Student ID: ")

        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Connect to the server
            client_socket.connect((self.server_address, self.server_port))
            print(f"Connected to {self.server_address}:{self.server_port}")

            # Send the UiTM Student ID to the server
            client_socket.sendall(student_id.encode('utf-8'))

            # Receive and print the server response
            response = client_socket.recv(1024)
            print("Server response:", response.decode('utf-8'))

        except Exception as e:
            print(f"Error during connection: {e}")

        finally:
            # Close the socket when done
            client_socket.close()

if __name__ == "__main__":
    student_client = StudentIDClient()
    student_client.connect_and_send_id()

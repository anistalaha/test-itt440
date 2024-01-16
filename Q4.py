import socket
import threading
import random

# Array of quotes, including Quranic verses
quotes = [
    "“Do not lose hope, nor be sad.” — Quran 3:139",
    "“For indeed, with hardship, there is ease.” — Quran 94:5",
    "“Allah is with those who have patience.” — Quran 2:1",
    "“Indeed, the patient will be given their reward without account.” – Quran 39:10"
]

# Function to handle a client request
def handle_client(client_socket):
    try:
        # Send a random quote to the client
        random_quote = random.choice(quotes)
        client_socket.sendall(random_quote.encode('utf-8'))

    except Exception as e:
        print(f"Error handling client: {e}")

    finally:
        # Close the connection
        client_socket.close()

# Main function for the server
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.84.81', 8484))
    server_socket.listen(5)

    print("QOTD server listening on port 8484...")

    while True:
        try:
            # Accept a connection
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")

            # Handle the client in a separate thread
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == "__main__":
    main()

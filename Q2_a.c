#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    // Server IP address and port
    const char *s_ip = "192.168.147.142";
    const int s_port = 8080;

    // Create server socket
    int server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        perror("Failed to create server socket");
        exit(EXIT_FAILURE);
    } else {
        printf("Server socket created successfully.\n");
    }

    // Bind socket to address
    struct sockaddr_in server_address = {
        .sin_family = AF_INET,
        .sin_addr.s_addr = inet_addr(s_ip),
        .sin_port = htons(s_port)
    };

    if (bind(server_socket, (struct sockaddr*)&server_address, sizeof(server_address)) == -1) {
        perror("Failed to bind server socket to address");
        close(server_socket);
        exit(EXIT_FAILURE);
    } else {
        printf("Server socket bound to address successfully.\n");
    }

    // Listen for incoming connections
    if (listen(server_socket, 5) == -1) {
        perror("Failed to start listening for connections");
        close(server_socket);
        exit(EXIT_FAILURE);
    } else {
        printf("Server is now listening for connections on %s:%d...\n", s_ip, s_port);
    }

    while (1) {
        // Accept a connection
        int client_socket = accept(server_socket, NULL, NULL);
        if (client_socket == -1) {
            perror("Failed to accept connection");
            continue;
        }

        // Connection successful message
        printf("Connection established. Sending random number...\n");

        // Generate a random number
        int random_number = rand() % 100;

        // Send the random number to the client
        send(client_socket, &random_number, sizeof(random_number), 0);

        // Close the connection
        close(client_socket);
    }

    // Close the server socket
    close(server_socket);

    return 0;
}

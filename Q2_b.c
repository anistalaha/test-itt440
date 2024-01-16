#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    // Client socket setup
    int client_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (client_sock == -1) {
        perror("Failed to create client socket");
        exit(EXIT_FAILURE);
    }

    struct sockaddr_in server_addr = {
        .sin_family = AF_INET,
        .sin_addr.s_addr = inet_addr("192.168.147.142"),  // Server IP address
        .sin_port = htons(8080)  // Server port
    };

    // Connect to the server
    if (connect(client_sock, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("Failed to connect to the server");
        close(client_sock);
        exit(EXIT_FAILURE);
    }

    // Receive random number from the server
    int received_num;
    if (recv(client_sock, &received_num, sizeof(received_num), 0) == -1) {
        perror("Failed to receive data from the server");
        close(client_sock);
        exit(EXIT_FAILURE);
    }

    // Display the received random number
    printf("Received random number from server: %d\n", received_num);

    // Close the client socket
    close(client_sock);

    return 0;
}

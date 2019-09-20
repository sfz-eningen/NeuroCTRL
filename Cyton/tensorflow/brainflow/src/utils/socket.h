#pragma once

#ifdef _WIN32
#include <ws2tcpip.h>
// should be included before windows.h
#include <windows.h>
#else
#include <arpa/inet.h>
#include <sys/socket.h>
#include <unistd.h>
#endif

#include <stdlib.h>
#include <string.h>


enum class SocketType
{
    UDP = 0,
    TCP = 1
};

enum class SocketReturnCodes
{
    STATUS_OK = 0,
    WSA_STARTUP_ERROR = 1,
    CREATE_SOCKET_ERROR = 2,
    CONNECT_ERROR = 3,
    PTON_ERROR = 4
};

class Socket
{

public:
    Socket (const char *port_name, int port, int socket_type);
    ~Socket ()
    {
        close ();
    }

    int connect ();
    int send (const char *data, int size);
    int recv (void *data, int size);
    void close ();
    char *get_ip_addr ()
    {
        return ip_addr;
    }
    int get_port ()
    {
        return port;
    }

private:
    char ip_addr[32];
    int port;
    int socket_type;
#ifdef _WIN32
    SOCKET connect_socket;
    struct sockaddr_in socket_addr;
#else
    int connect_socket;
    struct sockaddr_in socket_addr;
#endif
};

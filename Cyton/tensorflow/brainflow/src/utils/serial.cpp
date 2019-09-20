#include "serial.h"
#ifndef _WIN32
#include <fcntl.h>
#include <unistd.h>
#endif

/////////////////////////////////////////////////
/////////////////// Windows /////////////////////
/////////////////////////////////////////////////

#ifdef _WIN32
Serial::Serial (const char *port_name)
{
    strcpy (this->port_name, port_name);
    port_descriptor = NULL;
}

bool Serial::is_port_open ()
{
    return (this->port_descriptor != NULL);
}

int Serial::open_serial_port ()
{
    this->port_descriptor =
        CreateFile (this->port_name, GENERIC_READ | GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, NULL);
    if (this->port_descriptor == INVALID_HANDLE_VALUE)
        return SerialExitCodes::OPEN_PORT_ERROR;
    return SerialExitCodes::OK;
}

int Serial::set_serial_port_settings ()
{
    DCB dcb_serial_params = {0};
    COMMTIMEOUTS timeouts = {0};
    dcb_serial_params.DCBlength = sizeof (dcb_serial_params);
    if (GetCommState (this->port_descriptor, &dcb_serial_params) == 0)
    {
        CloseHandle (this->port_descriptor);
        return SerialExitCodes::GET_PORT_STATE_ERROR;
    }

    dcb_serial_params.BaudRate = CBR_115200;
    dcb_serial_params.ByteSize = 8;
    dcb_serial_params.StopBits = ONESTOPBIT;
    dcb_serial_params.Parity = NOPARITY;
    if (SetCommState (this->port_descriptor, &dcb_serial_params) == 0)
    {
        CloseHandle (this->port_descriptor);
        return SerialExitCodes::SET_PORT_STATE_ERROR;
    }

    timeouts.ReadIntervalTimeout = 1000;
    timeouts.ReadTotalTimeoutConstant = 1000;
    timeouts.ReadTotalTimeoutMultiplier = 100;
    timeouts.WriteTotalTimeoutConstant = 50;
    timeouts.WriteTotalTimeoutMultiplier = 10;
    if (SetCommTimeouts (this->port_descriptor, &timeouts) == 0)
    {
        CloseHandle (this->port_descriptor);
        return SerialExitCodes::SET_TIMEOUT_ERROR;
    }
    return OK;
}

int Serial::read_from_serial_port (void *bytes_to_read, int size)
{
    DWORD readed;
    if (!ReadFile (this->port_descriptor, bytes_to_read, size, &readed, NULL))
        return 0;
    return (int)readed;
}

int Serial::send_to_serial_port (const void *message, int length)
{
    DWORD bytes_written;
    if (!WriteFile (this->port_descriptor, message, length, &bytes_written, NULL))
        return 0;
    return bytes_written;
}

int Serial::close_serial_port ()
{
    if (this->is_port_open ())
    {
        CloseHandle (this->port_descriptor);
    }
    return SerialExitCodes::OK;
}

/////////////////////////////////////////////////
//////////////////// Linux //////////////////////
/////////////////////////////////////////////////

#else

Serial::Serial (const char *port_name)
{
    strcpy (this->port_name, port_name);
    port_descriptor = 0;
}

bool Serial::is_port_open ()
{
    return (this->port_descriptor > 0);
}

int Serial::open_serial_port ()
{
    int flags = O_RDWR | O_NOCTTY;
    this->port_descriptor = open (this->port_name, flags);
    if (this->port_descriptor < 0)
        return SerialExitCodes::OPEN_PORT_ERROR;
    return OK;
}

int Serial::set_serial_port_settings ()
{
    struct termios port_settings;
    memset (&port_settings, 0, sizeof (port_settings));

    tcgetattr (this->port_descriptor, &port_settings);
    cfsetispeed (&port_settings, B115200);
    cfsetospeed (&port_settings, B115200);
    port_settings.c_cflag &= ~PARENB;
    port_settings.c_cflag &= ~CSTOPB;
    port_settings.c_cflag &= ~CSIZE;
    port_settings.c_cflag |= CS8;
    port_settings.c_cflag |= CREAD;
    port_settings.c_cflag |= CLOCAL;
    port_settings.c_cflag |= HUPCL;
    port_settings.c_iflag = IGNPAR;
    port_settings.c_iflag &= ~(ICANON | IXOFF | IXON | IXANY);
    port_settings.c_oflag = 0;
    port_settings.c_lflag = 0;
    // blocking read with timeout 1 sec
    port_settings.c_cc[VMIN] = 0;
    port_settings.c_cc[VTIME] = 10;

    if (tcsetattr (this->port_descriptor, TCSANOW, &port_settings) != 0)
        return SerialExitCodes::SET_PORT_STATE_ERROR;
    tcflush (this->port_descriptor, TCIOFLUSH);
    return SerialExitCodes::OK;
}

int Serial::read_from_serial_port (void *bytes_to_read, int size)
{
    return read (this->port_descriptor, bytes_to_read, size);
}

int Serial::send_to_serial_port (const void *message, int length)
{
    int res = write (this->port_descriptor, message, length);
    return res;
}

int Serial::close_serial_port ()
{
    if (this->is_port_open ())
    {
        int res = close (port_descriptor);
        if (res < 0)
            return SerialExitCodes::CLOSE_ERROR;
    }
    return SerialExitCodes::OK;
}

#endif

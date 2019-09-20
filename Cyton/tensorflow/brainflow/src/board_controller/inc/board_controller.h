#pragma once

#ifdef _WIN32
#define SHARED_EXPORT __declspec(dllexport)
#else
#define SHARED_EXPORT
#endif

typedef enum
{
    STATUS_OK = 0,
    PORT_ALREADY_OPEN_ERROR,
    UNABLE_TO_OPEN_PORT_ERROR,
    SET_PORT_ERROR,
    BOARD_WRITE_ERROR,
    INCOMMING_MSG_ERROR,
    INITIAL_MSG_ERROR,
    BOARD_NOT_READY_ERROR,
    STREAM_ALREADY_RUN_ERROR,
    INVALID_BUFFER_SIZE_ERROR,
    STREAM_THREAD_ERROR,
    STREAM_THREAD_IS_NOT_RUNNING,
    EMPTY_BUFFER_ERROR,
    INVALID_ARGUMENTS_ERROR,
    UNSUPPORTED_BOARD_ERROR,
    BOARD_NOT_CREATED_ERROR,
    ANOTHER_BOARD_IS_CREATED_ERROR,
    GENERAL_ERROR,
    SYNC_TIMEOUT_ERROR
} CustomExitCodes;

typedef enum
{
    SYNTHETIC_BOARD = -1,
    CYTON_BOARD = 0,
    GANGLION_BOARD = 1,
    CYTON_DAISY_BOARD = 2,
    NOVAXR_BOARD = 3
} BoardIds;

#ifdef __cplusplus
extern "C"
{
#endif
    SHARED_EXPORT int prepare_session (int board_id, char *port_name);
    SHARED_EXPORT int start_stream (int buffer_size, int board_id, char *port_name);
    SHARED_EXPORT int stop_stream (int board_id, char *port_name);
    SHARED_EXPORT int release_session (int board_id, char *port_name);
    SHARED_EXPORT int get_current_board_data (int num_samples, float *data_buf, double *ts_buf,
        int *returned_samples, int board_id, char *port_name);
    SHARED_EXPORT int get_board_data_count (int *result, int board_id, char *port_name);
    SHARED_EXPORT int get_board_data (
        int data_count, float *data_buf, double *ts_buf, int board_id, char *port_name);
    SHARED_EXPORT int set_log_level (int log_level);
    SHARED_EXPORT int config_board (char *config, int board_id, char *port_name);
#ifdef __cplusplus
}
#endif
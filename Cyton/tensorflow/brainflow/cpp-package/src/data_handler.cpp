#include <math.h>
#include <stdlib.h>

#include "board_controller.h"
#include "data_handler.h"

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

DataHandler::DataHandler (int board_id)
{
    this->board_id = board_id;
    start_eeg = BoardInfoGetter::get_first_eeg_channel (board_id);
    stop_eeg = BoardInfoGetter::get_num_eeg_channels (board_id) + start_eeg;
    sample_rate = BoardInfoGetter::get_fs_hz (board_id);
}

void DataHandler::filter_lowpass (double **data, int data_count, float cutoff)
{
    double rc = 1.0 / (cutoff * 2 * M_PI);
    double dt = 1.0 / sample_rate;
    double alpha = dt / (rc + dt);
    double *temp_arr = new double[data_count];

    for (int channel = start_eeg; channel < stop_eeg; channel++)
    {
        temp_arr[0] = data[0][channel];
        for (int i = 1; i < data_count; i++)
            temp_arr[i] = temp_arr[i - 1] + alpha * (data[i][channel] - temp_arr[i - 1]);
        for (int i = 0; i < data_count; i++)
            data[i][channel] = temp_arr[i];
    }
    delete[] temp_arr;
}

void DataHandler::filter_highpass (double **data, int data_count, float cutoff)
{
    double rc = 1.0 / (cutoff * 2 * M_PI);
    double dt = 1.0 / sample_rate;
    double alpha = rc / (rc + dt);
    double *temp_arr = new double[data_count];

    for (int channel = start_eeg; channel < stop_eeg; channel++)
    {
        temp_arr[0] = data[0][channel];
        for (int i = 1; i < data_count; i++)
            temp_arr[i] = alpha * (temp_arr[i - 1] + data[i][channel] - data[i - 1][channel]);
        for (int i = 0; i < data_count; i++)
            data[i][channel] = temp_arr[i];
    }
    delete[] temp_arr;
}

void DataHandler::filter_bandpass (
    double **data, int data_count, float min_cutoff, float max_cutoff)
{
    filter_lowpass (data, data_count, max_cutoff);
    filter_highpass (data, data_count, min_cutoff);
}

void DataHandler::remove_dc_offset (double **data, int data_count, float value)
{
    filter_highpass (data, data_count, value);
}

void DataHandler::preprocess_data (
    double **data, int data_count, float min_cutoff, float max_cutoff, float dc_offset)
{
    remove_dc_offset (data, data_count, dc_offset);
    filter_bandpass (data, data_count, min_cutoff, max_cutoff);
}

#pragma once

#include "spinlock.h"
#include <stdlib.h>
#include <string.h>

class DataBuffer
{

    SpinLock lock;

    double *timestamps;
    float *data;

    size_t buffer_size;
    size_t first_used, first_free;
    size_t count;
    size_t num_samples;

    size_t next (size_t index)
    {
        return (index + 1) % buffer_size;
    }

    void get_chunk (size_t start, size_t size, double *tsBuf, float *data_buf);

public:
    DataBuffer (int num_samples, size_t buffer_size);
    ~DataBuffer ();

    void add_data (double timestamp, float *value);
    size_t get_data (size_t max_count, double *ts_buf, float *data_buf);
    size_t get_current_data (size_t max_count, double *ts_buf, float *data_buf);
    size_t get_data_count ();
    bool is_ready ();
};

#include "data_buffer.h"

DataBuffer::DataBuffer (int num_samples, size_t buffer_size)
{
    this->buffer_size = buffer_size;
    this->num_samples = num_samples;
    data = new float[buffer_size * num_samples];
    timestamps = new double[buffer_size];
    first_free = first_used = count = 0;
}

DataBuffer::~DataBuffer ()
{
    delete[] data;
    delete[] timestamps;
}

bool DataBuffer::is_ready ()
{
    return (data != NULL);
}

void DataBuffer::add_data (double timestamp, float *value)
{
    lock.lock ();
    this->timestamps[first_free] = timestamp;
    memcpy (this->data + first_free * num_samples, value, sizeof (float) * num_samples);
    first_free = next (first_free);
    count++;
    if (first_free == first_used)
    {
        first_used = next (first_used);
        count--;
    }
    lock.unlock ();
}

void DataBuffer::get_chunk (size_t start, size_t size, double *ts_buf, float *data_buf)
{
    if (start + size < buffer_size)
    {
        memcpy (ts_buf, timestamps + start, size * sizeof (double));
        memcpy (data_buf, data + start * num_samples, size * sizeof (float) * num_samples);
    }
    else
    {
        size_t first_half = buffer_size - start;
        size_t second_half = size - first_half;
        memcpy (ts_buf, timestamps + start, first_half * sizeof (double));
        memcpy (data_buf, data + start * num_samples, first_half * sizeof (float) * num_samples);
        memcpy (ts_buf + first_half, timestamps, second_half * sizeof (double));
        memcpy (
            data_buf + first_half * num_samples, data, second_half * sizeof (float) * num_samples);
    }
}

// removes data from buffer
size_t DataBuffer::get_data (size_t max_count, double *ts_buf, float *data_buf)
{
    lock.lock ();
    size_t result_count = max_count;
    if (result_count > count)
        result_count = count;
    if (result_count)
    {
        get_chunk (first_used, result_count, ts_buf, data_buf);
        first_used = (first_used + result_count) % buffer_size;
        count -= result_count;
    }
    lock.unlock ();
    return result_count;
}

// doesn't remove data from buffer
size_t DataBuffer::get_current_data (size_t max_count, double *ts_buf, float *data_buf)
{
    lock.lock ();
    size_t result_count = max_count;
    if (result_count > count)
        result_count = count;
    if (result_count)
    {
        size_t first_return = (first_used + (count - result_count)) % buffer_size;
        get_chunk (first_return, result_count, ts_buf, data_buf);
    }
    lock.unlock ();
    return result_count;
}

size_t DataBuffer::get_data_count ()
{
    lock.lock ();
    size_t result = this->count;
    lock.unlock ();
    return result;
}

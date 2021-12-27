#include "timing.h"

uint64_t time_in_microsec(){
    struct timeval t;
    gettimeofday(&t, NULL);
    return ((uint64_t)t.tv_sec * 1000000 + (uint64_t)t.tv_usec);
}
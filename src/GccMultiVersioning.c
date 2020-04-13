#include "Common.h"

MULTIDISPATCH_EXPORT __attribute__((target_clones("default,sse4.1,avx")))
int32_t sum(int32_t* data, size_t n) {
    int32_t r = 0;
    for(size_t ir = n; ir != 0; ir--) {
        size_t i = n - ir;
        r += data[i];
    }
    return r;
}
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include "params.h"
#include "ntt.h"
#include "randombytes.h"
#include "cpucycles.h"
#include "speed_print.h"
#include "reduce.h"

#define NTESTS 1000000
uint64_t t[NTESTS];

int main()
{
    int16_t a1[256];
    int16_t b1[256];
    int16_t result1[256];

    int16_t a2[256];
    int16_t b2[256];
    int16_t result2[256];
    for (int i = 0; i < 256; i++)
    {
        b1[i] = i;
        a1[i] = i;
        b2[i] = i;
        a2[i] = i;
    }
    ntt(a1);

    for (int i = 0; i < NTESTS; i++)
    {
        t[i] = cpucycles();
        ntt_error_detection(a1);
    }
    print_results("NTT: ", t, NTESTS);
}
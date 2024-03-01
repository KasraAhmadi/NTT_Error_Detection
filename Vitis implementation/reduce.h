#ifndef REDUCE_H
#define REDUCE_H
#include <stdint.h>

#define QINV 62209 // q^-1 mod 2^16
#define KYBER_Q 3329
int16_t montgomery_reduce(int32_t a);

#endif

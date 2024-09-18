# NTT_Error_Detection
This repository provides the simulation and Vitis code of Error detection capable Number-Theoretic Transform published in "Efficient Algorithm Level Error Detection for Number-Theoretic Transform used for Kyber Assessed on FPGAs and ARM"

The simulation part for Negative Wrapped Convolution is based on the work https://github.com/acmert/ntt-based-polmul.
The simulation and implementation for Kyber Round 3 is based on the reference implementation https://github.com/pq-crystals/kyber.

For getting the overhead of error detection scheme over x86-64 architectures run to compile:

'''gcc -Wall -Wextra -Wpedantic -Wmissing-prototypes -Wredundant-decls   -Wshadow -Wpointer-arith -mavx2 -mbmi2 -mpopcnt -maes   -march=native -mtune=native -O3 -fomit-frame-pointer main.c reduce.c ntt.c cpucycles.c speed_print.c'''

For getting the overhead of error detection scheme over x86-64 architectures run to compile:

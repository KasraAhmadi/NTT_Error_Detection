# NTT_Error_Detection
This repository provides the simulation and Vitis code of Error detection capable Number-Theoretic Transform published in "Efficient Algorithm Level Error Detection for Number-Theoretic Transform used for Kyber Assessed on FPGAs and ARM"

The simulation part for Negative Wrapped Convolution is based on the work https://github.com/acmert/ntt-based-polmul.
The simulation and implementation for Kyber Round 3 is based on the reference implementation https://github.com/pq-crystals/kyber.

#Compile
For getting the overhead of error detection scheme over x86-64 architectures run to compile:
```
gcc -Wall -Wextra -Wpedantic -Wmissing-prototypes -Wredundant-decls   -Wshadow -Wpointer-arith -mavx2 -mbmi2 -mpopcnt -maes   -march=native -mtune=native -O3 -fomit-frame-pointer main.c reduce.c ntt.c cpucycles.c speed_print.c
```
#citation
Please cite our papar if you find our repo helpful.
```
@article{ahmadi2024efficient,
  title={Efficient Algorithm Level Error Detection for Number-Theoretic Transform used for Kyber Assessed on FPGAs and ARM},
  author={Ahmadi, Kasra and Aghapour, Saeed and Kermani, Mehran Mozaffari and Azarderakhsh, Reza},
  journal={arXiv preprint arXiv:2403.01215},
  year={2024}
}
```

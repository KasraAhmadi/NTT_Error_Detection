#include "reduce.h"


//int16_t inverse(int16_t x, int16_t y, int16_t p)
//{
//
//    // Initialize answer
//	int16_t res = 1;
//
//    // Check till the number becomes zero
//    for (int8_t i=0;i<12;i++){
//
//        // If y is odd, multiply x with result
//        if (y % 2 == 1)
//            res = (res * x);
//
//        // y = y/2
//        y = y >> 1;
//
//        // Change x to x^2
//        x = (x * x);
//    }
//    return res % p;
//}

int16_t montgomery_reduce(int32_t a)
{
  int32_t t;
  int16_t u;

  u = a*QINV;
  t = (int32_t)u*KYBER_Q;
  t = a - t;
  t >>= 16;
  return t;
}

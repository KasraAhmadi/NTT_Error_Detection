#include "ntt.h"
#include "reduce.h"

static int16_t fqmul(int16_t a, int16_t b) {
  return montgomery_reduce((int32_t)a*b);
}

void stage(int16_t r[256],int stage,int16_t out[256])
{
#pragma HLS ALLOCATION instances=mul limit=2 operation

  unsigned int start, j, k;
  int step = 256 >> stage;
  int16_t t, zeta;
  int16_t index = 0;
  int16_t h = 1 << (stage-1);
  k = 1 << (stage-1);

  outer_loop:for (start = 0; start <  h; start++){
      zeta = zetas[k++];
//      index = step * start * 2;
      	  inner_loop:for (j = 0; j < step;j++){
			#pragma HLS PIPELINE
      		int16_t op_one = index+j;
      		int16_t op_two = op_one + step;
          // printf("op_one=%d,op_two=%d,k=%d\n",op_one,op_two,k-1);
          t = fqmul(zeta, r[op_two]);
          out[op_two] = r[op_one] - t;
          out[op_one] = r[op_one] + t;
      }
      index = index + (step << 1);
      // printf("w change\n");
  }
}

void ntt(int16_t input_data[256],int16_t output_data[256]) {
 #pragma HLS INTERFACE mode=ap_fifo port=input_data
 #pragma HLS INTERFACE mode=ap_fifo port=output_data
 #pragma HLS DATAFLOW
	int16_t local_data_0[256];
	int16_t local_data_1[256];
	int16_t local_data_2[256];
	int16_t local_data_3[256];
	int16_t local_data_4[256];
	int16_t local_data_5[256];
	int16_t local_data_6[256];
	int16_t local_data_7[256];


	copy_loop_in:for (int i = 0;i< 256; i++){
		  local_data_0[i] = input_data[i];
	  }
    stage(local_data_0,1,local_data_1);
    stage(local_data_1,2,local_data_2);
    stage(local_data_2,3,local_data_3);
    stage(local_data_3,4,local_data_4);
    stage(local_data_4,5,local_data_5);
    stage(local_data_5,6,local_data_6);
    stage(local_data_6,7,local_data_7);

    copy_loop_out:for (int i = 0;i< 256; i++){
    	   output_data[i] = local_data_7[i];
      }


//
// int16_t local_data[256];
//  unsigned int len, start, j, k;
//  int16_t* out;
//  int16_t t, zeta;
//
//  k = 1;
//
//  copy_loop_in:for (int i = 0;i< 256; i++){
//	  local_data[i] = input_data[i];
//  }
//
//  upper_loop:for(len = 128; len >= 2; len >>= 1) {
//	#pragma HLS loop_tripcount min=7 max=7
//    middle_loop:for(start = 0; start < 256; start = j + len) {
//	#pragma HLS loop_tripcount min=1 max=64
//      zeta = zetas[k++];
//      inner_loop:for(j = start; j < start + len; ++j) {
//		#pragma HLS loop_tripcount min=2 max=128
//        t = fqmul(zeta, local_data[j + len]);
//        local_data[j + len] = local_data[j] - t;
//        local_data[j] = local_data[j] + t;
//      }
//    }
//
//  }
//   copy_loop_out:for (int i = 0;i< 256; i++){
//	   output_data[i] = local_data[i];
//  }
}





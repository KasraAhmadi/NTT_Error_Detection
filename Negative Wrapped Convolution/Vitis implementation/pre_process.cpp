#include "pre_process.h"
void pre_process(int16_t input_1[256],int16_t out[256]){
#pragma HLS INTERFACE mode=ap_fifo port=input_1
#pragma HLS INTERFACE mode=ap_fifo port=out
	pre_process_loop:for (int i = 0;i< 256; i++){
			#pragma HLS PIPELINE
			out[i] = montgomery_reduce((int32_t)input_1[i]*psi[i]);
	}
}







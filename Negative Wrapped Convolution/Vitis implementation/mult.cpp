#include "mult.h"
#include "pre_process.h"

static void pre_process_error_detection(int16_t input_1[256],int16_t input_2[256],int16_t out_1_pre[256],int16_t out_2_pre[256]){

	#pragma HLS DATAFLOW
	pre_process(input_1,out_1_pre);
	pre_process(input_2,out_2_pre);
}

void mult(int16_t input_1[256],int16_t input_2[256],int16_t out[256]){
#pragma HLS INTERFACE mode=ap_fifo port=input_1
#pragma HLS INTERFACE mode=ap_fifo port=input_2
#pragma HLS INTERFACE mode=ap_fifo port=out


//#pragma HLS DATAFLOW
#pragma HLS allocation function instances=ntt limit=1

	int16_t out_1_pre[256];
	int16_t out_2_pre[256];
	int16_t out_1_ntt[256];
	int16_t out_2_ntt[256];
	pre_process_error_detection(input_1,input_2,out_1_pre,out_2_pre);
	ntt(out_1_pre,out_1_ntt);
	ntt(out_2_pre,out_2_ntt);
	mult_loop:for (int i = 0;i< 256; i++){
		#pragma HLS PIPELINE
		out[i] = montgomery_reduce((int32_t)out_1_ntt[i]*out_2_ntt[i]);
		}
}







from math import log
from random import randint
from generate_prime import *
from helper import *



def Radix2_DIT_Iterative_NTT_NR(A,W,q,mode):
    N = len(A)
    B = [_ for _ in A]
    alpha = 0
    for s in range(int(log(N,2)),0,-1):
        m = 2**s
        for k in range(int(N/m)):
            TW = pow(W,intReverse(k,int(log(N,2))-s)*int(m/2),q)
            for j in range(int(m/2)):
                u = B[k*m+j]
                t = (TW*B[k*m+j+int(m/2)]) % q
                B[k*m+j]          = (u+t) % q
                B[k*m+j+int(m/2)] = (u-t) % q
                alpha = alpha + 1
    sum = 0
    return B

def Radix2_DIT_Iterative_NTT_NR_encoded(A,W,q,mode,a,b):
    N = len(A)
    B = [_ for _ in A]
    for s in range(int(log(N,2)),0,-1):
        m = 2**s
        for k in range(int(N/m)):
            TW = pow(W,intReverse(k,int(log(N,2))-s)*int(m/2),q)
            for j in range(int(m/2)):
                u = B[k*m+j]
                t = (TW*B[k*m+j+int(m/2)]) % q
                B[k*m+j]          = (u+t) % q
                B[k*m+j+int(m/2)] = (u-t) % q
    for i in range(N):
        alpha = intReverse(i,int(log(N,2)))
        B[i] = (modinv((a+pow(w,N-alpha)),q)*B[i])%q
    return B

def Single_error_inection_location(N):
    faulty_butter_fly = random.randint(0,N)
    faulty_op = random.randint(0,4)
    err = [faulty_butter_fly,faulty_op]
    return err

def Multi_error_inection_location(N,number):
    faulty_butter_fly = []
    faulty_op = []
    for _ in range(number):
        faulty_butter_fly.append(random.randint(0,N))
        faulty_op.append(random.randint(0,4))
    err = [faulty_butter_fly,faulty_op]
    return err

def Radix2_DIT_Iterative_NTT_NR_Error(A,W,q,max_err):
    N = len(A)
    B = [_ for _ in A]
    fault_meta = Multi_error_inection_location(N,max_err)
    faulty_butter_fly_arr = fault_meta[0]
    faulty_op_arr = fault_meta[1]
    buttef_fly_counter = 0
    for s in range(int(log(N,2)),0,-1):
        m = 2**s
        for k in range(int(N/m)):
            TW = pow(W,intReverse(k,int(log(N,2))-s)*int(m/2),q)
            for j in range(int(m/2)):
                if(buttef_fly_counter in faulty_butter_fly_arr):
                    index = faulty_butter_fly_arr.index(buttef_fly_counter)
                    faulty_op = faulty_op_arr[index]
                    if(faulty_op == 0):
                        u = random.randint(0,q)
                    else:
                        u = B[k*m+j]
                    if(faulty_op == 1):
                        t = random.randint(0,q)
                    else:
                        t = (TW*B[k*m+j+int(m/2)]) % q
                    if(faulty_op == 2):
                        B[k*m+j] = random.randint(0,q)
                    else:
                        B[k*m+j]          = (u+t) % q
                    if(faulty_op == 3):
                        B[k*m+j+int(m/2)] = random.randint(0,q)
                    else:
                        B[k*m+j+int(m/2)] = (u-t) % q
                else:
                    u = B[k*m+j]
                    t = (TW*B[k*m+j+int(m/2)]) % q
                    B[k*m+j]          = (u+t) % q
                    B[k*m+j+int(m/2)] = (u-t) % q
                buttef_fly_counter = buttef_fly_counter + 1
    return B
    

def Radix2_DIT_Iterative_NTT_NR_Encode_Error(A,W,q,mode,a,b):
    N = len(A)
    B = [_ for _ in A]
    fault_meta = Single_error_inection_location(N)
    faulty_butter_fly = fault_meta[0]
    faulty_op = fault_meta[1]
    if(mode == "0"):
        faulty_butter_fly = -1
    buttef_fly_counter = 0
    for s in range(int(log(N,2)),0,-1):
        m = 2**s
        for k in range(int(N/m)):
            TW = pow(W,intReverse(k,int(log(N,2))-s)*int(m/2),q)
            for j in range(int(m/2)):
                if(faulty_butter_fly == buttef_fly_counter):
                    if(faulty_op == 0):
                        u = random.randint(0,q)
                    else:
                        u = B[k*m+j]
                    if(faulty_op == 1):
                        t = random.randint(0,q)
                    else:
                        t = (TW*B[k*m+j+int(m/2)]) % q
                    if(faulty_op == 2):
                        B[k*m+j] = random.randint(0,q)
                    else:
                        B[k*m+j]          = (u+t) % q
                    if(faulty_op == 3):
                        B[k*m+j+int(m/2)] = random.randint(0,q)
                    else:
                        B[k*m+j+int(m/2)] = (u-t) % q
                else:
                    u = B[k*m+j]
                    t = (TW*B[k*m+j+int(m/2)]) % q
                    B[k*m+j]          = (u+t) % q
                    B[k*m+j+int(m/2)] = (u-t) % q
                buttef_fly_counter = buttef_fly_counter + 1

    for i in range(N):
        alpha = intReverse(i,int(log(N,2)))
        B[i] = (modinv((a+b*pow(w,N-alpha)),q)*B[i])%q

    return B


def simple_mult(A1,A2,W,q,mode):
    N = len(A1)
    B1 = Radix2_DIT_Iterative_NTT_NR(A1,W,q,mode)
    B2 = Radix2_DIT_Iterative_NTT_NR(A2,W,q,mode)
    result = []
    for i in range(N):
        result.append((B1[i]*B2[i])%q)
    
def multi(A,B,W,q,a,b):
    N = len(A)
    A_shifted = A[1:] + A[0:1]
    B_shifted = B[1:] + B[0:1]
    encoded_A = []
    encoded_B = []
    for i in range(len(A)):
        encoded_A.append((2*A[i]+A_shifted[i])%q)
        encoded_B.append((2*B[i]+B_shifted[i])%q)
    #Single error injection
    B1 = Radix2_DIT_Iterative_NTT_NR_Error(encoded_A,W,q,1)
    B2 = Radix2_DIT_Iterative_NTT_NR_Error(encoded_B,W,q,0)
    result = []
    for i in range(N):
        alpha = intReverse(i,int(log(N,2)))
        result.append((modinv((a+b*pow(W,N-alpha)),q)**2*B1[i]*B2[i])%q)
    sum_A = 0
    sum_B = 0
    for item in A:
        sum_A = item + sum_A
    for item in B:
        sum_B = item + sum_B
    one_side = (sum_A*sum_B)%q
    second_side = result[0]
    
    if(one_side != second_side):
        return True
    else:
        return False

mod     = 2 # if 1 --> q = 1 (mod n), if 2 --> q = 1 (mod 2n)
n       = 256
size    = [8,8]
q       = 3329
w       = 17

print("Parameters")
print("n      : {}".format(n))
print("q      : {}".format(q))
print("w      : {}".format(w))



def run(n):
    detected_errors = 0
    testcases = 1000000
    for _ in range(testcases):
        A =[randint(0,q-1) for x in range(n)]
        B =[randint(0,q-1) for x in range(n)]
        res = multi(A,B,w,q,2,1)
        if(res == True):
            detected_errors = detected_errors + 1
    print("Precision is: {precision}%, Number of samples: {testcases}, N = {N}"
        .format(testcases=testcases,
                N = n,
                detected_error=detected_errors,
                precision=(detected_errors/testcases)*100))

run(n)


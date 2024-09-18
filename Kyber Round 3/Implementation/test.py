from math import log,floor,ceil
from implementation.simulation.helper import *

def Radix2_DIT_Iterative_NTT_NR(A,W,q):
    N = len(A)
    B = [_ for _ in A]

    for s in range(int(log(N,2)),0,-1):
        m = 2**s
        print("---------------------------------------------------")
        for k in range(int(N/m)):
            TW = pow(W,intReverse(k,int(log(N,2))-s)*int(m/2),q)
            print(intReverse(k,int(log(N,2))-s)*int(m/2))
            for j in range(int(m/2)):
                u = B[k*m+j]
                t = (TW*B[k*m+j+int(m/2)]) % q

                B[k*m+j]          = (u+t) % q
                B[k*m+j+int(m/2)] = (u-t) % q
                print("j = {}, j+len = {}, zeta = {}, k = {}".format(k*m+j,k*m+j+int(m/2),TW,intReverse(k,int(log(N,2))-s)*int(m/2)))

    return B

# A = [1]*256
# Radix2_DIT_Iterative_NTT_NR(A,17,3329)
n = 128
print(((2*intReverse(3,7)+1)*127)%256)

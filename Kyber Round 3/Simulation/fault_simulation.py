from helper import *
import random
tree = [
  0, 64, 32, 96, 16, 80, 48, 112, 8, 72, 40, 104, 24, 88, 56, 120,
  4, 68, 36, 100, 20, 84, 52, 116, 12, 76, 44, 108, 28, 92, 60, 124,
  2, 66, 34, 98, 18, 82, 50, 114, 10, 74, 42, 106, 26, 90, 58, 122,
  6, 70, 38, 102, 22, 86, 54, 118, 14, 78, 46, 110, 30, 94, 62, 126,
  1, 65, 33, 97, 17, 81, 49, 113, 9, 73, 41, 105, 25, 89, 57, 121,
  5, 69, 37, 101, 21, 85, 53, 117, 13, 77, 45, 109, 29, 93, 61, 125,
  3, 67, 35, 99, 19, 83, 51, 115, 11, 75, 43, 107, 27, 91, 59, 123,
  7, 71, 39, 103, 23, 87, 55, 119, 15, 79, 47, 111, 31, 95, 63, 127
]
zetas = [  2285, 2571, 2970, 1812, 1493, 1422, 287, 202, 3158, 622, 1577, 182, 962,
  2127, 1855, 1468, 573, 2004, 264, 383, 2500, 1458, 1727, 3199, 2648, 1017,
  732, 608, 1787, 411, 3124, 1758, 1223, 652, 2777, 1015, 2036, 1491, 3047,
  1785, 516, 3321, 3009, 2663, 1711, 2167, 126, 1469, 2476, 3239, 3058, 830,
  107, 1908, 3082, 2378, 2931, 961, 1821, 2604, 448, 2264, 677, 2054, 2226,
  430, 555, 843, 2078, 871, 1550, 105, 422, 587, 177, 3094, 3038, 2869, 1574,
  1653, 3083, 778, 1159, 3182, 2552, 1483, 2727, 1119, 1739, 644, 2457, 349,
  418, 329, 3173, 3254, 817, 1097, 603, 610, 1322, 2044, 1864, 384, 2114, 3193,
  1218, 1994, 2455, 220, 2142, 1670, 2144, 1799, 2051, 794, 1819, 2475, 2459,
  478, 3221, 3021, 996, 991, 958, 1869, 1522, 1628]


zetas_inv = [
  1701, 1807, 1460, 2371, 2338, 2333, 308, 108, 2851, 870, 854, 1510, 2535,
  1278, 1530, 1185, 1659, 1187, 3109, 874, 1335, 2111, 136, 1215, 2945, 1465,
  1285, 2007, 2719, 2726, 2232, 2512, 75, 156, 3000, 2911, 2980, 872, 2685,
  1590, 2210, 602, 1846, 777, 147, 2170, 2551, 246, 1676, 1755, 460, 291, 235,
  3152, 2742, 2907, 3224, 1779, 2458, 1251, 2486, 2774, 2899, 1103, 1275, 2652,
  1065, 2881, 725, 1508, 2368, 398, 951, 247, 1421, 3222, 2499, 271, 90, 853,
  1860, 3203, 1162, 1618, 666, 320, 8, 2813, 1544, 282, 1838, 1293, 2314, 552,
  2677, 2106, 1571, 205, 2918, 1542, 2721, 2597, 2312, 681, 130, 1602, 1871,
  829, 2946, 3065, 1325, 2756, 1861, 1474, 1202, 2367, 3147, 1752, 2707, 171,
  3127, 3042, 1907, 1836, 1517, 359, 758, 1441
]
q = 3329
w = 17
def intReverse(a,n):
    b = ('{:0'+str(n)+'b}').format(a)
    return int(b[::-1],2)

def matrix_mul(r):
    B = [0]*256
    for i in range(128):
        # print("\n######################")
        # print(i)
        for j in range(128):
            index = ((2 * intReverse(i,7)) + 1) * j
            index = index % 256
            tmp = (r[2*j] * (w**index)%q) % q
            tmp_2 = (r[2*j+1] * (w**index)%q) % q
            B[2*i] = (B[2*i] + tmp) % q
            B[2*i+1] = (B[2*i+1] + tmp_2) % q
    return B


def matrix_mul_encoded(r):
    f_0 = r[0]
    f_1 = r[1]
    r = r[2:] + r[0:2] #shift r
    # print(r)
    result = matrix_mul(r)
    for i in range(128):
        pow_number = intReverse(i,7)
        param = pow(w,2*pow_number+1)
        # helper = modinv(param,q)
        result[2*i] = ((result[2*i] * param) + (2 * f_0)) % q
        result[(2*i)+1] = ((result[2*i+1] * param) + (2 * f_1)) % q
    return result

def summation(input):
    sum = 0
    for i in range(256):
        sum += input[i] 
    sum = (sum%q)
    return sum


def ntt(r):
  k = 1
  len = 128
  while (len >=2):
    # print("----------------------------------------------------------------")
    start = 0
    while(start < 256):
        zeta =  (w ** tree[k]) % q
        # zeta = zetas[k]
        k = k + 1
        # print("Zeta incement")
        j = start
        while(j<start+len):
            # print("j = {}, j+len = {}, zeta= {}, k= {}".format(j,j+len,zeta,tree[k-1]))
            t = (zeta * r[j + len]) % q
            r[j + len] = (r[j] - t) % q
            r[j] = (r[j] + t)% q
            j = j + 1
        start = j + len
    len = len // 2
    
def error_detection(r_0,r_1,r):
    left_side = ((r_0*128) + (r_1*128)) % q
    right_side = summation(r) % q
    if(left_side != right_side):
        return True #Detect True
    else:
        return False
    
def burst_injection(max_faults,N):
    error = random.randint(0,N)
    errors = {}
    for i in range(max_faults):
        errors[error+i] = random.randint(0,3)
    return errors

def Single_error_inection_location(max_faults,N):
    errors = {}
    for i in range(max_faults):
        errors[random.randint(0,N)] = random.randint(0,3)
    return errors

def encode_input(a,alpha,betha):
    a_shifted = a[2:] + a[0:2]
    encoded_a = []
    for i in range(len(a)):
        encoded_a.append((alpha*a[i]+betha*a_shifted[i]))
    return encoded_a

def ntt_error_naive(r,error_number):
  zero_index = r[0]
  one_index = r[1]
  buterfly_counter = 0
  fault_meta = Single_error_inection_location(1,896)
  faulty_butter_fly = fault_meta[0]
  faulty_op = fault_meta[1]
  k = 1
  len = 128
  while (len >=2):
    start = 0
    while(start < 256):
        zeta =  (w ** tree[k]) % q
        k = k + 1
        j = start
        while(j<start+len):
            if( buterfly_counter in faulty_butter_fly):
                if(faulty_op[buterfly_counter] == 0):
                    t = random.randint(0,q)
                else:
                    t = (zeta * r[j + len]) % q
                if(faulty_op[buterfly_counter] == 1):
                    r[j + len] = random.randint(0,q)
                else:
                    r[j + len] = (r[j] - t) % q
                if(faulty_op[buterfly_counter] == 2):
                    r[j] = random.randint(0,q)
                else:
                    r[j] = (r[j] + t)% q
            else:
                t = (zeta * r[j + len]) % q
                r[j + len] = (r[j] - t) % q
                r[j] = (r[j] + t)% q
            buterfly_counter += 1
            j = j + 1
        start = j + len
    len = len // 2
  return error_detection(zero_index,one_index,r)

def ntt_error_novel(r_input,alpha,betha,error_number):
  zero_index = r_input[0]
  one_index = r_input[1]
  r = encode_input(r_input,alpha,betha)
  buterfly_counter = 0
  fault_meta = burst_injection(error_number,896)
#   fault_meta = Single_error_inection_location(error_number,896)
  faulty_butter_fly = list(fault_meta.keys())
  k = 1
  len = 128
  while (len >=2):
    start = 0
    while(start < 256):
        zeta =  (w ** tree[k]) % q
        k = k + 1
        j = start
        while(j<start+len):
            if(buterfly_counter in faulty_butter_fly):
                if(fault_meta[buterfly_counter] == 0):
                    t = random.randint(0,q)
                else:
                    t = (zeta * r[j + len]) % q
                if(fault_meta[buterfly_counter] == 1):
                    r[j + len] = random.randint(0,q)
                else:
                    r[j + len] = (r[j] - t) % q
                if(fault_meta[buterfly_counter] == 2):
                    r[j] = random.randint(0,q)
                else:
                    r[j] = (r[j] + t)% q
            else:
                t = (zeta * r[j + len]) % q
                r[j + len] = (r[j] - t) % q
                r[j] = (r[j] + t)% q
            buterfly_counter += 1
            j = j + 1
        start = j + len
    len = len // 2
  for i in range(128):
    index = ((2 * intReverse(i,7)) + 1)
    help = modinv(pow(w,index),q)
    r[2*i] = (r[2*i]+(2*betha*zero_index)*help)*modinv((betha*help)+alpha,q) %q
    r[2*i+1] = (r[2*i+1]+(2*betha*one_index)*help)*modinv((betha*help)+alpha,q) %q     

    
  return error_detection(zero_index,one_index,r)

undetected_errors = 0
samples = 10000
for i in range(samples):
    a = [0] * 256
    for i in range(256):
        a[i] = random.randint(0,q)
    # res = ntt_error_naive(a,1)
    res = ntt_error_novel(a,2,1,5)
    if(res == False):
        undetected_errors += 1
print("error detection rate = {}, samples = {}".format(((samples-undetected_errors)*100/samples),samples))



# a = [1] * 256
# ntt(a)
# print(a)
# print(((128*128)%3329))
# print(128)
# print(matrix_mul_encoded(b))
# matrix_mul(a)cl
# ntt_error_detection(b,2,1)

# print((17**(128*4))%q)

# print((17**3)%3329)
# print((17**(129*3))%3329)
# sum = 0
# for i in range(128):
#     x = 2*intReverse(i,7)+1
#     sum += x
#     print("Index: {}, int_reverse: {}".format(i,x))
# print(sum%256)
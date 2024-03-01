import random
from random import randint

def error_inection_location(err_number,max):
    err_list = []
    for _ in range(err_number):
        fault = random.randint(0,max)
        err_list.append(fault)
    return err_list

def faulty_pre_process(a,b,err_number):
    faults = error_inection_location(err_number,len(a))
    res = []
    for i in range(len(a)):
        if(i in faults):
            rand = random.randint(0,len(a))
            res.append(rand)
        else:
            res.append(a[i]*b[i])
    return res   

def pre_process(a,b):
    res = []
    for i in range(len(a)):
        res.append(a[i]*b[i])
    return res

def err_detection_scheme(a,b,err_number):
    faulty_res = faulty_pre_process(a,b,err_number)
    a_shifted = a[1:] + a[0:1]
    b_shifted = b[1:] + b[0:1]
    res_1 = pre_process(a_shifted,b_shifted)
    res_1_final = [res_1[-1]] + res_1[0:-1]
    if faulty_res == res_1_final:
        return False
    else:
        return True

n = 512
q = 12289
testcases = 100000
detected_errors = 0
err_number = 2
for i in range(testcases):
    a =[randint(0,q-1) for x in range(n)]
    b =[randint(0,q-1) for x in range(n)]
    answ = err_detection_scheme(a,b,err_number)
    if(answ == True):
        detected_errors = detected_errors + 1

print(":::Preprocessing:::\nPrecision is: {precision}%, Number of samples: {testcases}, N = {N}".format(testcases=testcases,
                N = n,
                detected_error=detected_errors,
                precision=(detected_errors/testcases)*100))

    
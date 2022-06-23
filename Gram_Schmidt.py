'''
Copyright 2021 JuanYeo

Linear Algebra HW#3: Gram-Schmidt Method
.ipynb -> .py
'''

import numpy as np

def gram_schmidt_method(A):
    A = np.array(A, dtype='f')
    Q = []
    
    for i in range(len(A)):
        A_n = A[i]
        for j in range(i):
            A_n -= (Q[j].dot(A[i])) * Q[j]
        volume_An = np.sqrt(np.sum(np.square(A_n)))
        q_n = A_n / volume_An
        Q.append(q_n)
    
    Q = np.round(Q, 3)
    return Q

def prove_orthonormality(Q):
    orthonormality = True
    for i in range(len(Q)):
        volume_Qn = np.sum(np.square(Q[i]))
        if round(volume_Qn, 1) != 1:
            orthonormality = False
            
        for j in range(i):
            inner_product = Q[i].dot(Q[j])
            if round(inner_product, 1) != 0:
                orthonormality = False
    
    return orthonormality

def run_gram_schmidt():
    n = int(input('enter the Number of Vector Dimension: '))
    m = int(input('enter the Number of Vectors: '))
    i = m
    A = []
    while m > 0:
        v = list(input('enter the Vector ' + str(i - m + 1) + ": ").split())
        if len(v) == n:
            A.append(v)
            m -= 1
        else:
            print('ERROR: wrong vector dimension - Please enter the correct vector...')
    
    Q = gram_schmidt_method(A)
    orthonormality = prove_orthonormality(Q)
    print_result(Q, orthonormality)
    
def print_result(Q, orthonormality):
    print('\nOrthonormal Basis Vectors')
    for n in range(len(Q)):
        print('q' + str(n+1) + ': [' + ' '.join(str(e) for e in Q[n]) + ']')
    if orthonormality:
        print('\nOrthonormality Test Result: PASS')
    else:
        print('\nOrthonormality Test Result: FAIL')

run_gram_schmidt()


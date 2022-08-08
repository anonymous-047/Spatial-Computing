# -*- coding: utf-8 -*-
"""branched 5 inputs OR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aQ1xuL-aXiDwV69cUr1kim7podJevoMM
"""

import math
import itertools
from itertools import *
import numpy as np
import collections
from itertools import groupby
import random
import sys
import copy
import time

def toint(array_tar):
  m,n = array_tar.shape 
  a = 2**np.arange(n)[::-1]  # -1 reverses array of powers of 2 of same length as bits
  return array_tar @ a

def or_operation_for2_v5(array_tar):  # not branched
    # array_tar = array_tar[0:20000]
    arr_bin = toint(array_tar)
    # print(arr_bin.shape)
    len1 = arr_bin.shape[0]
    n = (len1 // 5000) + 1
    arr_bin = arr_bin.reshape(len1, 1)
    # np.array_split(arr_bin, n)
    resu_array = np.array([0])
    for i in range(n):
        for j in range(i, n):
            l1 = np.array_split(arr_bin, n)[i].shape[0]
            l2 = np.array_split(arr_bin, n)[j].shape[0]

            array1 = np.full((l1, l2), np.array_split(arr_bin, n)[i])
            array2 = np.full((l1, l2), np.array_split(arr_bin, n)[j].T)
            or_re = np.bitwise_or(array1, array2)
            resu = np.unique(or_re)
            if resu_array.shape[0] == 1:
                resu_array = np.hstack((resu_array, resu))
                resu_array = resu_array[1:]

            else:
                resu_array = np.hstack((resu_array, resu))
                resu_array = np.unique(resu_array)
                print(resu_array.shape,j)

    # resu_array = np.unique(resu_array)
    return resu_array

def or_operation_for2_v6(array_tar,block_n): # 5 inputs, branched
    arr_bin = toint(array_tar)
    len1 = arr_bin.shape[0]
    
    if block_n == 1:
        arr_bin_1 = arr_bin[0:80000]
    elif block_n == 5:
        arr_bin_1 = arr_bin[320001:]
    else: 
        arr_bin_1 = arr_bin[(block_n-1)*80000+1:block_n*80000]
    len2 = arr_bin_1.shape[0]

    n = (len1 // 5000) + 1
    m = (len2 // 5000) + 1
    arr_bin = arr_bin.reshape(len1, 1)
    arr_bin_1or = arr_bin_1.reshape(len2, 1)
    
    resu_array = np.array([0])
    for i in range(m):
        for j in range(n):
            l1 = np.array_split(arr_bin_1or, m)[i].shape[0]
            l2 = np.array_split(arr_bin, n)[j].shape[0]

            array1 = np.full((l1, l2), np.array_split(arr_bin_1or, m)[i])
            array2 = np.full((l1, l2), np.array_split(arr_bin, n)[j].T)
            or_re = np.bitwise_or(array1, array2)
            resu = np.unique(or_re)
            if resu_array.shape[0] == 1:
                resu_array = np.hstack((resu_array, resu))
                resu_array = resu_array[1:]

            else:
                resu_array = np.hstack((resu_array, resu))
                resu_array = np.unique(resu_array)
                print(resu_array.shape,j)


    # resu_array = np.unique(resu_array)
    return resu_array

def or_operation_for2_v6_1(array_tar,block_n): # test for 4 inputs
    arr_bin = toint(array_tar)
    len1 = arr_bin.shape[0]
    
    if block_n == 1:
        arr_bin_1 = arr_bin[0:1500]
    elif block_n == 3:
        arr_bin_1 = arr_bin[3001:]
    else: 
        arr_bin_1 = arr_bin[(block_n-1)*1500+1:block_n*1500]
    len2 = arr_bin_1.shape[0]

    n = (len1 // 3000) + 1
    m = (len2 // 3000) + 1
    arr_bin = arr_bin.reshape(len1, 1)
    arr_bin_1or = arr_bin_1.reshape(len2, 1)
    
    resu_array = np.array([0])
    for i in range(m):
        for j in range(n):
            l1 = np.array_split(arr_bin_1or, m)[i].shape[0]
            l2 = np.array_split(arr_bin, n)[j].shape[0]

            array1 = np.full((l1, l2), np.array_split(arr_bin_1or, m)[i])
            array2 = np.full((l1, l2), np.array_split(arr_bin, n)[j].T)
            or_re = np.bitwise_or(array1, array2)
            resu = np.unique(or_re)
            if resu_array.shape[0] == 1:
                resu_array = np.hstack((resu_array, resu))
                resu_array = resu_array[1:]

            else:
                resu_array = np.hstack((resu_array, resu))
                resu_array = np.unique(resu_array)

    # resu_array = np.unique(resu_array)
    return resu_array

def or_operation_for3_v2(array_tar,result_1_or): # original, create square matrix
    arr_bin = toint(array_tar)
    # print(arr_bin.shape)
    len1 = arr_bin.shape[0]
    len2 = result_1_or.shape[0]

    n = (len1 // 5000) + 1
    m = (len2 // 5000) + 1
    arr_bin = arr_bin.reshape(len1, 1)
    arr_bin_1or = result_1_or.reshape(len2, 1)
    
    resu_array = np.array([0])
    for i in range(m):
        for j in range(n):
            l1 = np.array_split(arr_bin_1or, m)[i].shape[0]
            l2 = np.array_split(arr_bin, n)[j].shape[0]

            array1 = np.full((l1, l2), np.array_split(arr_bin_1or, m)[i])
            array2 = np.full((l1, l2), np.array_split(arr_bin, n)[j].T)
            or_re = np.bitwise_or(array1, array2)
            resu = np.unique(or_re)
            if resu_array.shape[0] == 1:
                resu_array = np.hstack((resu_array, resu))
                resu_array = resu_array[1:]

            else:
                resu_array = np.hstack((resu_array, resu))
                resu_array = np.unique(resu_array)

    # resu_array = np.unique(resu_array)
    return resu_array

gate5 = np.load('all gate.npy')

re1 = or_operation_for2_v6(gate5,1)
re2 = or_operation_for2_v6(gate5,2)
re3 = or_operation_for2_v6(gate5,3)
re4 = or_operation_for2_v6(gate5,4)
re5 = or_operation_for2_v6(gate5,5)


final = np.hstack((re1,re2,re3,re4,re5))
final = np.unique(final)

print(final.shape)

# def or_operation_for2(array_tar): # original, create square matrix
#     set1 = set()
#     len1 = array_tar.shape[0]
#     len2 = array_tar.shape[1]

#     array1 = np.full((len1,len1,len2),array_tar)
#     array2 = array1.transpose((1,0,2))
#     start1 = time.time()
#     or_re = np.logical_or(array1,array2)*1
#     or_re = np.reshape(or_re,(len1*len1,-1))
#     end1 = time.time()
#     print(end1-start1)
#     start4 = time.time()
#     re = toint(or_re)
#     re_list = re.tolist()
#     for item in re_list:
#         set1.add(item)
#     end4 = time.time()
#     print(end4-start4)

#     return len(set1)

# def or_operation_for2_v2(array_tar): # original, create square matrix
#     # array_tar = array_tar[0:1000]
#     start1 = time.time()
#     arr_bin = toint(array_tar)
#     len1 = arr_bin.shape[0]
#     arr_bin = arr_bin.reshape(len1,1)
#     array1 = np.full((len1,len1),arr_bin)
#     array2 = array1.T
#     or_re = np.bitwise_or(array1,array2)*1
#     or_re = np.reshape(or_re,(1,len1*len1))
#     or_re = or_re[0]
#     re_list = or_re.tolist()
#     re_set = set(re_list)
#     end1 = time.time()
#     print(end1-start1)
#     return len(re_set)

# def or_operation_for2_v3(array_tar): # original, create square matrix
#     # array_tar = array_tar[0:10000]
#     start1 = time.time()
#     arr_bin = toint(array_tar)
#     len1 = arr_bin.shape[0]
#     arr_bin = arr_bin.reshape(len1,1)
#     array1 = np.full((len1,len1),arr_bin)
#     array2 = array1.T
#     or_re = np.bitwise_or(array1,array2)*1
#     iu1 = np.triu_indices(len1)
#     or_re = or_re[iu1]
#     re_list = or_re.tolist()
#     re_set = set(re_list)
#     end1 = time.time()
#     print(end1-start1)
#     return len(re_set)

# def or_operation_for3_v1(array_tar,result_1_or): # original, create square matrix
#     m = result_1_or.shape[0]

    
#     arr_bin = toint(array_tar)
#     n = arr_bin.shape[0]
#     arr_bin = arr_bin.reshape(n,1)
#     array1 = np.full((m,n),arr_bin.T)

#     arr_bin_1_or = result_1_or.reshape(m,1)
#     array2 = np.full((m,n),arr_bin_1_or)
#     or_re = np.bitwise_or(array1,array2)
#     resu = np.unique(or_re)

#     return resu

# def or_operation_for2_v4(array_tar): # original, create square matrix
#     # array_tar = array_tar[0:20000]
#     start1 = time.time()
#     arr_bin = toint(array_tar)
#     # print(arr_bin.shape)
#     len1 = arr_bin.shape[0]
#     arr_bin = arr_bin.reshape(len1,1)
#     array1 = np.full((len1,len1),arr_bin)
#     array2 = array1.T
#     or_re = np.bitwise_or(array1,array2)*1
#     iu1 = np.triu_indices(len1)
#     or_re = or_re[iu1]
#     resu = np.unique(or_re)
#     end1 = time.time()
#     print(end1-start1)
#     return resu

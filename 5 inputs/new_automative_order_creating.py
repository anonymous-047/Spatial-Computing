# -*- coding: utf-8 -*-
"""8.1 automative order creating-parallel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HrJN9fs1bcb9QKfPz8XQxPxk3nLzq8Na
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
import queue
from queue import Queue
from collections import deque

def bandpass(matrix_target,threshold):
    shape = matrix_target.shape
    threshold_m = np.full(shape, threshold)
    result = 1*np.greater(matrix_target,threshold_m)
    return result

def bandpass_inverse(matrix_target,threshold):
    shape = matrix_target.shape
    threshold_m = np.full(shape, threshold)
    result = 1*np.greater(threshold_m,matrix_target)
    return result

def del_same(tar):
    tar01 = [list(t) for t in set(tuple(_) for _ in tar)]
    return tar01


def compare_item(dict01, dict02,dict03,num):
    list_164 = []
    list_256 = []
    for value in dict02[num]:
        if value not in dict01[num]:
            list_164.append(value)
    for value in dict03[num]:
        if value not in dict01[num]:
            list_256.append(value)
    return list_164,list_256

def compare_whole(dict01, dict02,dict03):
    list_g = []
    for i in range(9):
        compare_item(dict01, dict02,dict03,i)

def check_miss_item(dict01, dict02,dict03,num):
    list_256_164 = []
    list_new = []
    for value in dict03[num]:
        if value not in dict02[num]:
            list_256_164.append(value)
    for value in dict01[num]:
        if value in list_256_164:
            list_new.append(value)
    return list_256_164,list_new    


def ori_result(position,num):
    if position >=result.shape[0]:
        position = position-num**2
    
    return result[position]

def exchange(num):
    """
    from the position in get from logic gates in total01 to matrix
    """
    r,c = 0,0
    if num>=result.shape[0]:
        num=num-result.shape[0]
  
    width= result.shape[0]**(1/2)
    r = int(num/width)
    c = int(num%width)
    return [r,c]


def exchange_list(list_tar):
    list_new = []
    for item in list_tar:
        list_new.append(exchange(item) )
    return list_new

def try_thr(result_matrix, start, end,num):
    list_re = []
    thr = np.linspace(start,end,num)
    for item in thr:
        rebp = bandpass(result_matrix,item)
        reivbp = bandpass_inverse(result_matrix, item)
        total01 = np.concatenate((rebp,reivbp),axis = 0)
        total = del_same(total01)
        list_re.append(total)
    list_re = [item for sublist in list_re for item in sublist]
    list_re = del_same(list_re) 
    return list_re  

def dictionary_outcome(tar,state):
    dict_outcome = { }
    for i in range(state+1):
        dict_outcome[i]=[item for item in tar if np.sum(item)==i]
        
    for key, value in dict_outcome.items():
        print(key,len(value),value)
    return dict_outcome

def get_result(n,x1,y1,x2,y2,x3,y3,x4,y4,mu,num):
    matrix0000, matrix1000, matrix0100, matrix0010, matrix0001, matrix1100, matrix1010, matrix1001,matrix0110, matrix0101, matrix0011, matrix1110, matrix1101, matrix1011, matrix0111, matrix1111= get_probability(n,x1,y1,x2,y2,x3,y3,x4,y4,mu,num)
    whole = np.vstack(((matrix0000, matrix1000, matrix0100, matrix0010, matrix0001, matrix1100, matrix1010, matrix1001,matrix0110, matrix0101, matrix0011, matrix1110, matrix1101, matrix1011, matrix0111, matrix1111 )))
    AHL = whole.T
    result = GFP(whole)
    G = result.T
    return AHL, G

def check_miss_item2(dict01, dict02,num):
    list_new = []
    for value in dict01[num]:
        if value not in dict02[num]:
            list_new.append(value)
    return list_new  

def try_thr01(result_matrix, start1, end1, start2, end2,num1,num2):
    list_re = []
    thr1 = np.linspace(start1,end1,num1)
    thr2 = np.linspace(start2,end2,num2)
    thr = np.hstack((thr1,thr2))
    for item in thr:
        rebp = bandpass(result_matrix,item)
        reivbp = bandpass_inverse(result_matrix, item)
        total01 = np.concatenate((rebp,reivbp),axis = 0)
        total = del_same(total01)
        list_re.append(total)
    list_re = [item for sublist in list_re for item in sublist]
    list_re = del_same(list_re) 
    return list_re 


def fun_threshold(input_matrix, threshold):
    result = 1*(input_matrix>threshold)
    return result

def inv_threshold(input_matrix, threshold):
    result = 1*(input_matrix<threshold)
    return result

def reduce_dim(threeD):
    threeD = threeD.reshape(-1, threeD.shape[-1])
    return threeD

def convert(list):
    return (*list, )

def del_same(tar):
    tar01 = [list(t) for t in set(tuple(_) for _ in tar)]
    return tar01

def dictionary_outcome(tar,state):
    dict_outcome = { }
    for i in range(state+1):
        dict_outcome[i]=[item for item in tar if np.sum(item)==i]
        
    for key, value in dict_outcome.items():
        print(key,len(value),value)
    return dict_outcome

def sort_str(str):
    return ''.join(sorted(str))

def join_str(list_tar):
    return ''.join(list_tar)

def create_and_sort(tar):
    l1 = join_str(tar)
    l1 = sort_str(l1)
    return l1

def contains(substring, string):
    if substring == string:
        return False
    else:
        c1 = collections.Counter(string)
        c2 = collections.Counter(substring)
        return not (c2 - c1)

def get_indx(list1,list_for_index):
    list2 = map((lambda x: list_for_index.index(x)), list1)
    return list(list2)


def orderfun(obj, subitem):
    for item in obj:
        if len(item) > len(subitem) and contains(subitem, item):
            if not(obj.index(subitem) < obj.index(item)):
                return False
            return True

def group_by(position):
    position_no_0 = [item for item in position if item != '0']
    group_by = [list(g) for k, g in groupby(position_no_0, key=len)]
    return group_by

def combine_2_item(list_tar):
    new_list = []
    for i in range(len(list_tar)):
        for j in range(i+1,len(list_tar)):
            new_list.append(sort_str(list_tar[i]+list_tar[j]))

    return new_list
def combine_3_item(list_tar):
    new_list = []
    l = len(list_tar)
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                new_list.append(sort_str(list_tar[i]+list_tar[j]+list_tar[k]))
    return new_list

def generate_list01(obj,num_input):
    new_list = [x for x in obj if (len(x)==num_input and x!= '0')]
    return new_list


def fun_2nd_order(obj,position):
    group = group_by(position)
    list_one = generate_list01(obj,1)
    list_group2 = combine_2_item(list_one) #2 inputs correct order
    list_two = generate_list01(obj,2)
    if not(list_group2 == list_two):
        return False

    return True

def fun_3rd_order(obj,position):
    group = group_by(position)
    list_one = generate_list01(obj,1)
    list_group3 = combine_3_item(list_one) #2 inputs correct order
    list_three = generate_list01(obj,3)
    if not(list_group3 == list_three):
        return False

    return True

def threshold1(array_order, threshold):
    result = 1*np.greater(array_order, threshold)
    return result

def threshold2(array_order, threshold):
    result = 1*np.greater_equal(array_order, threshold)
    return result

def all_threshold(array_order):
    list_re = []
    len = array_order.shape[1]
    for i in range(len):
        result1 = threshold1(array_order, i)
        result2 = threshold2(array_order, i)
        result = np.concatenate((result1, result2), axis = 0)
        result = del_same(result)
        list_re.append(result)
    list_re = [item for sublist in list_re for item in sublist]
    list_re = del_same(list_re) 
    array_re = np.array(list_re)
    return array_re

def bandpass1(array_order, left, right):
    result = 1*np.logical_and(array_order>=left, array_order<=right)
    return result

def bandpass2(array_order, left, right):
    result = 1*np.logical_and(array_order>left, array_order<right)
    return result

def all_bandpass(array_order, leftrange = 7, rightrange = 8):
    list_re = []
    len = array_order.shape[1]
    for i in range(len-1):
        for j in range(i,len):
            result1 = bandpass1(array_order, i, j)
            result2 = bandpass2(array_order, i, j)
            result = np.concatenate((result1,result2),axis = 0)
            result = del_same(result)
            list_re.append(result)
    list_re = [item for sublist in list_re for item in sublist]
    list_re = del_same(list_re) 
    array_re = np.array(list_re)
    return array_re

def all_bandpass2(array_order, leftrange = 15, rightrange = 16):
    list_re = []
    len = array_order.shape[1]
    for i in range(len-1):
        for j in range(i,len):
            result1 = bandpass1(array_order, i, j)
            result2 = bandpass2(array_order, i, j)
            result = np.concatenate((result1,result2),axis = 0)
            result = del_same(result)
            list_re.append(result)
    list_re = [item for sublist in list_re for item in sublist]
    list_re = del_same(list_re) 
    array_re = np.array(list_re)
    return array_re

"""Create list forward"""

def add_item_remove(list_re,next_possible):
    list_re.append(random.choice(next_possible))
    next_possible.remove(list_re[len(list_re)-1])
    return list_re, next_possible

def two_route(list_tar,num1,num2,remain_array):
    route1 = list_tar
    route2 = list_tar
    route1 = np.hstack((route1, remain_array[:,num1].reshape(12,1)))
    route1 = np.hstack((route1, remain_array[:,num2].reshape(12,1)))

    route2 = np.hstack((route2, remain_array[:,num2].reshape(12,1)))
    route2 = np.hstack((route2, remain_array[:,num1].reshape(12,1)))

    stack = np.vstack((route1, route2))
    return stack.tolist()

def map_fun(list_tar,num1,num2):
    map1 = map((lambda item:[item[:] ,[sort_str(item[num1]+item[num2])]]),list_tar)
    list1 = [sum(list(item),[]) for item in map1]
    return list1

def map_fun2(list_tar,num1,num2,num3):
    map1 = map((lambda item:[item[:] ,[sort_str(item[num1]+item[num2]+item[num3])]]),list_tar)
    list1 = [sum(list(item),[]) for item in map1]
    return list1

def map_fun_later1(list_tar,num1,num2,re_later):
    map1 = map((lambda item:[re_later[:] ,[sort_str(item[num1]+item[num2])]]),list_tar)
    list1 = [sum(list(item),[]) for item in map1]
    return list1

def map_fun_later2(list_tar,num1,num2,num3,re_later):
    map1 = map((lambda item:[re_later[:] ,[sort_str(item[num1]+item[num2]++item[num3])]]),list_tar)
    list1 = [sum(list(item),[]) for item in map1]
    return list1

def iter_chain(item):
    return list(itertools.chain.from_iterable(item))

def two_route2(list_tar, num1, num2, num3, num4):
    route1 = map_fun(list_tar,num1,num2)
    route2 = map_fun(list_tar,num3, num4)
    route1 = map_fun(route1,num3,num4)
    route2 = map_fun(route2,num1, num2)
    route = route1 + route2
    return route

def two_route_add1(list_tar,num1,num2,remain_array):
    route1 = list_tar
    route2 = list_tar
    route1 = np.hstack((route1, remain_array[:,num1].reshape(12,1)))

    route2 = np.hstack((route2, remain_array[:,num2].reshape(12,1)))

    stack = np.vstack((route1, route2))
    return stack.tolist()

def two_route_1_3(list_tar,num1,num2,num3):
    route1 = list_tar
    route2 = list_tar
    remain_array = remain(single,list_tar)

    route1 = np.hstack((route1, remain_array))
    route1 = route1.tolist()
    route1 = map_fun2(route1,num1,num2,num3)
    route1 = np.array(route1)

    route2 = map_fun2(route2,num1,num2,num3)
    route2 = np.array(route2)
    route2 = np.hstack((route2,remain_array))

    stack = np.vstack((route1, route2))
    return stack.tolist()

def remain(all_list,list_tar):
    remain = map(lambda item: list(set(all_list)-set(item)), list_tar)
    remain = [list(item) for item in remain]
    return np.array(remain)

def join_str(list_tar):
    return ''.join(list_tar)

def all_possible_combined(current_list):
    next_item_set = [] # the list to put all items aftering combining 
    copy_currentlist = copy.deepcopy(current_list) # decopy the current order so it won't be changing
    for i in range(len(current_list)): 
        for j in range(i, len(current_list)):
            if len(set(current_list[i]) & set(current_list[j])) == 0: # make sure the two items have no same letters
                next_possible = create_and_sort(set(current_list[i]) | set(current_list[j])) # combine the letters and sort in alphabetical order
                if next_possible in current_list:
                    continue # if the otem already existed in the input list, move j to the next and combine with i until the combined element is a new one

                elif next_possible not in copy_currentlist:
                    next_item_set.append(next_possible) # if the item is a new one, add it into next_item_set
                    current_list = current_list[:j] # delete everything after j including j, as the combination of those item with item after current i would be larger than ij
                    break

    re_set = set(next_item_set)-set(copy_currentlist) # make sure no duplicate
    if len(re_set) <= 1: # if there is only 1 or no item possible, no need to filter it, return directly
        return re_set
    else:
        final = filter_states(re_set,copy_currentlist) # if there is more than 1 item, filter the set
        return final


def filter_states(set_tar,current_order):
    # new_set = set_tar
    list_tar = list(set_tar)
    # copy_listtar = copy.deepcopy(list_tar)
    # new_set = [set(item) for item in set_tar]
    for i in range(len(list_tar)):
        for j in range(i,len(list_tar)):
            if set(list_tar[i]) != set(list_tar[j]) and len(set(list_tar[i])& set(list_tar[j])) != 0 and list_tar[i] in set_tar and list_tar[j] in set_tar: # when two items have intersection,
                set1 = set(list_tar[i]) - set(list_tar[j])
                set2 = set(list_tar[j]) - set(list_tar[i])
                print(current_order,list_tar[i],list_tar[j],set1,set2)
                if set1 == set2 == set():
                    continue
                elif set1 == set():
                    set_tar.remove(list_tar[j])

                elif set2 == set():
                    set_tar.remove(list_tar[i])

                else:
                    str1 = create_and_sort(set1)
                    str2 = create_and_sort(set2)
                    if current_order.index(str1) < current_order.index(str2):
                        set_tar.remove(list_tar[j])


                    else:
                        set_tar.remove(list_tar[i])

    return set_tar

def generate_orders_v1(single_input_list, input):
    # to add the next possible states in the dictionary 'move' to the current list
    single_input = set(single_input_list)
    if len(input) == 0:
        input = [[]]

    input1 = [[]]
    for item in input:
        move = {0: (single_input - set(item)), 1: all_possible_combined(item)}
        if len(move[0]) == 0 and len(move[1]) == 0:
            return [item for item in input if len(item) == (2**(len(single_input))-1)]
            # return input
        else:
            for i in move:
                for j in move[i]:
                    new = copy.deepcopy(item)
                    new.append(j)
                    input1.append(new)

            input[:] = input1[:]
            # print(input)

def generate_orders1(single_input_list, input):
    single_input = set(single_input_list)
    if len(input) == 0:
        input = [[]]

    input1 = [['a']] # start with a single input

    for item in input:
        move = {0: (single_input - set(item)), 1: all_possible_combined(item)}
        if len(move[0]) == 0 and len(move[1]) == 0:
            return [item for item in input if len(item) == (2**(len(single_input))-1)]
            # return input
        else:
            for i in move:
                for j in move[i]:
                    new = copy.deepcopy(item)
                    new.append(j)
                    input1.append(new)

            input[:] = input1[:]
            # print(input)

single_position = ['a','b','c','d']
start = [] # this gets all the results

re = generate_orders(single_position, start)
print(np.array(re).shape)

current = ['a','b','c','d','e']
start = [[]] # this gets results starting with 'a' only

re = generate_orders(current, start)

print(np.array(re).shape)

13104/4

def add_zero(list_tar):
    re_array = np.array(list_tar)
    zero = np.full((re_array.shape[0],1),'0')
    re_array = np.hstack((zero,re_array))
    return re_array

def get_all_index(state_list, all_order_array):
    index = []
    all_order_list = all_order_array.tolist()
    for item in all_order_list:
        ree = get_indx(state_list, item)
        index.append(ree)
    index_array = np.array(index)
    return index_array

def process_steps_combined(index_array):
    bp = all_bandpass2(index_array)
    ivbp = 1*np.less(bp,1)
    all_gate = np.concatenate((bp, ivbp),axis = 0)
    all_gate = del_same(all_gate)
    all1 = np.array(all_gate)
    return all1

np.save('order_index_a',np.array(re))

position1 = ['a', 'b', 'c','d','e']
position2 = itertools.combinations(position1,2)
position3 = itertools.combinations(position1,3)
position4 = itertools.combinations(position1,4)
position5 = itertools.combinations(position1,5)
lst2 = [list(item) for item in position2]
lst3 = [list(item) for item in position3]
lst4 = [list(item) for item in position4]
lst5 = [list(item) for item in position5]

lst = lst2+lst3+lst4+lst5
new_list = []
for item in lst:
    new_list.append(''.join(item))



all_position = ['0']+position1 +new_list
print(all_position)

re_array = add_zero(re)
index_array = get_all_index(all_position,re_array)

np.save('order_index_a',index_array)

print(index_array[0:10])

def ProducerThread_v2(single_input_list):
    single_input = set(single_input_list)
    global queue_order
    global queue_next_item
    while True:
        item = queue_order.get()
        move = {0: (single_input - set(item)), 1: all_possible_combined(item)}
        if move[0] == set() and move[1] == set():
            queue_order.put(item)
            return list(queue_order.queue)

        else:
            new_set = move[0] | move[1]
            new_list = [item for item in new_set]
            for next_item in new_list:
                queue_order.put(item+[next_item])
            # print(list(queue_order.queue))

from queue import Queue

single = ['a', 'b', 'c','d','e']
queue_order = Queue(maxsize=0)
queue_order.put(['a'])
queue_next_item = Queue(maxsize=0)



re = ProducerThread_v2(single)

print(len(re))

# Summer-Project

## Spatial Computing 
> The aim of this project is to get the least number of outputs to get all the possible logic gates for n inputs. This repository contains the code for 
activation functions, the code for the generation of orders, the code used to compute the OR operation, and some of the results.

## Table of Contents
* [Generation of orders](#generation-of-orders)
* [OR operation](#or-operation)
* [Result data](https://github.com/Enbo-Lyu/Summer-Project/blob/f590c1fcdd129b6fb164b8d757c827484f2df729/4%20inputs/4%20input%201%20or%20int%20result.npy)



## Generation of orders
- [Code](automative_order_creating_per_branch+logic_gate.py)
- Here contains the code used to generate all possible orders. Using Queue, in each step, generate a dictionary that contains all the possible elements for next step based on the current item.
- There are two main functions for the generation of orders.
- 1. Next Possible item generation
- * Take the current list order as input eg.[a, b, ab, c, d]
- * Take the first item in the input list first (ie. a), as it is the one with the smallest concentration, combine it with the element after it in the order of the input list in order(b, ab, c, d).
- * If the combined item has existed in the current list(ab is in the list), combine with the next item(c) until there is an item that is not in the list, add that the combined item into a list that would contain all possible item. This item would be the one with least concentration starting with the first item(a). If all the combined item have already existed, move to the second element in the current list.
- * After combining the previous item, delete the item combined with the first item(d) and all elements after it in the current list.(a,b,ab,c)
- * Then move to the next item(b) and repeat the same thing(bc) until there is no more item to add.
- * All the item added to the list will be compared with each other in the next function.


- 2. Filter states
- * After getting the previous list, if the items in it do not contain same letter, then we do not know which have higher concentration, therefore all of them can be the possible next item, and will be in the dictionary move with key 1. eg: 1: [ab, ce]
- * if they contains same letter, then the function deletes the letter appears in both of them, then compare the rest using the current order, then delete the one with higher order. Eg.[abe, acd], then check in current list does ‘be’or ‘cd’come first.
- * After comparing all items, the items left will be added into set in the dictionary with key 1.
- * Then the items in the dictionary with both key 0 and 1 will be added to the current list separately.

- 3. Generate by branches
- * To make the process of generation shorter, we can generate only one branch of orders, use different label to map the orders to get all the possible index order.
- * Generation of one branch of order takes (T/n), T is the time needed to generate all the orders, n is the number of inputs.
Eg: start the Queue with [‘a’], then all the order in this branch will start with ‘a’.




## OR operation
- [Code](https://github.com/Enbo-Lyu/Summer-Project/blob/f590c1fcdd129b6fb164b8d757c827484f2df729/OR/or%20operation.py)
- Here contains the code used to do the OR operation.
- * Turn logic gate into int number
- * Use bitwise_or instead of logical_or
- * Use numpy.array operation instead of ‘for loop’
- * Split the data into chunks to avoid running out of memory
- * Run the program in several branches in parallel to save time



## Result data
- [3 inputs 1 output logic result](https://github.com/Enbo-Lyu/Spatial-Computing/blob/d040073ca119ac057f7bebdf5d111b9d1ba9c7f6/Result/3%20inputs%201%20output%20logical%20result.npy)
- [4 inputs 1 output logic result](https://github.com/Enbo-Lyu/Spatial-Computing/blob/d040073ca119ac057f7bebdf5d111b9d1ba9c7f6/Result/4inputs_1output_gate.npy)
- [4 inputs 2 outputs int result](https://github.com/Enbo-Lyu/Spatial-Computing/blob/d040073ca119ac057f7bebdf5d111b9d1ba9c7f6/Result/4%20input%201%20or%20int%20result.npy)
- [4 inputs 3 outputs int result](https://github.com/Enbo-Lyu/Spatial-Computing/blob/d040073ca119ac057f7bebdf5d111b9d1ba9c7f6/Result/4%20input%202%20or%20int%20result.npy)
- [5 inputs 1 output logic result](https://drive.google.com/file/d/1gC_lEHDxMGpLRobRxAUgQKVWXsBEIEtQ/view?usp=sharing)





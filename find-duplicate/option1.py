# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

import numpy as np

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

#Code:
#this imitates the action of looking at a calendar:
#to see if two events happen on the same day, we first label one down
#, and see the other date occurs on a "filled" day
def find_dup(array):
    l=[0]*len(array+1)#define empty list
    for i in range(len(array)):
        if array[i]==l[array[i]]:# check if two identical numbers "bump"
            print(array[i])
        l[array[i]]=array[i]
#this code reduces efficiency to O(n), so a pretty nice code
#%%
import numpy as np
#2-D search
def find_dup_lame(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]==array[j]:#check for match
                print(array[i])
# time complexity of O(n^2), terrible algorithm

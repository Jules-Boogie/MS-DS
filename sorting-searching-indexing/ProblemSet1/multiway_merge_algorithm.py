# Problem 3 (Develop Multiway Merge Algorithm, 15 points).
# We studied the problem of merging 2 sorted lists lst1 and lst2 into a single sorted list in time  Θ(𝑚+𝑛)  where  𝑚  is the size of lst1 and  𝑛  is the size of lst2. Let twoWayMerge(lst1, lst2) represent the python function that returns the merged result using the approach presented in class.

# In this problem, we will explore algorithms for merging k different sorted lists, usually represented as a list of sorted lists into a single list.


#  Implement an algorithm that will implement the 𝑘 way merge by calling twoWayMerge repeatedly as follows:

# Call twoWayMerge on consecutive pairs of lists twoWayMerge(lists[0], lists[1]), ... , twoWayMerge(lists[k-2], lists[k-1]) (assume k is even).
# Thus, we create a new list of lists of size k/2.
# Repeat steps 1, 2 until we have a single list left.


def twoWayMerge(lst1, lst2):
    # Implement the two way merge algorithm on 
    #          two ascending order sorted lists
    # return a fresh ascending order sorted list that 
    #          merges lst1 and lst2
    new_list = []
    n_1 = len(lst1)
    n_2 = len(lst2)
    s1 = 0
    s2 = 0
    while s1 < n_1 and s2 < n_2:
        if lst1[s1] < lst2[s2]:
            new_list.append(lst1[s1])
            s1 += 1
        elif lst1[s1] == lst2[s2]:
            new_list.append(lst1[s1])
            new_list.append(lst2[s2])
            s1 +=1
            s2 +=1
        else:
            new_list.append(lst2[s2])
            s2 += 1
    while s1 < n_1:
        new_list.extend(lst1[s1:])
        break
    while s2 < n_2:
        new_list.extend(lst2[s2:])
        break
    return new_list
        
# given a list_of_lists as input, 
#   if list_of_lists has 2 or more lists, 
#        compute 2 way merge on elements i, i+1 for i = 0, 2, ...
#   return new list of lists after the merge
#   Handle the case when the list size is odd carefully.
def oneStepKWayMerge(list_of_lists):
    if (len(list_of_lists) <= 1):
        return list_of_lists
    ret_list_of_lists = []
    k = len(list_of_lists)
    for i in range(0, k, 2):
        if (i < k-1):
            ret_list_of_lists.append(twoWayMerge(list_of_lists[i], list_of_lists[i+1]))
        else: 
            ret_list_of_lists.append(list_of_lists[k-1])
    return ret_list_of_lists
    
    
# Given a list of lists wherein each 
#    element of list_of_lists is sorted in ascending order,
# use the oneStepKWayMerge function repeatedly to merge them.
# Return a single merged list that is sorted in ascending order.
def kWayMerge(list_of_lists):
    k = len(list_of_lists)
    if k == 1:
        return list_of_lists[0]
    else:
        new_list_of_lists = oneStepKWayMerge(list_of_lists)
        return kWayMerge(new_list_of_lists)
        
# BEGIN TESTS
lst1= kWayMerge([[1,2,3], [4,5,7],[-2,0,6],[5]])
assert lst1 == [-2, 0, 1, 2, 3, 4, 5, 5, 6, 7], "Test 1 failed"

lst2 = kWayMerge([[-2, 4, 5 , 8], [0, 1, 2], [-1, 3,6,7]])
assert lst2 == [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], "Test 2 failed"

lst3 = kWayMerge([[-1, 1, 2, 3, 4, 5]])
assert lst3 == [-1, 1, 2, 3, 4, 5], "Test 3 Failed"

print('All Tests Passed = 15 points')
#END TESTS
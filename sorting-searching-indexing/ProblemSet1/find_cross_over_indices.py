# Problem 1: Find Crossover Indices.
# You are given data that consists of points  (𝑥0,𝑦0),…,(𝑥𝑛,𝑦𝑛) , wherein  𝑥0<𝑥1<…<𝑥𝑛 , and  𝑦0<𝑦1…<𝑦𝑛  as well.

# Furthermore, it is given that  𝑦0<𝑥0  and  𝑦𝑛>𝑥𝑛 .

# Find a "cross-over" index  𝑖  between  0  and  𝑛−1  such that  𝑦𝑖≤𝑥𝑖  and  𝑦𝑖+1>𝑥𝑖+1 .

# Note that such an index must always exist (convince yourself of this fact before we proceed).

# (A) Design an algorithm to find an index  𝑖∈{0,1,…,𝑛−1}  such that  𝑥𝑖≥𝑦𝑖  but  𝑥𝑖+1<𝑦𝑖+1 .

# Describe your algorithm using python code for a function findCrossoverIndexHelper(x, y, left, right)

# x is a list of x values sorted in increasing order.
# y is a list of y values sorted in increasing order.
# x and y are lists of same size (n).
# left and right are indices that represent the current search region in the list such that 0 <= left < right <= n
# Your solution must use recursion.

# Hint: Modify the binary search algorithm we presented in class.



def findCrossoverIndexHelper(x, y, left, right):
    # Note: Output index i such that 
    #         left <= i <= right
    #         x[i] <= y[i]
    # First, Write down our invariants as assertions here
    assert(len(x) == len(y))
    assert(left >= 0)
    assert(left <= right-1)
    assert(right < len(x))
    # Here is the key property we would like to maintain.
    assert(x[left] > y[left])
    assert(x[right] < y[right])
    
    while(left < right):
        mid = (left+right)//2
        if x[mid] > y[mid] and x[mid+1] < y[mid+1]:
            return mid
        if x[mid] < y[mid] and y[mid-1] < x[mid-1]:
            return mid-1
        if x[mid] < y[mid] and y[mid-1] > x[mid-1]:
            return findCrossoverIndexHelper(x, y, 0, mid)
        if x[mid] > y[mid]  and x[mid+1] > y[mid+1]:
            return findCrossoverIndexHelper(x, y, mid, len(y)-1)
            
def findCrossoverIndex(x, y):
    assert(len(x) == len(y))
    assert(x[0] > y[0])
    n = len(x)
    assert(x[n-1] < y[n-1]) # Note: this automatically ensures n >= 2 why?
    return findCrossoverIndexHelper(x,y,0,n-1)
    
# BEGIN TEST CASES
j1 = findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 5, 6, 7, 8, 9])
print('j1 = %d' % j1)
assert j1 == 1, "Test Case # 1 Failed"

j2 = findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 4.2, 4.3, 4.5, 8, 9])
print('j2 = %d' % j2)
assert j2 == 1 or j2 == 5, "Test Case # 2 Failed"

j3 = findCrossoverIndex([0, 1], [-10, 10])
print('j3 = %d' % j3)
assert j3 == 0, "Test Case # 3 failed"

j4 = findCrossoverIndex([0,1, 2, 3], [-10, -9, -8, 5])
print('j4 = %d' % j4)
assert j4 == 2, "Test Case # 4 failed"

print('Congratulations: all test cases passed - 10 points')
#END TEST CASES
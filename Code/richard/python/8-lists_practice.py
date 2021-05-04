# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"


# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even 
# numbers.

def even_even(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return True if count % 2 == 0 else False

def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False

## Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    reversedList = []
    i = len(nums) - 1
    while i >= 0:
        reversedList.append(nums[i])
        i -= 1
    return reversedList

def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]

# Common Elements
# Write a function to find all common elements between two lists.

def common_elements(nums1, nums2):
    numsDict = {}
    commonElements = []
    for i in range(len(nums1)):
        numsDict[nums1[i]] = 1
    for i in range(len(nums2)):
        if nums2[i] in numsDict.keys():
            commonElements.append(nums2[i])
    return commonElements

def test_common_elements():
    assert(common_elements([1, 2, 3], [2, 3, 4])) == [2, 3]

# Combine
# Write a function to combine two lists of equal length into one, alternating elements.

def combine(nums1, nums2):
    combinedList = []
    for i in range(len(nums1)):
        combinedList.append(nums1[i])
        combinedList.append(nums2[i])
    return combinedList


def test_combine():
    assert(combine(['a','b','c'],[1,2,3])) == ['a', 1, 'b', 2, 'c', 3]

# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a 
# target number. 

def find_pair(nums, target):
    pair = []
    i = 0
    while i < len(nums):
        j = i
        while j < len(nums):
            if nums[i] + nums[j] == target:
                pair.append(nums[i])
                pair.append(nums[j])
            j += 1
        i += 1
    return pair


def test_find_pair():
    assert(find_pair([5, 6, 2, 3], 7)) == [5, 2]

#Optional: return a list of all pairs of numbers that sum to a target value.

def find_pair_list(nums, target):
    pair = []
    i = 0
    while i < len(nums):
        j = i
        while j < len(nums):
            if nums[i] + nums[j] == target:
                tup = (nums[i],nums[j])
                pair.append(tup)
            j += 1
        i += 1
    return pair


def test_find_pair_list():
    assert(find_pair_list([5, 6, 2, 3], 7)) == [(5, 2)]


'''
# Average
# Write a function to find the average of a list of numbers


def average(nums):
    ...
print(average([1, 2, 3, 4, 5])) # 3


# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    ...
print(remove_empty(['a', 'b', '', 'c', '', 'd'])) # ['a', 'b', 'c', 'd']



# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a 
# list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    ...
print(merge([5,2,1], [6,8,2])) # [[5,6],[2,8],[1,2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element 
# from each of the lists.


def combine_all(nums):
    ...
print(combine_all([[5,2,3],[4,5,1],[7,6,3]])) # [5,2,3,4,5,1,7,6,3]


# Fibonacci
# Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci 
# Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    ...
print(fibonacci(8)) # [1, 1, 2, 3, 5, 8, 13, 21]

# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.


def factorial(n):
  ...
print(factorial(5)) # 120


# Find Unique
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.


def find_unique(nums):
    ...
nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_nums = find_unique(nums) # [12, 24, 35, 88, 120, 155]



## Progressive Tax

# Income Percentage of Income
# Paid in Tax Amount of Tax
# $5,000 10%
# $50,000 25%
# $100,000 28%
# $150,000 33%
# $350,000 35%



'''
#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Week 02
Practice 03 - Loops Practice
Jared Nistler
'''
#-----------------------------------------------#
# Instructions
#-----------------------------------------------#
'''
Practice 3: While and For Loops
Copy and paste this file into your own "03_loops.py"
Fill in the code for each of the functions
Run the tests by typing "pytest 03_loops.py"
'''

# Double Numbers
# Write a function that takes a list of numbers and returns 
# a new list with every number doubled

def double_numbers(nums):
    for num in range(len(nums)):
        nums[num] *= 2
    return nums

def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]


# Stars
# Write a function that takes an integer and returns that 
# number of asterisks in a string

def stars(n):
    i = 0
    star_str = ""
    while i<n:
        star_str += '*'
        i += 1
    return star_str

def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'


# Extract Less Than Ten
# Write a function to move all the elements of a list 
# with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    ten_list = []
    for num in nums:
        if num < 10:
            ten_list.append(num)
        else:
            continue
    return ten_list

def test_extract_less_than_ten():
    assert extract_less_than_ten([2, 8, 12, 18]) == [2, 8]
"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 7) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
    
What if n is:
    + a string -- if it's not an int, force to int with int()
    + a float -- if its not an int, force to int with int()
    + negative -- return empty list
    + complex number?  -- don't need to deal with this

What if the list 
    + is empty
"""


def last(a, n):
    # Your code here                                 
    # Make sure n is an int
    try:
        n = int(n)
    except ValueError:
        return "invalid number"
    #  Make sure n isn't too large
    if n > len(a):
        return "invalid"
    # Make sure n is positive
    if n == 0:
        return []
    # # Check if n is 0 
    # if n == 0 
    #     return []
    # Get the last elements from the list  
    result = []
    # Loop n times
    for _ in range(n):
        # pop the value off the end of the list 
        val = a.pop()
        # insert the value at the front of the result list 
        result.insert(0, val)

    return result

print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], -7))
print(last([1, 2, 3, 4, 5], 7), 'beej')
         
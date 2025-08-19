num_string = "012345"
one_two_three = num_string[-5:-2]
print(one_two_three)


"""Since in Python, strings are arrays, we can use the same syntax for both object types.

Slicing segments an array and returns that segment.

In the example below, a string is segmented to return a single word from within the string:"""

hello_world_string = "Hello World!"
world = hello_world_string[6:11]
print(world)

"""The start is the index of the array that you would like the slice to begin with, the stop is the index of the array you would like to stop at.

The value of the array at the stop index is not included in the slice."""

num_string = "012345"
zero_to_four = num_string[0:5]
print(zero_to_four)

# array[start:stop:step]

num_string = "0123456"
even_nums = num_string[2::2]
print(even_nums)

"""Negative Indexing
Slicing can use negative indexing. With negative indexing, the last value in an array is -1, the second last is -2, and so on.

For example:"""

num_string = "012345"
one_two_three = num_string[-5:-2]
print(one_two_three)


"""Reversing Arrays with Negative Indexing
Use negative indexing to step through an array in reverse.

For example"""
num_string = "012345"
reverse_string = num_string[::-1]
print(reverse_string)






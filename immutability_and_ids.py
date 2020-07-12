# While result and another_result are just different names bound to the same
# variable. This is an example of immutability.
result = True
another_result = result
print(id(result))
print(id(another_result))

del result
del another_result

# The course instructer says that the id number is not necessarily the memory
# address, unless you're using CPython, and then when you run the program
# again, it might not always be the same id, and that when you delete and recreate
# the variable, id might change. But I guess this is CPython
# bc even when I delete the value and recreate it, the id remains the same
# Perhaps it is in fact the memory address

# Okay this is super fucking weird. A_different_result, which is presumably
# bound to a different variable (a different boolean?), it returns the same
# id. Are all trues the same true?
result = True
a_different_result = True
print(id(result))
print(id(a_different_result))
result = False
print(id(result))

# Lookit dat! When result gets changed to false, the id changes!

# Strings are also immutable

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
print(id(another_result))

# While the id for result changed, because it had to create a new string
# and bind the result variable to it, because strings are immutable,
# Python could not change the value of result, and was forced to create a
# a new string and bind it to the result variable, while another_result
# remained the same
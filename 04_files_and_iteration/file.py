f = open("hello.py")
iter(f) is f

# True

################################
myList = [1, 3, 4, 5, 6, 7, 8, 9]
iter(myList) is myList

# False

################################

# When we store the reference of a file in a variable, it is itself an iteratable object.
# But, when we store the reference of a list in a variable, it is not an iteratable object itself. (it is the reference of the actual list)
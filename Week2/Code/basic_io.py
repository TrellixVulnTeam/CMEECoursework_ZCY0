#!/usr/bin/env python3

"""combination of the previous 3 scripts, read and save files"""

__appname__ = 'basic_io.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'


#############################
# FILE INPUT
#############################
# Open a file for reading
f = open('/home/nelson/Documents/CMEECoursework/Week2/Sandbox/test.txt', 'r')
# use "implicit" for loop:
# if the object is a file, python will cycle over lines
for line in f:
    print(line)

# close the file
f.close()

# Same example, skip blank lines
f = open('/home/nelson/Documents/CMEECoursework/Week2/Sandbox/test.txt', 'r')
for line in f:
    if len(line.strip()) > 0:
        print(line)

f.close()

#############################
# FILE OUTPUT
#############################
# Save the elements of a list to a file
list_to_save = range(100)

f = open('/home/nelson/Documents/CMEECoursework/Week2/Sandbox/testout.txt','w')
for i in list_to_save:
    f.write(str(i) + '\n') ## Add a new line at the end

f.close()

#############################
# STORING OBJECTS
#############################
# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11}

import pickle

f = open('/home/nelson/Documents/CMEECoursework/Week2/Sandbox/testp.p','wb') ## note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

## Load the data again
f = open('/home/nelson/Documents/CMEECoursework/Week2/Sandbox/testp.p','rb')
another_dictionary = pickle.load(f)
f.close()

print(another_dictionary)
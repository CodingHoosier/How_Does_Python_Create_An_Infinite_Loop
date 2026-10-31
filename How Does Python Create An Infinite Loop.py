# https://www.youtube.com/watch?v=kp1FIEdrw7M
# How Does Python Create An Infinite Loop?
# We'll use this library 
#  in an example, below.
import itertools
# The simplest infinite loop...
# A while loop runs as long as
#  the condition is true. 
# In this example, 
#  it's True forever.
# The loop never ends!
# So, we'll build in a break
#  statement to get us out.
while True:
    print("We're stuck in this loop!")
    print("Thank goodness for the break statement.")
    break
# Use a for loop 
#  to acheive infinity...
# For this example we'll add
#  a break statement.
# The count() steps 
#  up to infinity, sort-of.
for i in itertools.count():   
    print(i) 
    # Example condition 
    #  to break the loop
    if i > 3:
        break
# A somewhat sily example...
# Create a logical expresion
#  that's always true
#  and never changes.
# 0 is always less than 1.
while 0 < 1:
    print("We're stuck in this odd loop!")
    print("Thank goodness for the break statement.")
    break

#!/usr/bin/env python
# coding: utf-8

# In[1]:



def add(a, b):
    sum = a + b
    return sum

def sub(a, b):
    diff = a - b
    return diff

def mul(a, b):
    multi = a*b
    return multi

def div(a, b):
    divi = a/b
    return divi

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The Sum is: ", add(a,b))
print("The Difference is: ", sub(a,b))
print("The product is: ", mul(a,b))
print("The answer is: ", div(a,b))


# In[ ]:





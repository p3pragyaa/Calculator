#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def calculate(expression):
    # Remove all non-digit and non-operator characters
    expression = re.sub(r'[^\d+\-*/().]', '', expression)

    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except:
        return "Error: Invalid expression"

while True:
    user_input = input("Enter an expression (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    result = calculate(user_input)
    print("Result:", result)


# In[ ]:





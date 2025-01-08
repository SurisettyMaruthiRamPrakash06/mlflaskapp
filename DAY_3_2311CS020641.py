#!/usr/bin/env python
# coding: utf-8

# # Write a Python program that takes a student's marks in three subjects as input.
# 
# ### If the average is greater than or equal to 90, print "Grade: A".
# ### If the average is between 80 and 89, print "Grade: B".
# ### If the average is between 70 and 79, print "Grade: C".
# ### Otherwise, print "Grade: Fail".

# In[2]:


marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

average = (marks1 + marks2 + marks3) / 3

if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")


# In[1]:


marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

average = (marks1 + marks2 + marks3) / 3

if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")


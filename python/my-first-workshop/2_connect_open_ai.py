#======================================================
# Create Basic Project to prepare for the workshop
#======================================================

#--------------------
# Import libraries
#--------------------
from openai import OpenAI
import os


#--------------------
# Function create and call OpenAI 
# with Chat Completions API
#--------------------
def call_compleation():
    return "Hello from my-first-function!"

#--------------------
# Function create and call OpenAI
# with Chat Responses API
#--------------------
def call_responses():
    return "Hello from my-first-function!"

#--------------------
# Set default to call main function
#--------------------
def main():
    print(my_first_function())

if __name__ == "__main__":
    main()

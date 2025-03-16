#======================================================
# Create Basic Project to prepare for the workshop
#======================================================

#--------------------
# Import libraries
#--------------------
from dotenv import load_dotenv
from openai import OpenAI
import os
import json

#--------------------
# Define Constants
#--------------------
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#--------------------
# Initialize OpenAI client
#--------------------
client = OpenAI(api_key=OPENAI_API_KEY)

#--------------------
# Function create and call OpenAI 
# with Chat Completions API
# Response from openAI is a JSON object like this:
# 
#--------------------
def call_compleation():
    completionResponse = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": "Write one-sentence about me",
            }
        ],
    )
    return completionResponse

#--------------------
# Function create and call OpenAI
# with Chat Responses API
#--------------------
def call_responses():
    responseResponse = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "user",
                "content": "Write one-sentence about me",
            }
        ],
    )
    return responseResponse

#--------------------
# Set default to call main function
#--------------------
def main():
    completion_response = call_compleation()
    response_response = call_responses()
    
    #Print out for completion API
    print("\n===== Completion API Object =====\n")
    print(completion_response.choices[0].message.content)
    print(f"\nFull response: {completion_response}")

    #Print out for response API
    print("\n\n===== Response API Object =====\n")
    print(response_response.output_text)
    print(f"\nFull response: {response_response}")

if __name__ == "__main__":
    main()


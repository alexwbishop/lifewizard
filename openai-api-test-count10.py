# purpose: functionality testing with the openai api

# first load virtual env with: source openai-env/bin/activate
# then: source ~/.zshrc (to load the interactive shell)
# to confirm shell has loaded your key: echo $OPENAI_API_KEY
import openai
import time
from openai import OpenAI
# Initialize the OpenAI client to interact with the OpenAI API
client = OpenAI()

# record the time before the request is sent
start_time = time.time()

print(f"Sending request to OpenAI API...")
try:
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  # The main input is the 'messages' parameter. Messages must be an array of message 
  # objects, where each object has a role (either "system", "user", or "assistant") and content.
  messages=[
    # Conversations are formatted with a system message first, 
    # followed by alternating user and assistant messages.
    {"role": "system", "content": "You are a helpful assistant."},

    # The user messages provide requests or comments for the assistant to respond to. 
    {"role": "user", "content": "What number comes after 1 and before 2?"},

    # Assistant messages store previous assistant responses, but can also be 
    # written by you to give examples of desired behavior.    
    {"role": "assistant", "content": "3."},

    # Ask the assistant to count to 100
    {'role': 'user', 'content': 'Prove it to me! Count to 10, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'}
  ],
  # sets the 'temperature' for the response
  temperature=0,
    # sets the maximum number of tokens allowed in the response
  #max_tokens=250
)
# error messages to be printed if api key is not loaded
except openai.APIError as e:
  #Handle API error here, e.g. retry or log
  print(f"OpenAI API returned an API Error: {e}")
  pass
except openai.APIConnectionError as e:
  #Handle connection error here
  print(f"Failed to connect to OpenAI API: {e}")
  pass
except openai.RateLimitError as e:
  #Handle rate limit error (we recommend using exponential backoff)
  print(f"OpenAI API request exceeded rate limit: {e}")
  pass

# calculate the time it took to receive the response
response_time = time.time() - start_time

# print the time delay and text received
print(f"Success! Full response received {response_time:.2f} seconds after request.")
#print(f"Full response received:\n{response}")
print(f"============================================================================\n")

# Extract the first message (signified by [0]) from the response choices returned by the API
reply = response.choices[0].message
# print the reply extracted from the API response
#print(f"Extracted reply: \n{reply}")
# print the extracted response content
reply_content = response.choices[0].message.content
print(f"ChatGPT: {reply_content}")
print("\n============================================================================")
print("That's the end of this chat!\nExiting...")
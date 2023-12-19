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
    # Conversations can be as short as one message or many back and forth turns.
    # Typically, a conversation is formatted with a system message first, 
    # followed by alternating user and assistant messages.

    # The "system" message helps set the behavior of the assistant. For example, you 
    # can modify the personality of the assistant or provide specific instructions 
    # about how it should behave throughout the conversation. However note that the 
    # system message is optional and the model’s behavior without a system message 
    # is likely to be similar to using a generic message such as "You are a helpful assistant."
    {"role": "system", "content": "You are a helpful assistant."},

    # The user messages provide requests or comments for the assistant to respond to. 
    {"role": "user", "content": "Who won the world series in 2020?"},

    # Assistant messages store previous assistant responses, but can also be 
    # written by you to give examples of desired behavior.    
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    # another example of desired behavior (question and response):
    {"role": "user", "content": "Where was it played?"},
    {"role": "assistant", "content": "The World Series in 2020 was played at the Globe Life Field, in Arlington, Texas."},
    # a user question is posed without an assistant response, which generates a response from the model:
    {"role": "user", "content": "Who did they defeat?"},
],
  # sets the 'temperature' for the response
  # between 0 and 2. The default value for temperature is usually set to 1.
  # 0 is most precise, 2 is most random.
  temperature=1,
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
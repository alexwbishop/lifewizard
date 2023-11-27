# purpose: functionality testing with the openai api
import openai
import time
from openai import OpenAI
client = OpenAI()

# record the time before the request is sent
start_time = time.time()

print(f"Sending request to OpenAI API...")
try:
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
      {"role": "user", "content": "Compose an 8-line poem that explains the difference between enums and constants in programming."}
    ],
    # sets the 'temperature' for the response (0 - 2)
    temperature=0.5,
  )
# print error exceptions if api key is not loaded
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
poem = response.choices[0].message.content
print(f"ChatGPT:\n{poem}")
print("\n============================================================================")
print("That's the end of this chat!\nExiting...")